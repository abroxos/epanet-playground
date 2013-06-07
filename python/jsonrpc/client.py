from jsonrpc import proxy

epanet = proxy.JSONRPCProxy('http://127.0.0.1:8007', '/jsonrpc')

print epanet.ENgeterror(102)[1]
print epanet.shutdown()