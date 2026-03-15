# -*- coding: utf-8 -*-
from django.db import migrations


def update_career_entries(apps, schema_editor):
    CareerEntry = apps.get_model('biodata', 'CareerEntry')

    # Update VMware: rename and add period
    CareerEntry.objects.filter(company_name='VMware').update(
        company_name='VMware (now Broadcom)',
        period='Jul 2018 \u2013 Jan 2022',
    )

    # Update Microsoft: add period
    CareerEntry.objects.filter(company_name='Microsoft').update(
        period='Jan 2022 \u2013 Aug 2025',
    )

    # Update Atlassian: add period
    CareerEntry.objects.filter(company_name='Atlassian').update(
        period='Dec 2025 \u2013 Present',
    )


def reverse_update(apps, schema_editor):
    CareerEntry = apps.get_model('biodata', 'CareerEntry')

    CareerEntry.objects.filter(company_name='VMware (now Broadcom)').update(
        company_name='VMware',
        period='',
    )
    CareerEntry.objects.filter(company_name='Microsoft').update(period='')
    CareerEntry.objects.filter(company_name='Atlassian').update(period='')


class Migration(migrations.Migration):
    dependencies = [
        ('biodata', '0004_set_linkedin_url'),
    ]
    operations = [
        migrations.RunPython(update_career_entries, reverse_update),
    ]
