from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    def get_token(self, payload):
        """Override to set the frontend redirect uri"""
        payload['redirect_uri'] = self.get_settings('OIDC_REDIRECT_URI')
        return super().get_token(payload)
