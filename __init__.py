__version__ = '0.1'

from .app import App
from .response import HTTPError, HTTPResponse

app = App()

COOKIES = app.COOKIES
FILES = app.FILES
GET = app.GET
POST = app.POST
delcookie = app.delcookie
error = app.error
install = app.install
notfound = app.notfound
plugins = app.plugins
redirect = app.redirect
request = app.request
route = app.route
run = app.run
setcookie = app.setcookie

from .static import sendfile, stream