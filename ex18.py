def fox1(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)
  fox1("witress", "me")

def fox2(arg1,arg2):
  print "%r, %r" % (arg1, arg2)
fox2("name", "it")
