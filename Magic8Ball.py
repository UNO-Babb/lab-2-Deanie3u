#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["How are you?", "Hi!", "what's up?" "What are you doing today?", "Is that so?", "Oh I see", 
             "It is wonderful!","What is your dream job?", "I am good!", "I am doing homework, wbu?",
               "Do you feel like a leader or follower", " What's your dream job?", "My dream job is to be an Engineering."]
  #Answer question randomly with one of the options from your earlier list.
  num = random.random() # decimal 0 - 1
  num = num * 1000 #number 0 - 999 with decimals
  num = int(num) #no more decimals
  
  things = len(answers)
  num = num % things
  question = input("Ask me a question: ")
  print(answers[num])
  
  
  
if __name__ == '__main__':
  main()
