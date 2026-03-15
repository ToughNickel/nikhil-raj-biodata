# -*- coding: utf-8 -*-
from django.db import migrations


def seed_data(apps, schema_editor):
    PersonalInfo = apps.get_model('biodata', 'PersonalInfo')
    Education = apps.get_model('biodata', 'Education')
    Property = apps.get_model('biodata', 'Property')
    CareerEntry = apps.get_model('biodata', 'CareerEntry')
    FamilyMember = apps.get_model('biodata', 'FamilyMember')
    FamilyMemberTag = apps.get_model('biodata', 'FamilyMemberTag')
    LineageNode = apps.get_model('biodata', 'LineageNode')
    HeritageInfo = apps.get_model('biodata', 'HeritageInfo')
    MoolCard = apps.get_model('biodata', 'MoolCard')
    Greeting = apps.get_model('biodata', 'Greeting')
    NavLink = apps.get_model('biodata', 'NavLink')

    # ── PersonalInfo (singleton pk=1) ──
    PersonalInfo.objects.create(
        pk=1,
        full_name='Nikhil Raj',
        sanskrit_greeting='।। ॐ गणेशाय नम: ।।',
        role_title='Senior Software Engineer',
        current_company='Atlassian',
        company_color='#2684FF',
        location_primary='Bangalore, India',
        location_roots='Sitamarhi, Bihar',
        height="6'0\"",
        date_of_birth='1996-04-20',
        complexion='Fair',
        current_address="#212, Ram's Lakeview Meadows Apartment, Vinayakanagar",
        native_village='Sisautia, Sitamarhi',
        native_district='District Sitamarhi, Bihar',
        phone='9900817051',
        footer_sanskrit='।। इति शुभम् ।।',
        copyright_year=2026,
    )

    # ── Education ──
    Education.objects.create(
        degree='B.E. Computer Science',
        institution='University Visvesvaraya College of Engineering (UVCE), Bangalore University',
        year_range='2014\u20132018',
        description='Class of 2014\u20132018',
        order=0,
    )
    Education.objects.create(
        degree='12th (Computer Science)',
        institution='Kendriya Vidyalaya, Air Force Station, Yelahanka',
        year_range='2013\u20132014',
        description='',
        order=1,
    )

    # ── Properties ──
    Property.objects.create(name='Residence in Bangalore', order=0)
    Property.objects.create(name='Own Property in Jamshedpur', order=1)

    # ── Career Entries ──
    CareerEntry.objects.create(
        company_name='Atlassian', badge_letter='A',
        badge_css_class='badge-atlassian',
        role='Senior Software Engineer',
        location='Bangalore', period='', is_current=True, order=0,
    )
    CareerEntry.objects.create(
        company_name='Microsoft', badge_letter='M',
        badge_css_class='badge-microsoft',
        role='Senior Software Engineer / Software Engineer 2',
        location='Bangalore', period='', is_current=False, order=1,
    )
    CareerEntry.objects.create(
        company_name='VMware', badge_letter='V',
        badge_css_class='badge-vmware',
        role='Member of Technical Staff (MTS)',
        location='Bangalore', period='', is_current=False, order=2,
    )
    CareerEntry.objects.create(
        company_name='UVCE, Bangalore University', badge_letter='U',
        badge_css_class='badge-uvce',
        role='B.E. Computer Science & Engineering',
        location='', period='2014 \u2013 2018', is_current=False, order=3,
    )
    CareerEntry.objects.create(
        company_name='Kendriya Vidyalaya, AFS Yelahanka', badge_letter='K',
        badge_css_class='badge-kv',
        role='12th Grade \u2014 Computer Science',
        location='', period='2013 \u2013 2014', is_current=False, order=4,
    )

    # ── Family Members + Tags ──
    father = FamilyMember.objects.create(
        relation='Father',
        name='Shri Jata Shankar Lal Karn',
        description='Ex-Indian Air Force Personnel. Currently working in State Bank of India (SBI) at Bangalore.',
        contact='9900817051', extra_info='', order=0,
    )
    FamilyMemberTag.objects.create(member=father, label='Ex-Indian Air Force', is_amber=True, order=0)
    FamilyMemberTag.objects.create(member=father, label='SBI, Bangalore', is_amber=False, order=1)

    mother = FamilyMember.objects.create(
        relation='Mother',
        name='Mrs Chhaya Karn',
        description='Homemaker, B.A.',
        contact='', extra_info='Naihar: Chahuta, Madhubani, Bihar', order=1,
    )
    FamilyMemberTag.objects.create(member=mother, label='Homemaker', is_amber=True, order=0)
    FamilyMemberTag.objects.create(member=mother, label='B.A.', is_amber=False, order=1)

    sister = FamilyMember.objects.create(
        relation='Sister (Younger \u2014 Married)',
        name='Mrs Niharika Karn',
        description='Software Developer at Tech Mahindra Pvt Ltd, Bangalore.',
        contact='', extra_info='', order=2,
    )
    FamilyMemberTag.objects.create(member=sister, label='Tech Mahindra', is_amber=False, order=0)
    FamilyMemberTag.objects.create(member=sister, label='Software Developer', is_amber=False, order=1)

    bil = FamilyMember.objects.create(
        relation='Brother-in-Law',
        name='Shri Harsh Prakash Karn',
        description='Senior Software Engineer in Volkswagen at Bangalore.',
        contact='', extra_info='', order=3,
    )
    FamilyMemberTag.objects.create(member=bil, label='Volkswagen', is_amber=False, order=0)
    FamilyMemberTag.objects.create(member=bil, label='Senior SE', is_amber=False, order=1)

    uncle = FamilyMember.objects.create(
        relation='Chacha (Uncle)',
        name='Shri Gauri Kant Lal Karn',
        description='Retired Indian Railway personnel. Residing at Tata Nagar, Jamshedpur, Jharkhand.',
        contact='', extra_info='', order=4,
    )
    FamilyMemberTag.objects.create(member=uncle, label='Retd. Indian Railway', is_amber=True, order=0)
    FamilyMemberTag.objects.create(member=uncle, label='Jamshedpur', is_amber=False, order=1)

    # ── Lineage Nodes ──
    LineageNode.objects.create(
        name_hindi='स्वर्गीय राम स्वरुप लाल', name_english='',
        role_label='Great-Grandfather (परपौत्र)', is_self=False, order=0,
    )
    LineageNode.objects.create(
        name_hindi='स्वर्गीय जय कांत लाल', name_english='',
        role_label='Grandfather (पौत्र)', is_self=False, order=1,
    )
    LineageNode.objects.create(
        name_hindi='श्री जटा शंकर लाल कर्ण', name_english='',
        role_label='Father (पुत्र)', is_self=False, order=2,
    )
    LineageNode.objects.create(
        name_hindi='', name_english='Nikhil Raj',
        role_label='Self', is_self=True, order=3,
    )

    # ── Heritage Info (singleton pk=1) ──
    HeritageInfo.objects.create(
        pk=1,
        gotra_hindi='भारद्वाज',
        gotra_english='Bhardwaj',
        closing_note='विशेष पंजीकार ताल्लुक।',
    )

    # ── Mool Cards ──
    MoolCard.objects.create(
        label_hindi='मूल (Mool)',
        text_hindi='मेहत संग रानीपुर डेरा, वास - सिसौटिया, श्री जटा शंकर लालक पुत्र, स्वर्गीय जय कांत लालक पौत्र, स्वर्गीय राम स्वरुप लालक परपौत्र।',
        order=0,
    )
    MoolCard.objects.create(
        label_hindi='मात्रिक (Matrik)',
        text_hindi='वसंतपुर संग जोंकी डेरा, वास - चहुटा, श्री मणि शंकर दत्तक दौहित्र, स्वर्गीय हरि देव दत्तक परदौहित्र, स्वर्गीय अयोध्या दत्तक पौत्रक दौहित्र।',
        order=1,
    )
    MoolCard.objects.create(
        label_hindi='मात मात्रिक (Maat Matrik)',
        text_hindi='केवटी संग दुधैल डेरा, वास - बेतौना, स्वर्गीय दर्प नारायण लालक दौहित्रिक पुत्र, स्वर्गीय हरि नंदन लालक परदौहित्रिक पुत्र, स्वर्गीय महेश लालक पौत्रक दौहित्रिक पुत्र।',
        order=2,
    )
    MoolCard.objects.create(
        label_hindi='पितृ मात्रिक (Pitri Matrik)',
        text_hindi='अटहर संग सुंदरपुर डेरा, वास - बिरौली, स्वर्गीय किशोरी लालक दौहित्रक पुत्र, स्वर्गीय दरबारी लालक परदौहित्रक पुत्र, स्वर्गीय लक्ष्मी शरण लालक पौत्रक दौहित्रक पुत्र।',
        order=3,
    )

    # ── Greetings ──
    for i, text in enumerate(['Namaste', 'Hello', 'नमस्ते', 'Welcome']):
        Greeting.objects.create(text=text, order=i)

    # ── Nav Links ──
    for i, (label, anchor) in enumerate([
        ('About', 'about'), ('Career', 'career'), ('Family', 'family'),
        ('Heritage', 'heritage'), ('Gallery', 'gallery'),
    ]):
        NavLink.objects.create(label=label, anchor=anchor, order=i)


def reverse_seed(apps, schema_editor):
    for model_name in [
        'NavLink', 'Greeting', 'MoolCard', 'HeritageInfo',
        'LineageNode', 'FamilyMemberTag', 'FamilyMember',
        'CareerEntry', 'Property', 'Education', 'GalleryImage', 'PersonalInfo',
    ]:
        apps.get_model('biodata', model_name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('biodata', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
