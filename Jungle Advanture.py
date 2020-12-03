import os
import sys
import time
import playsound 
import speech_recognition as sr 
from gtts import gTTS 

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp4"
    tts.save(filename)
    playsound.playsound(filename)
    
def close():
    speak("Bye! Have a nice day, you are an awsome kid")
    sys.exit()

def win():

    print("Congratulations! You won. Do you want to play again?")
    speak("Congratulations! You won. Do you want to play again?")
    yn=input("Select 'YES' or 'NO': ")
    if yn=="Yes" or yn=="yes" or yn == "YES":
        print("")
        game()    
    else:
        sys.exit()
    
def lose():
    print("Sorry! You lose. Game Over. Do you want to play again?")
    speak("Sorry! You lose. Game Over. Do you want to play again?")
    yn=input("Select 'YES' or 'NO': ")
    if yn=="Yes" or yn=="yes" or yn == "YES":
        print("")
        game()
    else:
        sys.exit()
        
def wrongInput():
    print("Wrong Input! Please Type Carefully.")
    speak("Please read instructions and type correctly")
    game()

    
def game():
    print("")
    
    speak("Choose one.  Left. or. Right?.")
    left_or_right = input("Type 'LEFT' or 'RIGHT' : ")
    if left_or_right == "LEFT" or left_or_right == "Left" or left_or_right == "left":
          speak("Great choice! You have 10 points. You are now towards the African Jungle. ")
          print("Current Point= 10")
          print("")
          speak("You need 20 Points to win the game.")
          speak("Choose one. (A) Start walking. (B) Search for a Bicycle?")      
          A_or_B= input("Type 'A' or 'B': ")

          if A_or_B == "A" or A_or_B == "a":
              speak("Great! You won five points, because you are brave enough to walk.")
              print("Current Point= 15")
              print("")
              speak("After Walking for couple of hours you reached a River side. Choose one. (A) Make a boat. And follow the River with the Boat. (B) Continue walking.")
              A_or_B= input("Type 'A' or 'B': ")
              
              if A_or_B == "A" or A_or_B == "a":
                  speak("By following the river, you have reached at the End of the Jungle and got five more points. ")
                  print("Current Point= 20")
                  print("")
                  win()
                    
              elif A_or_B == "B" or A_or_B == "b":
                   speak("As you are walking for so long, you get tired and lost five points.")
                   print("Current Point= 10")
                   print("")
                   speak("Choose one: (A). Take a nap. (B). Climb a tree to have a birds eye view.")
                   A_or_B= input("Type 'A' or 'B': ")
                   if A_or_B == "A" or A_or_B == "a":
                       speak("You were eaten by a King Kobra while sleeping. And lose your last 10 points")
                       print("Current Point= 0")
                       print("")
                       lose()
                       
                   elif A_or_B == "B" or A_or_B == "b":
                       speak("You fall from the tree and lost your last 10 points.")
                       
                       print("Current Point= 0")
                       print("")
                       lose()

                   else:
                       wrongInput()
              else:
                  wrongInput()
                   
                   
                   

          elif A_or_B == "B" or A_or_B == "b":
              speak("Searching for a Bicycle in a forest is not a smart idea. You lose 5 Points.")
              print("Current Point= 5")
              print("")
              speak("Choose one. (A). Take some rest. (B). Start walking now.")
              A_or_B= input("Type 'A' or 'B': ")
              if A_or_B == "A" or A_or_B == "a":
                       speak("You are too lazy. You lost your last 5 points. ")
                       print("Current Point= 0")
                       print("")
                       lose()
              elif A_or_B == "B" or A_or_B == "b":
                  speak("Smart move.You got 5 Points. ")
              
                  print("Current Point= 10")
                  print("")
                  speak("Now you see a River in front of you. Choose one. (A) Make a boat and cross the river, using it. (B) Just swim acress the river.")
                  A_or_B= input("Type 'A' or 'B': ")
                  if A_or_B == "A" or A_or_B == "a":
                     speak("Great choice. You have crossed the river wisely and reached at the end of the Jungle. As a result, you won 10 more points. ")
                     print("Current Point= 20")
                     print("")
                     win()
                  elif A_or_B == "B" or A_or_B == "b":
                     speak("Swimming in a Jungle river is not a wise decision. You were eaten by a Crocodile and lost your last 10 points.  ")
                     print("Current Point= 0")
                     print("")
                     lose()
                  else:
                      wrongInput()
              else:
                  wrongInput()
                     
          else:
              wrongInput()
          
    elif left_or_right == "RIGHT" or left_or_right == "Right" or left_or_right == "right":
          speak("Great choice! You have 10 points. You are now towards the Asian Jungle. ")
          print("Current Point= 10")
          print("")
          speak("You need 20 Points to win the game.")
          speak("Choose one. (A) Search for a hidden map of the jungle. (B) Climb on a Tree to look around, and have an idea, about your goal path.")      
          A_or_B= input("Type 'A' or 'B': ")

          if A_or_B == "A" or A_or_B == "a":
              speak("You searched for the map till evening but found nothing. You have wasted your time and lose 5 points. ")
              print("Current Point= 5")
              print("")
              speak("Choose one. A. Get some sleep. (B) Start climbing the tree now.")
              A_or_B= input("Type 'A' or 'B': ")
              
              if A_or_B == "A" or A_or_B == "a":
                  speak("While sleeping you were eaten by a Lion. You lost your last five points.")
                  print("Current Point= 0")
                  print("")
                  lose()
                    
              elif A_or_B == "B" or A_or_B == "b":
                   speak("You fall from the tree, because, it was too dark in the jungle. and lost your last five points. ")
                   print("Current Point= 0")
                   print("")
                   lose()
              else:
                  wrongInput()
                   
                   

          elif A_or_B == "B" or A_or_B == "b":
              speak("Great decision. Now, you have a clear idea, about your goal path. And you got 5 more points")
              print("Current Point= 15")
              print("")
              speak("Choose one. (A) Go through the found path. (B) Explore other ways to find something interesting in the Jungle!")
              A_or_B= input("Type 'A' or 'B': ")
              if A_or_B == "A" or A_or_B == "a":
                       speak("You got five more points. and reached at the end of the Jungle.  ")
                       print("Current Point= 20")
                       print("")
                       win()
              elif A_or_B == "B" or A_or_B == "b":
                  speak("After exploring more and more, you lose some of your energy and lost 5 points. ")
                  print("Current Point= 10")
                  print("")
                  speak("Now, you found an old lady in the jungle, who was in need of some help. What will you do?  (A) Help her. (B) Ignore her. and continue exploring. ")
                  A_or_B= input("Type 'A' or 'B': ")
                  if A_or_B == "A" or A_or_B == "a":
                     speak("Great! you helped the old lady and got 10 more points. ")
                     print("Current Point= 20")
                     speak("In return the old lady gave you a magical carpet, by which you reached at the end of the jungle.")
                     print("")
                     win()
                  elif A_or_B == "B" or A_or_B == "b":
                     speak("While exploring more, You were eaten by a Lion on the deep of the jungle. You lost all of your LAST 10 points.   ")
                     print("Current Point= 0")
                     print("")
                     lose()
                  else:
                      wrongInput()
              else:
                  wrongInput()
          else:
              wrongInput()
         
    else:
        wrongInput()

