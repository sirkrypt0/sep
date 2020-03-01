from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# see https://mozilla-django-oidc.readthedocs.io/en/stable/
class OpenIDAuthenticationBackend(OIDCAuthenticationBackend):
    def filter_users_by_claims(self, claims):
        email = claims.get('email')
        if not email:
            return []

        try:
            return [self.UserModel.objects.get(email=email)]
        except Profile.DoesNotExist:
            return []

    def create_user(self, claims):
        user = self.UserModel.objects.create(
            username=generate_username_from_email(claims.get('email')),
            email=claims.get('email'),
            first_name=claims.get('given_name', ''),
            last_name=claims.get('family_name', ''),
        )
        return user

    @staticmethod
    def update_user(user, claims):
        user.email = claims.get('email')
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()
        return user


def generate_username_from_email(email):
    return unicodedata.normalize('NFKC', email).split('@')[0].lower()