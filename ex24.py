def beatles():
  john = "john", "Lennon"
  paul = "paul", "McCartney"
  george = "george", "Harrison"
  ringo = "ringo", "Starr"
  return john, paul, george, ringo
  
Lennon, McCartney, Harrison, Starr = beatles()

print Lennon, McCartney, Harrison, Starr
print "member 1 name is %s\nmember 2 name is %s\nmember 3 name is %s\nmember 4 name is %s\n" % beatles()
