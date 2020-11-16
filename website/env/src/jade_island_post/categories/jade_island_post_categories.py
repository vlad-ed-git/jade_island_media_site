from django.db import models
from django.utils.translation import gettext_lazy as _

class JADE_ISLAND_POST_CATEGORIES(models.TextChoices):
        EVENT = 'E', _('Event')
        PLACE ='P', _('Place')
        TIP = 'T', _('Tip')
        SHARED_MOMENT = 'SM', _('Shared Moment')
        SALE = 'S', _('Sale')
        JOB = 'J', _('Job')
        ADVERT = 'AD', _('Advert')
        UNCATEGORIZED = 'UN', _('UN Categorized')