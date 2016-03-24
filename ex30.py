a = float(raw_input("lunch\n"))
b = float(raw_input("dinner\n"))
c = float(raw_input("breakfast\n"))

def food(lunch, dinner, breakfast):
    return lunch + dinner + breakfast
sum = food(a, b, c)

if  sum > 50:
    print "You need diet"
elif sum > 30 and sum < 50:
    print "A apple a day,keep kinney away."
else:
    print "卤,wash your hand and eat something"
