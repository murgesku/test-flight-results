from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed


class DummyUser(AnonymousUser):
    """
    Dummy user for dummy authentication
    """
    is_active = True

    @property
    def is_authenticated(self):
        return True


class DummyTokenAuthentication(BaseAuthentication):
    """
    Dummy authentication using static token
    """
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'bearer':
            return None

        if len(auth) != 2:
            msg = _("Invalid bearer header.")
            raise AuthenticationFailed(msg)
        
        if auth[1] != settings.DUMMY_AUTH_TOKEN:
            return None
        
        return (DummyUser(), None)
    
    def authenticate_header(self, request):
        return 'Bearer realm="api"'
