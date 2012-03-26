#Copyright 2010-2012 Brian E. Chapman, Annie T. Chen, Glenn Dayton IV,
# Rutu Mulkar-Mehta
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
This module contains the models that are used in the pyConTextKit application.

This application uses the following models:

1) itemDatum: extraction criteria

2) itemDatumSet: a table that stores default extraction criteria settings for
application (e.g. on/off)

3) Report: the reports used by the application

4) Alert: contains a document-level classifications for extracted instances

5) Result: contains each instance identified when Annotate function is run

Note: The get_all_fields method is redundant. A model should be defined for this
application, and then have the other models inherit from it.
"""
from django.db import models
from django.contrib.auth.models import User

class creator(models.Model):
    """Valid creators for itemDatum"""
    name = models.CharField(max_length=250)
    """
    If we decide to base the creator off of the currently logged in user:
    Precondition: User must be authenticated

    user = models.ForeignKey(User, unique=True)
    """
    def __unicode__(self):
    	"""return user"""
        return id # should I also return the id? => Yes, creators could have the same name. -Glenn

class supercategory(models.Model): 
    name = models.CharField(max_length=250)

class category(models.Model):
    name = models.CharField(max_length=250)

class itemRule(models.Model):
    rule = models.CharField(max_length=250)

class collection(models.Model):
    name = models.CharField(max_length=250)
    creator = models.ForeignKey('creator')
    
class itemDatum(models.Model):
    supercategory = models.ForeignKey('supercategory')
    category = models.ForeignKey(category)
    literal = models.CharField(max_length=250)
    re = models.CharField(max_length=250,blank=True)
    re.help_text='regular expression'
    rule = models.ForeignKey('itemRule')
    creator = models.ForeignKey('creator')
    include = models.BooleanField() # we want to delete include from itemDatum
    def __unicode__(self):
        return self.literal
    
class itemDatumSet(models.Model):
    setname = models.CharField(max_length=50)
    itemDatum = models.ForeignKey('itemDatum')
    include = models.BooleanField()
    def __unicode__(self):
        return self.setname

class ReportType(models.Model):
    name = models.CharField(max_length=250)

class Report(models.Model):
    dataset = models.ForeignKey('collection') 
    reportid = models.TextField()
    reportType = models.ForeignKey('ReportType')
    report = models.TextField()
    def __unicode__(self):
        return str(self.reportid)
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:
    
            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr( self, get_choice):
                value = getattr( self, get_choice)()
            else:
                try :
                    value = getattr(self, fname)
                except User.DoesNotExist:
                    value = None
    
            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :

                fields.append(
                  {
                   'label':f.verbose_name, 
                   'name':f.name, 
                   'value':value,
                  }
                )
        return fields
# Can we generalize the Alert class to be an application class that is built by
# the user?
class Alert(models.Model):
    reportid = models.IntegerField()
    category = models.TextField()
    alert = models.IntegerField()
    report = models.TextField()
    def __unicode__(self):
        return str(self.reportid)
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:
    
            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr( self, get_choice):
                value = getattr( self, get_choice)()
            else:
                try :
                    value = getattr(self, fname)
                except User.DoesNotExist:
                    value = None
    
            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :
    
                fields.append(
                  {
                   'label':f.verbose_name, 
                   'name':f.name, 
                   'value':value,
                  }
                )
        return fields
# Don't know that we want to store this back into the database
# How would we make results general?
class Result(models.Model):
    reportid = models.IntegerField()
    category = models.TextField()
    disease = models.TextField()
    uncertainty = models.TextField()
    historical = models.TextField()
    literal = models.TextField()
    matchedphrase = models.TextField()
    def __unicode__(self):
        return str(self.reportid)
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:
    
            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr( self, get_choice):
                value = getattr( self, get_choice)()
            else:
                try :
                    value = getattr(self, fname)
                except User.DoesNotExist:
                    value = None
    
            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :
    
                fields.append(
                  {
                   'label':f.verbose_name, 
                   'name':f.name, 
                   'value':value,
                  }
                )
        return fields
