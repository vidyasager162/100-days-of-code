#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

toss = random.randint(0, 1)
if toss == 0:
    print("Tails")
else:
    print("Heads")