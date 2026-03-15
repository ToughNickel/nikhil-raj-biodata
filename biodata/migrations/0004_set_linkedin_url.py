from django.db import migrations


def set_linkedin_url(apps, schema_editor):
    PersonalInfo = apps.get_model('biodata', 'PersonalInfo')
    PersonalInfo.objects.filter(pk=1).update(
        linkedin_url='https://www.linkedin.com/in/nikhil-raj-swe/'
    )


def clear_linkedin_url(apps, schema_editor):
    PersonalInfo = apps.get_model('biodata', 'PersonalInfo')
    PersonalInfo.objects.filter(pk=1).update(linkedin_url='')


class Migration(migrations.Migration):
    dependencies = [
        ('biodata', '0003_personalinfo_linkedin_url'),
    ]
    operations = [
        migrations.RunPython(set_linkedin_url, clear_linkedin_url),
    ]
