from functools import partial
import requests

class API(object):
    """
    The toplevel object, and the "entry-point" into the client API.
    Subclass this to develop an application for a particular REST API.
    """
    def __init__(self, *args, **kwargs):
        self.session = requests.Session()

    def __getattr__(self, key):
        return IncompleteRequest(self.base_url, self.session).__getattr__(key)

    __getitem__ = __getattr__

    def __repr__(self):
        return IncompleteRequest(self.base_url, self.session).__repr__()

    def getheaders(self):
        return self.client.headers


class IncompleteRequest(object):
    """
    IncompleteRequests are partially-built HTTP requests.
    They can be built via an HTTP-idiomatic notation,
    or via "normal" method calls.
    """
    HTTP_METHODS = ['head', 'get', 'post', 'put', 'patch', 'delete', 'request']

    def __init__(self, base_url, session):
        self.url = base_url
        self.session = session

    def __getattr__(self, key):
        if key.lower() in self.HTTP_METHODS:
            mfun = getattr(self.session, key)
            return partial(mfun, url=self.url)
        elif hasattr(self.session, key):
            return getattr(self.session, key)

        return self.__getitem__(key)

    def __getitem__(self, key):
        new_url = self.url + '/' + str(key)
        return self.__class__(new_url, self.session)

    def __str__(self):
        return self.url

    def __repr__(self):
        return '<%s %s>' % (self.__class__, self.url)
