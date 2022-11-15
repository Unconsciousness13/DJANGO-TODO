from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy



# CUSTOM USER




MIN_NAMES_LENGTH_VALIDATOR = 2


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('Email required !'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    user_name = models.CharField(max_length=80, unique=True, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    first_name = models.CharField(max_length=80, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    last_name = models.CharField(max_length=80, validators=(
        MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),))
    start_time = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name

    def clean(self):
        invalid_chars_first_name = [ch for ch in self.first_name if not ch.isalnum() or not ch.isalpha()]
        invalid_chars_last_name = [ch for ch in self.last_name if not ch.isalnum() or not ch.isalpha()]
        invalid_chars_username = [ch for ch in self.user_name if not ch.isalnum() or ch == '_' or ch == '-']
        if invalid_chars_first_name:
            raise ValidationError(f'The name must contain only letters but contain: {invalid_chars_first_name}')
        if invalid_chars_last_name:
            raise ValidationError(
                f'The last name  must contain only letters but contain: {invalid_chars_last_name}')
        if invalid_chars_username:
            raise ValidationError(
                f'Username must contain only letters or numbers: {invalid_chars_username}')


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=555)
    task_date = models.DateField(auto_now=False, blank=False)
    task_hour = models.TimeField(auto_now=False, blank=False)
    created_at = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    