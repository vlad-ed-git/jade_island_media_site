from django.db import models
from django.utils.translation import gettext_lazy as _

class PLACE_CATEGORIES(models.TextChoices):
        DINING = 'D', _('Dining')
        PLAYING = 'P', _('Playing')
        LEARNING = 'L', _('Learning')
        HEALTH = 'H', _('Health')
        LOCALS = 'LO', _('Locals')
        STAYING = 'S', _('Staying')
        OTHER = 'O', _('Other')