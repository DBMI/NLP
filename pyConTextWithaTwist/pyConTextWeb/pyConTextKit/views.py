#Copyright 2010 Annie T. Chen
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
"""
This module contains the views that are used in the pyConTextKit application. 
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, RequestContext
import csv
import os
from django.utils.encoding import smart_str, smart_unicode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#connection for raw sql
from django.db import connection, transaction
from pyConTextKit.models import *
from pyConTextKit.criticalFinderGraph import criticalFinder, modifies, getParser
from pyConTextGraphV2.itemData import itemData, contextItem
from pyConTextKit.forms import *
from csvparser import csvParser

from django.forms.models import modelformset_factory

def index(request):
    """
    This in the index page.
    """
    #the following lines of code loads the settings in itemDatumSet as the default
    #criterion set
    #itemDatum.objects.all().update(include=0)
    #testset = itemDatumSet.objects.filter(setname__contains="SO")
    #for i in testset:
    #    j = itemDatum.objects.get(pk=i.itemDatum_id)
    #    print j.id, j.include, i.include
    #    j.include = i.include
    #    j.save()
    return render_to_response('pyConTextKit/index.html',context_instance=RequestContext(request))

def logout_view(request):
    """
    This logs the user out of the application.
    """
    logout(request)
    return render_to_response('registration/logout.html',context_instance=RequestContext(request))
    
def run(request):
    """
    This executes the Annotate feature.
    """
    if request.method == "POST":
        rform = RunForm(data = request.POST)
        if rform.is_valid():
            dataset = rform.cleaned_data['dataset']
            category = rform.cleaned_data['category']
            limit = rform.cleaned_data['limit']
            label = rform.cleaned_data['label']
            parser = getParser()
            (options, args) = parser.parse_args()
            options.dataset = dataset
            if(category == ''):
                options.category = 'all'
            else:
                options.category = category
            options.number=limit            
            
            pec = criticalFinder(options)
            pec.processReports()

            return HttpResponseRedirect(reverse('pyConTextKit.views.complete'))
        else:
            print rform.errors

    else:
        rform=RunForm()
        
    return render_to_response('pyConTextKit/run.html', {'form': rform,},context_instance=RequestContext(request))

def complete(request):
    """
    This page is rendered by the run view when the Annotate feature is finished.
    """
    return render_to_response('pyConTextKit/complete.html',context_instance=RequestContext(request))

"""
	UPDATED 7/27/12 G.D.
	Changed reference from itemDatum object to Lexical object, formset shares same names w/ Lexical's 
	names, they did not need modification. (Line 122, Declaration of formset)
"""
def itemData_view(request):
    itemFormSet = modelformset_factory(Lexical, fields=('id',), extra=0)
    sform = SearchForm(data = request.POST)
    if request.method == "POST" and sform.is_valid():
        term = sform.cleaned_data['term']
        if term != '':
            #print "non-space"
            #literal__contains looks at field, literal and checks against term
            formset = itemFormSet(queryset = Lexical.objects.filter(literal__contains=term))
            return render_to_response('pyConTextKit/itemdata.html',{'formset': formset, 'form': sform,},context_instance=RequestContext(request))
        else:
            formset = itemFormSet(request.POST, request.FILES)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse('pyConTextKit.views.itemData_complete'))               
    formset = itemFormSet()
    return render_to_response("pyConTextKit/itemdata.html", {
        "formset": formset,'form': sform,}, context_instance=RequestContext(request))
        
"""
	UPDATED 7/27/12 G.D.
	Removed supercategory and replaced w/ category, not sure if we want this method anymore
"""
def itemData_filter(request, cat):
    """
    This method takes a supercategory name as an argument and renders a view of
    the criteria in this supercategory.
    """
    itemFormSet = modelformset_factory(Lexical, fields=('id',), extra=0)
    sform = SearchForm(data = request.POST)
    formset = itemFormSet(queryset=itemDatum.objects.filter(category=cat))
    return render_to_response('pyConTextKit/itemdata.html',{'formset': formset,'form': sform,},context_instance=RequestContext(request))

"""
	UPDATED 7/27/12
	Changed reference from itemDatum to Lexical
