import time



print("Hello my name is yamy the bunny!")
print("Do you want to make your own story?\n[YES]\n[NO]")
i = input("enter answer here\n")
if i.lower().strip() == "yes":
    print("Ready...!")
    time.sleep(1)
    print("Set....!")
    time.sleep(1)
    print("GO!!!!!!!!")
    i = input("Ok so you're in a forest and you meet a bear what do you do. Do you\n[FIGHT IT]\n[RUN]")
    if i.lower().strip() == "fight it":
        print("GAME OVER.... You got killed by the bear because you didn't have a weapon")
    elif i.lower().strip() == "run":
        print("Good job.... you run as fast as you can.")
        time.sleep(2)
        print('....YOU SURVIVE!!!.')
        i = input("blah blah blah hello my name is ava i like unicors do you like unicoorn if you dont i will  come to your house and ....KILL YOu")



if  i.lower().strip() == "no":
    print("okay! BUHHHH BYE")
else:
    print("Please enter a vaild selection")


















