from urllib.parse import urlencode, parse_qsl

import requests
from django.http import JsonResponse, HttpResponseForbidden
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView, OIDCAuthenticationRequestView, get_next_url, \
    OIDCLogoutView


def health(request):
    return JsonResponse({'result': 'OK'})


class CustomOIDCAuthCallbackView(OIDCAuthenticationCallbackView):

    def get(self, request):
        """Override to return the access_token for frontend authentication"""
        redirect = super().get(request)

        if redirect.url == self.failure_url:
            return HttpResponseForbidden()
        return JsonResponse({'access_token': self.request.session['oidc_access_token']})


class CustomOIDCAuthRequestView(OIDCAuthenticationRequestView):

    def get(self, request):
        """Override to return url and session id instead of redirect"""
        resp = super().get(request)
        url, query = resp.url.split('?')
        query = parse_qsl(query)
        for i in range(len(query)):
            if query[i][0] == 'redirect_uri':
                query[i] = ('redirect_uri', self.get_settings('OIDC_REDIRECT_URI'))
        redirect_url = '{url}?{query}'.format(url=url, query=urlencode(query))
        if not request.session.exists(request.session.session_key):
            request.session.create()
        return JsonResponse({'url': redirect_url, 'sessionid': request.session.session_key})


class CustomOIDCLogoutView(OIDCLogoutView):

    def revoke_token(self, request):
        token = request.headers['Authorization'].split(' ')[1]

        payload = {
            'client_id': self.get_settings('OIDC_RP_CLIENT_ID'),
            'client_secret': self.get_settings('OIDC_RP_CLIENT_SECRET'),
            'token': token,
            'token_type_hint': 'access_token',
        }

        response = requests.post(
            self.get_settings('OIDC_OP_REVOCATION_ENDPOINT'),
            data=payload,
            verify=self.get_settings('OIDC_VERIFY_SSL', True),
            timeout=self.get_settings('OIDC_TIMEOUT', None),
            proxies=self.get_settings('OIDC_PROXY', None))
        response.raise_for_status()
        print(response)

    def post(self, request):
        """Override to revoke token on logout"""
        super().post(request)
        self.revoke_token(request)
        return JsonResponse({'msg': 'Logged out.'})
