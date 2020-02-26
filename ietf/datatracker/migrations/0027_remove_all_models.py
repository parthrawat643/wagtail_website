# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-07 21:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatracker', '0026_auto_20180202_1623'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Charter',
        ),
        migrations.RemoveField(
            model_name='datatrackermeta',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='InternetDraft',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='RFC',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='RoleName',
        ),
        migrations.DeleteModel(
            name='WorkingGroup',
        ),
        migrations.DeleteModel(
            name='DatatrackerMeta',
        ),
    ]
