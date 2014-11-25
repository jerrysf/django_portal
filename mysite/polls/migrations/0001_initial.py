# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ID_mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcomponent_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('sublevel_id', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'ID Mapping',
                'verbose_name_plural': 'ID Mapping',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product_Phases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('entity_build', models.IntegerField()),
                ('QT_sanity_minorRegression_SWBT', models.IntegerField()),
                ('majorRegression', models.IntegerField()),
                ('fullRegression', models.IntegerField()),
                ('neve', models.IntegerField()),
                ('timestamp', models.DateTimeField(verbose_name=b'data upload time')),
                ('contact_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Product Phases',
                'verbose_name_plural': 'Product Phases',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DCM_Phases',
            fields=[
                ('product_phases_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Product_Phases')),
            ],
            options={
                'verbose_name': 'DCM Phases',
                'verbose_name_plural': 'DCM Phases',
            },
            bases=('polls.product_phases',),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField(default=0)),
                ('product_name', models.CharField(max_length=200)),
                ('bu_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcomponent_Phases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcomponent_id', models.IntegerField(default=0)),
                ('component_CI_pre_commit_phase', models.IntegerField()),
                ('UT_MT', models.IntegerField()),
                ('SCT_build', models.IntegerField()),
                ('SCT_FT', models.IntegerField()),
                ('Promotion', models.IntegerField()),
                ('Additional', models.IntegerField()),
                ('timeStamp', models.DateTimeField(verbose_name=b'data upload time')),
                ('contact_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Subcomponent Phases',
                'verbose_name_plural': 'Subcomponent Phases',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcomponents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcomponent_id', models.IntegerField(default=0)),
                ('subcomponent_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sub Components',
                'verbose_name_plural': 'Sub Components',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sublevel_Phases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sublevel_id', models.IntegerField(default=0)),
                ('entity_build', models.IntegerField()),
                ('QT_sanity_minorRegression_SWBT', models.IntegerField()),
                ('fullRegression', models.IntegerField()),
                ('neve', models.IntegerField()),
                ('timestamp', models.DateTimeField(verbose_name=b'data upload time')),
                ('contact_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sublevel Phases',
                'verbose_name_plural': 'Sublevel Phases',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sublevels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sublevel_id', models.IntegerField(default=0)),
                ('sublevel_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sub Levels',
                'verbose_name_plural': 'Sub Levels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TDD_LTE_Phases',
            fields=[
                ('product_phases_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Product_Phases')),
            ],
            options={
                'verbose_name': 'TDD-LTE Phases',
                'verbose_name_plural': 'TDD-LTE Phases',
            },
            bases=('polls.product_phases',),
        ),
        migrations.CreateModel(
            name='WMP_cplane_Phases',
            fields=[
                ('sublevel_phases_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Sublevel_Phases')),
            ],
            options={
                'verbose_name': 'WMP Cplane Phases',
                'verbose_name_plural': 'WMP Cplane Phases',
            },
            bases=('polls.sublevel_phases',),
        ),
        migrations.CreateModel(
            name='WMP_dl_phy_Phases',
            fields=[
                ('subcomponent_phases_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Subcomponent_Phases')),
            ],
            options={
                'verbose_name': 'WMP dl phy Phases',
                'verbose_name_plural': 'WMP dl phy Phases',
            },
            bases=('polls.subcomponent_phases',),
        ),
        migrations.CreateModel(
            name='WMP_Phases',
            fields=[
                ('product_phases_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='polls.Product_Phases')),
            ],
            options={
                'verbose_name': 'WMP Phases',
                'verbose_name_plural': 'WMP Phases',
            },
            bases=('polls.product_phases',),
        ),
    ]
