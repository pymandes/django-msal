"""Main module."""

import logging
import msal
import uuid
from django_msal.conf import settings
from django.shortcuts import render, redirect, reverse


logger = logging.getLogger(__name__)


class Connection(object):

    def __init__(self, connection):

        self._connection = connection


def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        settings.AZURE_CLIENT_ID, authority=authority or settings.MICROSOFT_AUTHORITY,
        client_credential=settings.AZURE_CLIENT_SECRET, token_cache=cache)


def _build_auth_url(request, authority=None, scopes=None, state=None):
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=request.build_absolute_uri(reverse(settings.LOGIN_REDIRECT_PATH)))
