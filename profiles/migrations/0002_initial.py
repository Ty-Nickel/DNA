# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'profiles_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'profiles', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'profiles_profile')


    models = {
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['profiles']