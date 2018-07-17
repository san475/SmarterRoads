import urllib.request

uf = urllib.request.urlopen(https://smarterroads.org/api/spat?mode=GetLastSeconds&value=1&token=JNK41Hx3oE4vEmj7k5lTSrNTw6T4z3VnEy2OZP1LIawtIRJcwG2e2TPmLOjpWm5z)
html = uf.read()