"""
def itemData_edit(request, itemData_id=None):
    """
    This method takes an Lexical ID as an argument and renders a form for the
    user to edit the specified extraction criterion.  If no argument is supplied,
    a blank form is rendered, which the user can use to enter a new criterion.
    
    Note: A useful addition to this would be examples that the user can use as
    a reference.
    """
    intro="""<p>This application employs Python regular expressions. Refer to the key below
    for guidance on how to create regular expressions.<p><b>\s:</b> space<br><b>|:</b> or<br>
    <b>\w:</b> alphanumeric character or underscore (equivalent to [a-zA-Z0-9_])<br>
    <b>*:</b> match one or more repetitions of the preceding regular expression<br>
    <b>?:</b> matches 0 or 1 of the preceding regular expressions<br>
    You can learn more about Python regular expressions at:
    <a href="http://docs.python.org/library/re.html">http://docs.python.org/library/re.html</a>"""
  
    iform = itemForm(request.POST or None,instance=itemData_id and Lexical.objects.get(id=itemData_id))
    if request.method == "POST" and iform.is_valid:
        iform.save()
        return HttpResponseRedirect(reverse('pyConTextKit.views.itemData_complete'))
    	
    return render_to_response('pyConTextKit/itemdata_edit.html', {'form': iform, 'intro': intro}, context_instance=RequestContext(request))
    
def itemData_complete(request):
    return render_to_response('pyConTextKit/itemdata_complete.html',context_instance=RequestContext(request))
     
