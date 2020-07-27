"""
Settings
"""

from django.conf import settings


class LazySetting(object):

    def __init__(self, name, default=None):
        self.name = name
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return getattr(obj._settings, self.name, self.default)


class LazySettings(object):

    """
    A proxy to ldap-specific django settings.
    Settings are resolved at runtime, allowing tests
    to change settings at runtime.
    """

    def __init__(self, settings):
        self._settings = settings

    LOGIN_URL_NAME = LazySetting(
        name="LOGIN_URL_NAME",
        default="login",
    )

    LOGOUT_URL_NAME = LazySetting(
        name="LOGOUT_URL_NAME",
        default="logout",
    )

    LOGIN_EXEMPT_URLS = LazySetting(
        name="LOGIN_EXEMPT_URLS",
        default=['signup'],
    )

    LOGIN_REDIRECT_URL = LazySetting(
        name="LOGIN_REDIRECT_URL",
        default="home",
    )

    LOGOUT_REDIRECT_URL = LazySetting(
        name="LOGOUT_REDIRECT_URL",
        default="index",
    )

    AZURE_CLIENT_ID = LazySetting(
        name="CLIENT_ID",
        default="",
    )

    AZURE_CLIENT_SECRET = LazySetting(
        name="CLIENT_SECRET",
        default="",
    )

    MICROSOFT_AUTHORITY = LazySetting(
        name="AUTHORITY",
        default="",
    )

    LOGIN_REDIRECT_PATH = LazySetting(
        name="REDIRECT_PATH",
        default="/authorized",
    )

    AZURE_AD_SCOPE = LazySetting(
        name="SCOPE",
        default=["User.ReadBasic.All"],
    )

    AZURE_AD_SESSION_TYPE = LazySetting(
        name="SESSION_TYPE",
        default="filesystem",
    )


settings = LazySettings(settings)