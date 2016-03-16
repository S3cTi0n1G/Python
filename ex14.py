from sys impory argv
script, name = argv
prompt = "> "

print "Hi %s, I am %s,I'd ask you some qustion" % (script, name)
print "What kind of color do you like,%s" % name
color = raw_input(prompt) 

print "What pet do you want,%s" % name
pet = raw_input(prompt)

Print """
So %s, You have finish my qustion.
Your like %s. me too
Your want %s. good
here is you answer
Good bye,I'm %s
""" % (name, color, pet, script)
