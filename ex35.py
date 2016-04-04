# a axe mystery
from sys import exit
def choice_axe():
    print "your axe drop into the river"
    print "You come down to the rivershore"
    print "There is a little boat"
    print "A old man show up from the water"
    print "He hand a gold axe, is this belong to you?"
    your_choice = False
    
    while True:
        gold_choice = raw_input("> ")
    
        if gold_choice.lower() ==  'yes':
            print "Young man,take your axe"
            print "The old man disappeared"
            why("You take the gold axe, and go back to work")
        elif gold_choice.lower() == 'no':
            print  "He dive into the river a moment, hand a sliver axe, is this belong to you?"
        
            sliver_choice = raw_input("> ")
        
            if sliver_choice.lower() == 'yes':
                print "Young man,take your axe"
                print "The old man disappeared"
                why("You take the sliver axe, and go back to work")
            elif sliver_choice == 'no':
                print "He dive into the river a moment again, He hand a steel axe, is this belong to you?"
            
                steel_choice = raw_input("> ")
            
                if steel_choice.lower() ==  'yes':
                    print "You are honest boy, I will give gold axe,sliver axe and steel axe to you"
                    axe()
                elif steel_choice == 'no':
                    print "Your axe not in here, the old man disappeared"
                    exit(0)
                else:
                    print "I'm too old to understand what you saying"
            else:
                print "I'm too old to understand what you saying"
        else:
            print "I'm too old too understand what you saying"
        
def axe(): ＃最后一步
    print "Do you want take other two axe?"
    
    take_axe = raw_input("> ")
    
    if take_axe.lower() == 'yes':
        why("You have take three axe,and go to work!")
    elif take_axe.lower() == 'no':
        print("You only take your axe")
        why("you meet alibaba on your way to work,and he take you to the Cathlhu.")
        print("ENd")
        
def why(gg): #why 函数，用于输出结果。
    print gg, "Good Job"
    exit(0)

def start(): ＃开始，设置选择
    print "You are go to work shop"
    print "You have too cross a river,there are two bridge you can cross the river"
    print "the harrod bridge is far but maybe blocked,the woodstock bridge is fast but more dangerous"
    print "which bridge do you choice?"
    
    bridge = raw_input("> ")
    
    if bridge == 'harrod':
        print "Your are go to harrod"
        why("Your arriver your work shop")
    elif bridge == 'woodstock':
        choice_axe()
        
start()
        
        
