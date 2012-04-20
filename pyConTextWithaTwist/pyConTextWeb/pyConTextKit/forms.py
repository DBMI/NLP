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
This module contains the forms that are used in the pyConTextKit application. 
"""
from django import forms
from django.forms import ModelForm
from pyConTextKit.models import itemDatum, Report

UNCERTAINTY_CHOICES = (('separate_uncertainty','distinguish certainty from uncertainty'), ('allow_uncertainty','do not distinguish certainty from uncertainty'), ('no_uncertainty','do not include instances of uncertainty'))

class SearchForm(forms.Form):
    """
    A form that takes the input for a simple search.
    """
    term = forms.CharField(label = 'Search term', required=False)

class RunForm(forms.Form):
    """
    This form enables the user to specify settings for Annotate (formerly called "Analyze").
    """
    dataset = forms.ChoiceField(label = 'Report dataset', choices=[], required=False)
    category = forms.CharField(label = 'Target category', required=False)
    limit = forms.IntegerField(required=False)
    def __init__(self, *args, **kwargs):
        super(RunForm, self).__init__(*args, **kwargs)
        self.fields['dataset'].choices = Report.objects.all().values_list("dataset","dataset").distinct()

class DocClassForm(forms.Form):
    """
    This form accepts user input for classifying documents.
    """
    limit_pos = forms.BooleanField(label="Positive Findings Only", required=False,initial=True)
    limit_new = forms.BooleanField(label="New Findings Only", required=False,initial=True)
    uncertainty = forms.ChoiceField(widget=forms.RadioSelect, choices=UNCERTAINTY_CHOICES,initial={'separate_uncertainty','separate_uncertainty'})
    def __init__(self, *args, **kwargs):
        super(DocClassForm, self).__init__(*args, **kwargs)
    
class itemForm(forms.ModelForm):
    """
    This form for the itemDatum class employs the default ModelForm.
    """
    class Meta:
        model = itemDatum
        
class ReportForm(forms.Form):
    """
    This form enables the user to select a report to view.
    """
    REPORT_CHOICES = [(i.id, i.id) for i in Report.objects.all()]
    REPORT_CHOICES.insert(0, ('', '-- choose a report number first --'))
    
    id = forms.ChoiceField(choices=REPORT_CHOICES, widget=forms.Select(attrs={'onchange':'get_report_number();'}))
    text = forms.CharField()


class UploadDatabase(forms.Form):
	"""
	This form enables the user to upload a custom database file
	"""
	databaseFile = forms.FileField()