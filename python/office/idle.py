# Your code here
from random import randint

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[randint(0, 3)]
    print("Chatting with ", chatee, "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")

def useSocialMedia():
    socialMedia = [
      "FaceBook", 
      "Twitter",
      "YouTube", 
      "Reddit", 
      "Instagram", 
      "TikTok"
      ]
    choice = socialMedia[randint(0, 5)]
    print("Using " + choice + "...")
    print("Done")
