from django.db import models


class PersonalInfo(models.Model):
    """Singleton model: stores the subject's core personal data."""
    full_name = models.CharField(max_length=100)
    sanskrit_greeting = models.CharField(max_length=200)
    hero_photo = models.ImageField(upload_to='profile/', blank=True)
    role_title = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100)
    company_color = models.CharField(max_length=7, default='#2684FF')
    location_primary = models.CharField(max_length=100)
    location_roots = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    complexion = models.CharField(max_length=50)
    current_address = models.TextField(blank=True)
    native_village = models.CharField(max_length=100)
    native_district = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(max_length=300, blank=True)
    footer_sanskrit = models.CharField(max_length=200)
    copyright_year = models.PositiveIntegerField(default=2026)

    class Meta:
        verbose_name = "Personal Info"
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={
            'full_name': 'Nikhil Raj',
            'sanskrit_greeting': '।। ॐ गणेशाय नम: ।।',
            'role_title': 'Senior Software Engineer',
            'current_company': 'Atlassian',
            'location_primary': 'Bangalore, India',
            'location_roots': 'Sitamarhi, Bihar',
            'height': "6'0\"",
            'date_of_birth': '1996-04-20',
            'complexion': 'Fair',
            'native_village': 'Sisautia, Sitamarhi',
            'native_district': 'District Sitamarhi, Bihar',
            'phone': '9900817051',
            'footer_sanskrit': '।। इति शुभम् ।।',
        })
        return obj


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_range = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Property(models.Model):
    name = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name


class CareerEntry(models.Model):
    company_name = models.CharField(max_length=100)
    badge_letter = models.CharField(max_length=5)
    badge_css_class = models.CharField(max_length=50)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True)
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Career Entry"
        verbose_name_plural = "Career Entries"

    def __str__(self):
        return f"{self.company_name} — {self.role}"


class FamilyMember(models.Model):
    relation = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact = models.CharField(max_length=100, blank=True)
    extra_info = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.relation})"


class FamilyMemberTag(models.Model):
    member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='tags')
    label = models.CharField(max_length=100)
    is_amber = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label


class LineageNode(models.Model):
    name_hindi = models.CharField(max_length=200, blank=True)
    name_english = models.CharField(max_length=200, blank=True)
    role_label = models.CharField(max_length=100)
    is_self = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name_hindi or self.name_english


class HeritageInfo(models.Model):
    """Singleton for gotra and heritage metadata."""
    gotra_hindi = models.CharField(max_length=100)
    gotra_english = models.CharField(max_length=100)
    closing_note = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Heritage Info"
        verbose_name_plural = "Heritage Info"

    def __str__(self):
        return f"Gotra: {self.gotra_english}"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class MoolCard(models.Model):
    label_hindi = models.CharField(max_length=100)
    text_hindi = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label_hindi


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('traditional', 'Traditional / Ethnic'),
        ('candid', 'Candid / Travel'),
        ('family', 'Family'),
        ('casual', 'Casual / Hobby'),
        ('other', 'Other'),
    ]
    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    object_position = models.CharField(max_length=50, blank=True, default='center center')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.alt_text or f"Gallery Image {self.pk}"


class Greeting(models.Model):
    """Cycling greeting texts for the hero section."""
    text = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text


class NavLink(models.Model):
    label = models.CharField(max_length=50)
    anchor = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
