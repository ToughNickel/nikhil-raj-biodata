import json
from django.views.generic import TemplateView
from .models import (
    PersonalInfo, Education, Property, CareerEntry,
    FamilyMember, LineageNode, HeritageInfo, MoolCard,
    GalleryImage, Greeting, NavLink
)


class HomeView(TemplateView):
    template_name = 'biodata/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['personal'] = PersonalInfo.load()
        ctx['education_list'] = Education.objects.all()
        ctx['properties'] = Property.objects.all()
        ctx['career_entries'] = CareerEntry.objects.all()
        ctx['family_members'] = FamilyMember.objects.prefetch_related('tags').all()
        ctx['lineage_nodes'] = LineageNode.objects.all()
        ctx['heritage'] = HeritageInfo.objects.filter(pk=1).first()
        ctx['mool_cards'] = MoolCard.objects.all()
        ctx['gallery_images'] = GalleryImage.objects.all()
        ctx['greetings_json'] = json.dumps(
            list(Greeting.objects.values_list('text', flat=True))
        )
        ctx['nav_links'] = NavLink.objects.all()
        return ctx
