# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Dna_Profile.D21S11_left'
        db.alter_column(u'profiles_dna_profile', 'D21S11_left', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'Dna_Profile.FGA_right'
        db.alter_column(u'profiles_dna_profile', 'FGA_right', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Dna_Profile.D21S11_right'
        db.alter_column(u'profiles_dna_profile', 'D21S11_right', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'Dna_Profile.FGA_left'
        db.alter_column(u'profiles_dna_profile', 'FGA_left', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Dna_Profile.D21S11_left'
        db.alter_column(u'profiles_dna_profile', 'D21S11_left', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3))

        # Changing field 'Dna_Profile.FGA_right'
        db.alter_column(u'profiles_dna_profile', 'FGA_right', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=4))

        # Changing field 'Dna_Profile.D21S11_right'
        db.alter_column(u'profiles_dna_profile', 'D21S11_right', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3))

        # Changing field 'Dna_Profile.FGA_left'
        db.alter_column(u'profiles_dna_profile', 'FGA_left', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=4))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.dna_profile': {
            'AMEL_left': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'AMEL_right': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'CSF1PO_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'CSF1PO_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D13S317_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D13S317_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D16S539_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D16S539_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D18S51_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D18S51_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D19S433_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D19S433_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D21S11_left': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'D21S11_right': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'D2S1338_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D2S1338_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D3S1358_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D3S1358_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D5S818_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D5S818_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D7S820_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D7S820_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D8S1179_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'D8S1179_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'FGA_left': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2'}),
            'FGA_right': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2'}),
            'Meta': {'object_name': 'Dna_Profile'},
            'TH01_left': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'TH01_right': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1'}),
            'TPOX_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'TPOX_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Profile']"}),
            'vWA_left': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'vWA_right': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'})
        },
        u'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'merge_accounts': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'street_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'street_number': ('django.db.models.fields.IntegerField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'unit_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']