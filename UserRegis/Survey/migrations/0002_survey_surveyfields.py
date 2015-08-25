# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survey_name', models.CharField(max_length=200)),
                ('end_date', models.DateTimeField(verbose_name=b'Complete by')),
                ('survey_description', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('response', models.CharField(default=b'NA', max_length=5000)),
                ('survey', models.ForeignKey(to='Survey.Survey')),
            ],
        ),
    ]
