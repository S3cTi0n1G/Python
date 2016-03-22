a = float(raw_input("food1：your_food\n"))
b = float(raw_input("food2:_my_food\n"))
c = float(raw_input("How much you paid?\n"))

def price(a, b, c):
  print "food1 is %d yuan, food2 is %d yuan." % (a, b)
  print "I have paid %d Yuan" % c
  return a + b 

sum = price(a, b, c)
x = round(a * c / (a + b), 2)
y = c - x

print "You need pay me %d yuan" % x
