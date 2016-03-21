from sys import argv
script, filename = argv

def print_all(f):
  print f.read()

def rewind(f):
  f.seek(0)

def print_line(line_number, f):
  print line_number, f.readline()
  
current_file = open (filename)

print "Whole line"
print_all(current_file)

rewind(current_file)

current_line = 1
print_line = (current_line,current_file)
current_line += 1
print_line = (current_line, current_file)
current_line += 1
print_line = (current_line, current_file )
