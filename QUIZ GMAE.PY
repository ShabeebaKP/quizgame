print ("WELCOME TO QUIZ GAME")

game= input("Do you want to play? ")

result =0
if game.lower() != "yes":
    print("Thank you, we will see next time")
    quit()

print("Okay! We will start ")

Question= input("1)Grand Central Terminal,park avenue ,New york is the world's ")
if Question .lower() == "largest railway station":
    print("Answer is correct,you scored 1 mark")
    result += 1
else:
    print("Answer is wrong")

Question= input("2)Hitler party which came into power in 1933 is known as")
if Question .lower() == "Nazi party".lower():
    print("Answer is correct,you scored 1 mark")
    result += 1
else:
    print("Answer is wrong")

Question= input("3)FFC stands for ")
if Question.lower() == "Film Finance Corporation".lower():
    print("Answer is correct,you scored 1 mark")
    result += 1
else:
    print("Answer is wrong")

Question= input("4)Epsom is the place associated with ")
if Question.lower()== "Horse racing".lower():
    print("Answer is correct,you scored 1 mark")
    result += 1
else:
    print("Answer is wrong")

Question= input("5)First Afghan War took place in ")
if Question.lower() == "1839":
    print("Answer is correct,you scored 1 mark")
    result += 1
else:
    print("Answer is wrong")

print("your result is: " +str(result) + " out of 5")
