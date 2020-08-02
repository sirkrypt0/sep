from urllib.parse import parse_qsl, urlencode

from django.http import JsonResponse
from mozilla_django_oidc.middleware import SessionRefresh


class CustomSessionRefresh(SessionRefresh):

    def process_request(self, request):
        """Override to set the frontend redirect uri"""
        response = super().process_request(request)
        if response is None:
            return
        if request.is_ajax():
            url, query = response['refresh_url'].split('?')
            query = parse_qsl(query)
            for i in range(len(query)):
                if query[i][0] == 'redirect_uri':
                    query[i] = ('redirect_uri', self.get_settings('OIDC_REDIRECT_URI', ''))
            redirect_url = '{url}?{query}'.format(url=url, query=urlencode(query))
            response = JsonResponse({'refresh_url': redirect_url}, status=403)
        return response
