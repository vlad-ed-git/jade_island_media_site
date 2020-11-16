from django.db import models
from django.utils.translation import gettext_lazy as _

class SALE_CATEGORIES(models.TextChoices):
        CRAFTS = 'AC', _('Arts & Crafts')
        CHILDREN = 'BC', _('Baby & Children')
        CLOTHING = 'CA', _('Clothing & Apparel')
        ELECTRONICS = 'EI', _('Electronics')
        HEALTH = 'HS', _('Health & Sports')
        HOME = 'HF', _('Home & Furniture')
        PETS = 'PA', _('Pets & Animals')
        SERVICES = 'SE', _('Services')
        VEHICLES = 'V', _('Vehicles')
        OTHER = 'O', _('Other')