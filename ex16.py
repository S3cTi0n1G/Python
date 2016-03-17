from sys import argv
script, filename = argv
print "I will destory this file,just like destory you."
print "hit ENTER to destroy %s" % filename
raw_input(shall we?)
target = open(filename, 'w')
target.truncate()
print "we done here"

print "Now,I will ask you for three lines"
line1 = raw_input("line1\n")
line2 = raw_input("line2\n")
line3 = raw_input("line3\n")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close

txt = open(filename)
print txt.read()