print("Welcome to Jungle Advanture, A simple 'Choose your own'-Game")
speak("Welcome to Jungle Advanture")


speak("What's your name?")
name = input("Your Name: ")

speak("How old are you?")
age = int(input("Your Age: "))
print("")

if age<=10 and age>=6:
    print("")
    print("Please Put on your headset, or turn on your speaker. ")
    print("You need to listen to the Story and type your choice to continue the game.")
    speak("Please Put on your headset, or turn on your speaker. You need to listen to the Story. and type your choice to continue the game.")
    game()
elif age<=5 and age>=0:
    print("")
    print("Sorry! you can not play the game.")
    speak("Sorry! you can not play the game.")
    sys.exit()
   
else:
    print("You are too old to play the game. Still want to continue?")
    ans = input("Type 'YES' or 'NO' : ")
    print("")
    if ans == "YES" or ans == "yes" or ans == "Yes":
        print("")
        print("Please Put on your headset, or turn on your speaker. ")
        print("You need to listen to the Story and type your choice to continue the game.")
        speak("Please Put on your headset, or turn on your speaker. You need to listen to the Story, and type your choice to continue the game.")
        game()
    elif ans == "NO" or ans == "no" or ans == "No":
        sys.exit()

    else:
        print("You have Given a Wrong Input, Please restart the game and try again!")
        speak("You have Given a Wrong Input, Please restart the game. And try again!")
        
                     
    
    
          
    
          
          
    
  

         






