# Project: Guess The Number
# Author : TousifNehal

#importing modules

import random
import os

# Files Path For Storing Scores And High Scores
scorefile = "score.txt"
hiscorefile = "hiscore.txt"

# If ScoreFile Exists Write The Value To 0
if os.path.exists(scorefile) == True :
    with open(scorefile, "w") as y:
        y.write(str(0))

# Guess The Number Game Funcion
      
def game():
    # If File Don't Exist Create & Replace The Value With 0
    if os.path.exists(scorefile) == False :
                with open(scorefile, "w") as x:
                    x.write(str(0))
    if os.path.exists(hiscorefile) == False :
                with open(hiscorefile, "w") as z:
                    z.write(str(0))
                    
    # Generating The Number And Confirming It
    number = random.randint(1,100)
    print("✅ Number Generated Successfully")
    
    # Hint For The Generated Number
    x = random.randint(1,20)
    if x == number :
        x = random.randint(1,20)
    if x > number : 
        x = random.randint(1,20)
    hint1 = number - x
    hint2 = number + x

    if number > hint1 or number == hint1:
        hint1 = random.randint(1, 50)

    elif number < hint2 or number == hint2:
        hint2 = random.randint(51, 100)


    if hint1 < number < hint2:
        print(f"💡 Hint: The number is higher than {hint1} and lower than {hint2}.")

    # Difficulty Function For Guesses
    
    difficulty = int(input("⚡ Difficulty: Choose \n\t1 for Easy (5-10 guesses) \n\t2 for Medium (3-6 guesses) \n\t3 for hard (2-4 Guesses) \n\t4 for extreme hard (1-2) guesses"))
    
    # Easter Egg (5,6) randomly generated. If Matches It Will Reveal The Number For You :( Don't Try To Cheat 
    egg = random.randint(5,6)
    if difficulty == egg :
        guess = random.randint(1,10)
        print("😲 Oh No! You Knew The Easter Egg. Cheat Mode enabled")
        print("👀 The number Is", str(number))
    elif difficulty == 1 :
        guess = random.randint(5,10)
    elif difficulty == 2:
        guess = random.randint(3,6)
    elif difficulty == 3:
        guess = random.randint(2,4)
    elif difficulty == 4:
        guess = random.randint(1,2)
    else :
        guess = random.randint(1,10)
        print(f"⚠ You Typed {difficulty} that was out of choice, choosing random guesses ")
        
    # Declaring How Many gueeses he have
    print(f"⚡ You Have {guess} guesses")

    # Until The Guess Equals To Zero The Guessing Function will run                   
    while guess != 0 :
        # Asking User What he guessed?
            userg = int(input("❓ Enter Your Guess : ")) 
        # If UserGuess == Number Function
            if userg == number:
                # Reading Previous Score
                with open(scorefile, "r") as scoreread:
                    data = scoreread.readline()
                    data = int(data)
                # If Score = 0 Than add 1 points
                if data == 0:
                    with open(scorefile, "w") as scorewrite:
                        score = data + 1
                        scorewrite.write(str(score))
                        # print(score)
                # If It's Bigger Than Zero Read & Add 1 With that previous score
                elif data > 0:
                    with open(scorefile, "r") as scoreread:
                        data = scoreread.readline()
                        data = int(data)
                    with open(scorefile, "w") as scorewrite:
                        score = data + 1 
                        scorewrite.write(str(score))
                # If User guessed Correctly Congrates Him
                print(f"🎉 Congrats. The Number Was Really {number}, You Gained 1 Points. Your Score : {score}")
                break
            else:
                # For Wrong guesses
                guess = guess - 1
                print(f"You have {guess} guesses left")  
                # If Guess = 1 It will reveal lucky hint if you have luck
                if guess == 1 :
                    value = random.randint(0,7)
                    h1 = number - value
                    h2 = number + value
                    lucky = random.randint(0,1)
                    if lucky == 0:
                          pass
                    elif lucky == 1:
                        print(f"❗ LUCKY HINT : {h1} < number < {h2}") 
                # If attempts end it will substract 1 score from previous and save
                if guess == 0:  
                    with open(scorefile, "r") as scoreread:
                        data = scoreread.readline()
                        data = int(data)
                        # If Score = 0 it will not substract
                    if data == 0:
                        print("You Have 0 Score 😢")
                        # If Not It Will substract 1 from score
                    elif data > 0:
                        with open(scorefile, "r") as scoreread:
                            data = scoreread.readline()
                            data = int(data)
                        with open(scorefile, "w") as scorewrite:
                            score = data - 1 
                            scorewrite.write(str(score))
                    # Ensuring the user that he ran out of guesses
                    print(f"😢 You're out of guesses! The correct number was: {number}, You lost 1 Points, Your Score : {score}")
                    break
   # If He Wants To Play Again or not function
    def again():
        x = int(input("""\n\nType: \n\t➰ 1 for Playing again\n\t❌ 2 For Exit \n"""))
        return x
  
    choice = again()
    choice
    # if yes than running the whole script again
    if choice == 1 :
        game()
    # If not than checking how many score he have and is it higher than the previous high score
    else:
        with open(scorefile, "r") as scoreread:
            data = scoreread.readline()
            data = int(data)
            #here Data Refers To Scorefile Value
        with open(hiscorefile, "r") as hsread:
            hdata = hsread.readline()
            hdata = int(hdata)
            #here data refers to hi score value
        # If not high ignore
        if hdata > data:
            print(f"➡ Your Current Score is {data}, High Score is {hdata}")
        # If High Replace the data
        elif hdata < data :
            # Ensuring the user that he scored higher than the past
            print("❗ HIGH SCORE ❗")
            print(f"🎉 Your Previous Score was {hdata}, New High Score = {data}")
            with open(hiscorefile, "w") as writeHiscore:
                writeHiscore.write(str(data))
        #Exiting After That        
        print("✅ Thank You For Playing With Me. Exiting Now ")
        exit()

# Running The Guess The Number Game Function

game()
 
 
# Thank You For Using This Script
# Created on 03-03-2024
# Author -> TousifNehal
# Feel free to contract
# Open A Issue if any error occurs           

