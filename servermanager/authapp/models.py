from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class UserProfile(AbstractUser):
    GENDER_MANE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHICES = (
        (GENDER_MANE, _('male')),
        (GENDER_FEMALE, _('female')),
    )

    date_birth = models.DateField(_('birth date'), null=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$',
    #                              message="Номер телефона необходимо вводить в формате: '+799999999'. Допускается до "
    #                                      "15 цифр.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHICES, blank=True)