def output_alerts(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=alerts.csv'

    writer = csv.writer(response)
    alerts=Alert.objects.all()
    writer.writerow(['id', 'reportid', 'category', 'alert','report'])
    for a in alerts:
        writer.writerow([smart_str(a.id), smart_str(a.reportid), smart_str(a.category), smart_str(a.alert), smart_str(a.report)])
    return response
    
def output_results(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results.csv'

    writer = csv.writer(response)
    results=Result.objects.all()
    writer.writerow(['id', 'reportid', 'category', 'disease','uncertainty','historical','literal'])
    for r in results:
        writer.writerow([smart_str(r.id), smart_str(r.reportid), smart_str(r.category),
                         smart_str(r.disease), smart_str(r.uncertainty), smart_str(r.historical), smart_str(r.literal)])
    return response

def reports(request):
    report_list=Report.objects.all()
    paginator = Paginator(report_list, 10) # Show 10 reports per page
    page = int(request.GET.get('page','1'))
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reports = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reports = paginator.page(paginator.num_pages)
   
    return render_to_response('pyConTextKit/reports.html', {"report": reports},context_instance=RequestContext(request))

def report_detail(request, reportid):
    try:
        r = Report.objects.get(id=reportid)
    except Report.DoesNotExist:
        raise Http404
    return render_to_response('pyConTextKit/report_detail.html',{'report': r},context_instance=RequestContext(request))

def alerts(request):
    if request.method == "POST":
        rform = DocClassForm(data = request.POST)
        if rform.is_valid():
            limit_pos = rform.cleaned_data['limit_pos']
            uncertainty = rform.cleaned_data['uncertainty']
            limit_new = rform.cleaned_data['limit_new']
            if limit_pos:
                if uncertainty=='separate_uncertainty':
                    if limit_new:
                        print "here"
                        r=Result.objects.values('reportid','category','disease','uncertainty','historical').filter(disease="Pos").filter(historical="New").annotate(Count('id'))
                        print r
                    else:
                        r=Result.objects.values('reportid','category','disease','uncertainty','historical').filter(disease="Pos").annotate(Count('id'))
                elif uncertainty=='allow_uncertainty':
                    if limit_new:
                        r=Result.objects.values('reportid','category','disease','historical').filter(disease="Pos").filter(historical="New").annotate(Count('id'))
                    else:
                        r=Result.objects.values('reportid','category','disease','historical').filter(disease="Pos").annotate(Count('id'))
                else:
                    if limit_new:
                        r=Result.objects.values('reportid','category','disease','historical').filter(disease="Pos").filter(uncertainty="No").filter(historical="New").annotate(Count('id'))
                    else:
                        r=Result.objects.values('reportid','category','disease','historical').filter(disease="Pos").filter(uncertainty="No").annotate(Count('id'))
            else:
                if uncertainty=='separate_uncertainty':
                    if limit_new:
                        r=Result.objects.values('reportid','category','disease','uncertainty','historical').filter(historical="New").annotate(Count('id'))
                    else:
                        r=Result.objects.values('reportid','category','disease','uncertainty','historical').annotate(Count('id'))
                elif uncertainty=='allow_uncertainty':
                    if limit_new:
                        r=Result.objects.values('reportid','category','disease','historical').filter(historical="New").annotate(Count('id'))
                    else:
                        r=Result.objects.values('reportid','category','disease','historical').annotate(Count('id'))
                else:
                    if limit_new:
                        r=Result.objects.values('reportid','category','disease','historical').filter(uncertainty="No").filter(historical="New").annotate(Count('id'))
                    else:
                        r=Result.objects.values('reportid','category','disease','historical').filter(uncertainty="No").annotate(Count('id'))

            return render_to_response('pyConTextKit/alerts.html',{'alert': r},context_instance=RequestContext(request))
        else:
            print rform.errors
            print "error"

    else:
        rform=DocClassForm()
        
    return render_to_response('pyConTextKit/run_alert.html', {'form': rform,},context_instance=RequestContext(request))

def results(request):
    r=Result.objects.all()
    return render_to_response('pyConTextKit/results.html',{'result': r},context_instance=RequestContext(request))
    
def result_detail(request, result_id):
    try:
        r = Result.objects.get(id=result_id)
    except Result.DoesNotExist:
        raise Http404
    return render_to_response('pyConTextKit/result_detail.html', {'result': r},context_instance=RequestContext(request))

def stats(request): 
    a=Alert.objects.values('category','alert').annotate(Count('id'))
    return render_to_response('pyConTextKit/stats.html',{'alert': a},context_instance=RequestContext(request))
   
def report_text(request, reportid):
    if request.is_ajax() and request.method == 'POST':
        report = Report.objects.get(pk=request.POST.get('reportid', ''))
    return render_to_response('pyConTextKit/report_test.html', {'report':report}, context_instance=RequestContext(request))
    
def ajax_user_search( request ):
    if request.is_ajax():
        q = request.GET.get( 'q' )
        if q is not None:            
            results = Report.objects.get(pk=q)
            template = 'pyConTextKit/report_test.html'
            data = {
                'results': results,
            }
            return render_to_response( template, data, 
                                       context_instance = RequestContext( request ) )
                                       
def upload_csv(request):
	status = ''
	uploadDbForm = UploadDatabase(request.POST, request.FILES)
	if request.method == 'POST' and uploadDbForm.is_valid:
		res = handle_uploaded_file(request.FILES['csvfile'], request.cleaned_data['label'])
		uploadDbForm.save()
		"""if res == False:
			status = '<p style="color:red;">File was not CSV, or formatted incorrectly</p>'
		else:
			status = '<p style="color:green;">Database was successfully modified</p>'"""
		return render_to_response('pyConTextKit/upload_db.html',{'status': status, 'form': uploadDbForm},context_instance=RequestContext(request))
	else:
		uploadDbForm = UploadDatabase()	
	return render_to_response('pyConTextKit/upload_db.html',{'status': status, 'form': uploadDbForm},context_instance=RequestContext(request))
			
def handle_uploaded_file(f, label):
	user_home = os.getenv('HOME')
	pyConTextWebHome = os.path.join(user_home,'pyConTextWeb','templates','media','csvuploads') #this needs to be modifed to accomodate othe user's home directory
	destPath = os.path.join(pyConTextWebHome,str(int(round(time.time() * 1000)))+'.csv')
	destination = open(destPath,'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	#then implement the csvparser class here
	c = csvParser(destPath, label)
	return c.iterateRows() #updates DB with table information

def edit_report(request, eid=None):
	eReport = EditReport(request.POST or None,instance=eid and Report.objects.get(id=eid))
	if request.method == "POST" and eReport.is_valid:
		eReport.save()
        return HttpResponseRedirect('pyConTextKit')
	
	return render_to_response('pyConTextKit/edit_report.html', {'form': eReport}, context_instance=RequestContext(request))