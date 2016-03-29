print "Your are the Lone Ranger,just down to the moon,find a gold mine,what will you do next"
print "1. I take all of the gold"
print "2. I take the diamond"

choice = raw_input(">")

if choice == "1":
    print "You find a hulk, dress like daydream in the middle of two way,what you do next?"
    print "1. run to the left way"
    print "2. walk to the right way"
    print "3. kiss the hulk, I am black wisdom"
    
    hulk = raw_input(">")
    
    if hulk == "1":
        print "Hulk catcted you, you died."
    elif hulk == "2":
        print "Hulk, fall into sleeping,you alive."
    else:
        print "Hulk doesn't reconize you, you died."
    
elif choice == "2":
    print "Right now, you put the diamond into you pocket,and walk to end of the way, you stand at the pondshore,what will you do?"
    print "1. Dive into the water"
    print "2. walk back"
    
    diamond = raw_input(">")
    
    if diamond == "1":
        print "Finally, you find a exit, lead you to amazon river, You Alive"
    else: 
        continue #syntax error
else:
    print "You wake up! and turn off the radio."
