# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '__first__'),
        ('cms', '0010_migrate_use_structure'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScientistPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, primary_key=True, to='cms.CMSPlugin')),
                ('scientist', models.ForeignKey(related_name='plugins', to='lab_members.Scientist')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
