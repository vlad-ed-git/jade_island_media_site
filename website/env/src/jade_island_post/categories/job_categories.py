from django.db import models
from django.utils.translation import gettext_lazy as _

class JOB_CATEGORIES(models.TextChoices):
    TEACHING_ENGLISH = 'ET', _('Teaching English')
    TEACHING_OTHER = 'NET', _('Teaching Other Subjects')
    NON_TEACHING = 'NT', _('Non Teaching')

class JOB_TYPE(models.TextChoices):
    FULL_TIME = 'FT', _('Full Time')
    PART_TIME = 'PT', _('Part Time')
    FREELANCE = 'FR', _('Contract or Freelance')
    INTERNSHIP = 'INT', _('Paid Internship')
    VOLUNTEER = 'VT', _('Volunteer or Unpaid Internship')