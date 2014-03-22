# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'dna_profile')

        # Adding model 'Dna'
        db.create_table(u'dna_dna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'dna', ['Dna'])


    def backwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'dna_profile', (
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=6)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dna', ['Profile'])

        # Deleting model 'Dna'
        db.delete_table(u'dna_dna')


    models = {
        u'dna.dna': {
            'Meta': {'object_name': 'Dna'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['dna']