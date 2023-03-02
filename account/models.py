from django.core.mail import send_mail
from django.utils import timezone

from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **other_fields):
        """crea un utente normale (Acquirente)"""
        if not email:
            raise ValueError('Gli utenti devono avere una mail')
        user = self.model(
            email=self.normalize_email(email),
            username=username, **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **other_fields):
        """
        crea un super-utente (admin)
        """

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('il SuperUser deve essere assegnato a is_staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('il Superuser deve essere assegnato a is_superuser')

        user = self.create_user(
            email,
            username=username,
            password=password,
            **other_fields
        )

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), max_length=100, unique=True)

    nome = models.CharField(max_length=50, blank=True)
    cognome = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    citta = models.CharField(max_length=50, blank=True)
    indirizzo = models.CharField(max_length=100, blank=True)
    codice_postale = models.CharField(max_length=5, blank=True)
    punti = models.PositiveIntegerField(default=0, editable=False)

    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    object = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nome", "cognome", "telefono", "citta", "indirizzo", "codice_postale"]

    class Meta:
        verbose_name_plural = "Utenti"


    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'Negozio_online_Balugani@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return str(self.username)
