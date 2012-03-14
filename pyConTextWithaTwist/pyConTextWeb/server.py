import sys
import os
import webbrowser

from twisted.application import internet, service
from twisted.web import server, resource, wsgi, static, client 
from twisted.python import threadpool
from twisted.internet import reactor, defer 

user_home = os.getenv('HOME')
pyConTextWebHome = os.path.join(user_home,"pyConTextWeb")
# make sure pyConText directory exists in user's home. If not create it
if( not os.path.exists( os.path.join(user_home,"pyConTextWeb")) ):
    os.mkdir( pyConTextWebHome )
PORT = 8095

sys.path.append(pyConTextWebHome)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.handlers.wsgi import WSGIHandler


class Root(resource.Resource):

    def __init__(self, wsgi_resource):
        resource.Resource.__init__(self)
        self.wsgi_resource = wsgi_resource

    def getChild(self, path, request):
        path0 = request.prepath.pop(0)
        request.postpath.insert(0, path0)
        return self.wsgi_resource

def wsgi_resource():
    pool = threadpool.ThreadPool()
    pool.start()
    reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
    wsgi_resource = wsgi.WSGIResource(reactor, pool, WSGIHandler())
    return wsgi_resource

application = service.Application('twisted-django')
wsgi_root = wsgi_resource()
root = Root(wsgi_root)

staticrsrc = static.File(os.path.join(pyConTextWebHome,"/pyConTextWeb/templates/media/"))
root.putChild("pyConTextWeb.media", staticrsrc)

main_site = server.Site(root)
internet.TCPServer(PORT, main_site).setServiceParent(application)
webbrowser.open_new_tab("http://localhost:"+str(PORT))#+"/pyConTextKit/accounts/login/")
#webbrowser.open_new_tab("http://www.yahoo.com")
