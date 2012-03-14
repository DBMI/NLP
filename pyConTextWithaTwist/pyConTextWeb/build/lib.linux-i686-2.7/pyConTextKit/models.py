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

class itemDatum(models.Model):
    supercategory = models.CharField(max_length=250)
    literal = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    re = models.CharField(max_length=250,blank=True)
    re.help_text='regular expression'
    rule = models.CharField(max_length=250,blank=True)
    creator = models.CharField(max_length=16)
    include = models.BooleanField()
    def __unicode__(self):
        return self.literal
    
class itemDatumSet(models.Model):
    setname = models.CharField(max_length=50)
    itemDatum = models.ForeignKey('itemDatum')
    include = models.BooleanField()
    def __unicode__(self):
        return self.setname
    
class Report(models.Model):
    dataset = models.TextField()
    hbid = models.TextField()
    reportid = models.TextField()
    reportType = models.TextField()
    report = models.TextField()
    impression = models.TextField()
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
