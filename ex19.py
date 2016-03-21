def money(cash, credit_card):
  print "You have %d dolloars cash,and %d credit_card" % (cash, credit_card)
  
print "way 1"
money(1000, 4)

print "way 2"
amount = 1000
icbc = 4
money(amount, icbc)

print "way 3" 
money(500 + 500, 2**2)

print "way 4"
money(amount - icbc, icbc + 1)

