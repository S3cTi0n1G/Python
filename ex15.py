from sys import argv
script, filename = argv

txt = open(filename)
print "Here is your %s" % filename
print txt.read()

print "Input your filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
