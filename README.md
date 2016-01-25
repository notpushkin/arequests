# Agnostic Requests

Heavily inspired by [agithub](https://github.com/jaredhobbs/agithub). Powered by [Requests](http://docs.python-requests.org/).

## Usage

Let's make a GitHub API client.

```py
from arequests import API

class Github(API):
    base_url = "https://api.github.com"

    def __init__(self, auth):
        super(Github, self).__init__()
        # self.session is a requests.Session [1] object here
        self.session.auth = auth
        self.session.headers.update({
            'Accept': 'application/vnd.github.v3+json'
        })
```

\[1]: http://docs.python-requests.org/en/latest/user/advanced/#session-objects

```py
>>> g = Github(("iamale", "f2a3ec8e7901edef12b6ce9bce437780b69a5cd3"))
>>> g.users["mdo"].get().json()
{
    'name': 'Mark Otto',
    'login': 'mdo',
    'blog': 'http://mdo.fm',
    'followers': 9388,
    'hireable': True,
    'site_admin': True,
    ...
}
>>> g.issues.get(params={"filter": "mentioned"}).json()
[{
    'id': 12345678,
    'repository': { ... },
    'number': 9,
    'state': 'open',
    'title': 'Propose a new schema',
    'body': ...,
    'comments': 6,
    ...
}, ...]
```
