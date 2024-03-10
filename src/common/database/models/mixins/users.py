# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from src.common.constants import DEFAULT_LANGUAGE
from src.common.domain.enums.locales import Language
from src.common.presentation.utils.files import clean_static_url


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['']

    class Meta:
        abstract = True

    def clean(self):
        super().clean()


class AuthMixin(models.Model):
    email_address = models.ForeignKey(
        'EmailAddressORM',
        verbose_name='Email Address',
        db_index=True,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )
    phone_number = models.ForeignKey(
        'PhoneNumberORM',
        verbose_name='Phone Number',
        db_index=True,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        abstract = True

    @property
    def email_verified(self) -> bool:
        return self.email_address.is_verified if self.email_address else False

    @property
    def phone_number_verified(self) -> bool:
        return self.phone_number.is_verified if self.phone_number else False

    @property
    def display_phone_number(self) -> str:
        return self.phone_number.display_phone_number if self.phone_number else '---'

    @property
    def display_email_address(self) -> str:
        return self.email_address.email if self.email_address else '---'


def photos_folder(instance, filename):
    return '/'.join(['avatars', filename])


class ProfileMixin(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
        db_index=True,
        blank=True,
        null=True,
    )
    paternal_surname = models.CharField(
        verbose_name='Paternal Surname',
        max_length=150,
        db_index=True,
        blank=True,
        null=True,
    )
    maternal_surname = models.CharField(
        verbose_name='Maternal Surname',
        max_length=150,
        blank=True,
        null=True,
    )
    photo = ProcessedImageField(
        verbose_name='Photo',
        upload_to=photos_folder,
        processors=[ResizeToFill(512, 512)],
        format='PNG',
        options={'quality': 80},
        blank=True,
        null=True,
    )
    lang = models.CharField(
        verbose_name='Language',
        choices=Language.choices(),
        max_length=3,
        default=str(DEFAULT_LANGUAGE),
    )

    class Meta:
        abstract = True

    @property
    def last_name(self) -> str:
        value = ''
        if self.paternal_surname:
            value += self.paternal_surname
        if self.maternal_surname:
            value += f' {self.maternal_surname}'
        return value

    @property
    def display_name(self) -> str:
        display_name = ''
        if self.first_name:
            display_name += self.first_name
        if self.last_name:
            display_name += f' {self.last_name}'
        return display_name.strip()

    @property
    def photo_url(self):
        return clean_static_url(self.photo.url) if self.photo else None
