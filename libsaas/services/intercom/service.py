import json

from libsaas import http

from libsaas.filters import auth
from libsaas.services import base

from . import resource


class Intercom(base.Resource):
    """
    """
    def __init__(self, app_id, api_key):
        """
        Create a Intercom service.

        :var app_id: The APP identifier.
        :vartype app_id: str
        :var api_key: The API key.
        :vartype api_key: str
        """
        self.apiroot = 'https://api.intercom.io'

        self.add_filter(auth.BasicAuth(app_id, api_key))
        self.add_filter(self.use_json)
        self.add_filter(self.add_json_headers)

    def get_url(self):
        return self.apiroot

    def use_json(self, request):
        if request.method.upper() not in http.URLENCODE_METHODS:
            request.params = json.dumps(request.params)

    def add_json_headers(self, request):
        request.headers['Accept'] = 'application/json'
        request.headers['Content-Type'] = 'application/json'

    @base.resource(resource.Users)
    def users(self):
        """
        Return the resource corresponding to all users.
        """
        return resource.Users(self)

    @base.resource(resource.User)
    def user(self):
        """
        Return the resource corresponding to a single user.
        """
        return resource.User(self)

    @base.resource(resource.Impressions)
    def impressions(self):
        """
        Return the resource corresponding to all impressions.
        """
        return resource.Impressions(self)

    @base.resource(resource.MessageThreads)
    def message_threads(self):
        """
        Return the resource corresponding to all message threads.
        """
        return resource.MessageThreads(self)

    @base.resource(resource.MessageThread)
    def message_thread(self):
        """
        Return the resource corresponding to a single message thread.
        """
        return resource.MessageThread(self)

    @base.resource(resource.Counts)
    def counts(self):
        """
        Return the resource corresponding to all counts.
        """
        return resource.Counts(self)

    @base.resource(resource.Events)
    def events(self):
        """
        Return the resource corresponding to all events.
        """
        return resource.Events(self)

    @base.resource(resource.Companies)
    def companies(self):
        """
        Return the resource corresponding to all companies.
        """
        return resource.Companies(self)

    @base.resource(resource.Company)
    def company(self, id):
        """
        Return the resource corresponding to a single company.
        """
        return resource.Company(self, id)
