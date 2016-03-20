from sys import argv
from os.path import exists
script, ff, tf = argv
in_date = open(ff)
to = in_date.read()

print len(to)

print "Does tf exists? %s " % exists(tf)

out_date = open(tf, 'w')
out_date.write(to)
print "done"

out_date = open(tf)
print out_date.read()

out_date.close
in_date.close
