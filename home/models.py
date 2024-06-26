from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        # make the text block read only
        FieldPanel('subtitle', read_only=True),
        FieldPanel('body'),
    ]
