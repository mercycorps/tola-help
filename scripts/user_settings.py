#!/usr/bin/python
"""
create_usersettings.py - Easy way to create helpdesk-specific settings for
users who don't yet have them.
"""
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

from helpdesk.models import UserSettings
from project.settings.base import DEFAULT_USER_SETTINGS


def run():
    for u in User.objects.all():
        try:
            s = UserSettings.objects.get(user=u)
        except UserSettings.DoesNotExist:
            s = UserSettings(user=u, settings=DEFAULT_USER_SETTINGS)
            s.save()