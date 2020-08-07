from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from app import settings


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username_regex = RegexValidator(regex=r'[a-z]{5,15}', message='Username must be all lower case & 5-15 characters')
    username = models.CharField(validators=[username_regex, ], max_length=15, unique=True, blank=False, null=False)

    USERNAME_FIELD = 'username'


class Session(models.Model):
    """User created sessions contain Time Blocks customers can book with the user"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user'
    )

    name = models.CharField(max_length=1028, blank=True, default='')
    details = models.CharField(max_length=6000, blank=True, default='')
    pricing = models.CharField(max_length=1028, blank=True, default='')


class TimeBlock(models.Model):
    """The block of time that a customer can book for a given session"""

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='session'
    )

    start = models.DateTimeField(blank=False, null=False)
    end = models.DateTimeField(blank=False, null=False)

    # TODO: override string


class BookingRequest(models.Model):
    """customer request to claim a time_block"""

    time_block = models.ForeignKey(
        TimeBlock,
        on_delete=models.CASCADE,
        related_name='requested_time_block'
    )

    first_name = models.CharField(max_length=15, blank=False, null=False)
    last_name = models.CharField(max_length=15, blank=False, null=False)

    contact_email = models.EmailField(blank=False, null=False)
    contact_phone = models.IntegerField(null=True, blank=True)

    message = models.CharField(max_length=6000, blank=True, default='')


class Booking(models.Model):
    """User accepted booking for a customer"""

    time_block = models.ForeignKey(
        TimeBlock,
        on_delete=models.CASCADE,
        related_name='time_block'
    )

    first_name = models.CharField(max_length=15, blank=False, null=False)
    last_name = models.CharField(max_length=15, blank=False, null=False)

    contact_email = models.EmailField(blank=False, null=False)
    contact_phone = models.IntegerField(null=True, blank=True)

    STATUS_CHOICES = (
        ('booked', 'booked'),
        ('removed', 'removed'),
        ('declined', 'declined'),
        ('confirmed', 'confirmed'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'pending'),
        ('paid', 'paid'),
        ('deposit-received', 'deposit-received'),
        ('declined', 'declined')
    )
