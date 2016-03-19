from sys import argv
from os.path import exists
script, from_file, to_file = argv
in_file = open(from_file)
indate = in_file.read()

out_file = open(to_file)
out_file.write(indate)

out_file = open(to_file)
print out_file.read()

out_file.close
in_file.close

