from __future__ import print_function
from twisted.internet import reactor
from twisted.web import server
import pyepanet2 as epanet
import threading

from jsonrpc.server import ServerEvents, JSON_RPC

class EpanetServer(ServerEvents):
    timer = threading.Timer(5.0, reactor.stop)
    def log(self, responses, txrequest, error):
        print(txrequest.code, end=' ')
        if isinstance(responses, list):
            for response in responses:
                msg = self._get_msg(response)
                print(txrequest, msg)
            else:
                msg = self._get_msg(responses)
                print(txrequest, msg)
    
    def findmethod(self, method,a,b):
        methods = set(self.__class__.__dict__.keys())
        if method in methods:
            return getattr(self, method)
        else:
            return None
            
    def _get_msg(self, response):
        print('response', repr(response))
        return ' '.join(str(x) for x in [response.id, response.result or response.error])
        
    def getmethods(self):
        return self.__class__.__dict__.keys()
        
    def ENgeterror(self,val):
        errstr = "                                                               "
        ret = epanet.ENgeterror(int(val),errstr,len(errstr))
        return [ret,str(errstr)]
        
    def shutdown(self):
        self.timer.start()
        return 1

root = JSON_RPC().customize(EpanetServer)
site = server.Site(root)

PORT = 8007
print('Listening on port %d...' % PORT)
reactor.listenTCP(PORT, site)
reactor.run()
print('Server shutdown by client')

