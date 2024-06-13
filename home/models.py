from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
