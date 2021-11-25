from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


class Organization(models.Model):
    '''
    There are many organization that publish their's KDWS services.
    '''
    name = models.CharField(_('title'), max_length=100)
    url = models.URLField(_('url'), max_length=200)
    description = models.TextField(_('description'))
    logo = models.FileField(_('url'), upload_to='uploads/', default='default_logo.png')
    

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organization_detail", kwargs={"pk": self.pk})

