#Character Creation library
#Kale Berger
#October 1st, 2018
#############################
import time
import nameinput
import raceinput
import classinput

print ("""You are creating a character in a game. You can put your name, choice of race and gender, and your class
(for those who dont know that is what chooses your weapon and armour, typically).
Have fun with this character creation! 
""")

name = nameinput.whatisyourname()
time.sleep(5)
race = raceinput.characterrace()
time.sleep(5)
gender = raceinput.charactergender()
time.sleep(5)
classchoice = classinput.classselection()
time.sleep(10)
print("")
print("")
print ("Your name is", name, "you are a", gender, race, "and have chosen the class of", classchoice)
