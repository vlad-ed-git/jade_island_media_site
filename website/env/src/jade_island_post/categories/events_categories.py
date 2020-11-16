from django.db import models
from django.utils.translation import gettext_lazy as _

class EVENT_CATEGORIES(models.TextChoices):
        EDUCATIONAL = 'ED', _('Educational or Inspirational')
        ENTERTAINMENT = 'EN', _('Entertainment')
        EXHIBITION = 'EX', _('Exhibition or Trade fair')
        CHARITY = 'CH', _('Charity or Fund Raising')
        COMPETITIONS = 'AC', _('Awards and Competitions')
        CONFERENCE = 'CO', _('Conference or Meeting')
        NETWORKING = 'NS', _('Networking Sessions')
        OTHER = 'O', _('Other')
        WEBINARS = 'W', _('WEBINARS')