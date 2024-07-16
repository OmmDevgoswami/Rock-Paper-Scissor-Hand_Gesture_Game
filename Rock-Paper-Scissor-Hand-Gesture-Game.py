import cv2
from cvzone.HandTrackingModule import HandDetector
import random

#Logo Art
LOGO = '''
______           _              ______                                _____      _                    
| ___ \         | |             | ___ \                              /  ___|    (_)                   
| |_/ /___   ___| | __  ______  | |_/ /_ _ _ __   ___ _ __   ______  \ `--.  ___ _ ___ ___  ___  _ __ 
|    // _ \ / __| |/ / |______| |  __/ _` | '_ \ / _ \ '__| |______|  `--. \/ __| / __/ __|/ _ \| '__|
| |\ \ (_) | (__|   <           | | | (_| | |_) |  __/ |             /\__/ / (__| \__ \__ \ (_) | |   
\_| \_\___/ \___|_|\_\          \_|  \__,_| .__/ \___|_|             \____/ \___|_|___/___/\___/|_|   
                                          | |                                                         
                                          |_|                                                        
'''

print(LOGO)

#ASCII ART
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print ("Welcome to the Rock-Paper-Scissor Python Game !!")
print ("Special Hand Gesture Version !!")
start = input ("Press 'Y' to Play or 'N' to Exit: ")
x = 1
player = 0

if start == "Y":
    cam = cv2.VideoCapture(0)
    detector = HandDetector(maxHands = 1)
    while x == 1:
        success, img = cam.read()
        hands, img = detector.findHands(img, draw = True)
    
        cv2.imshow("Images",img)
        if cv2.waitKey(1) & 0xFF == ord("0"): #Press 0 to quite
            x = 0
    
        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            if fingers == [0, 0, 0, 0, 0] or fingers == [1, 0, 0, 0, 0]:
                player = 1
                x = 0
            elif fingers == [1, 1, 1, 1, 1] or fingers == [0, 1, 1, 1, 1]:
                player = 2
                x = 0
            elif fingers == [0, 1, 1, 0, 0] or fingers == [1, 1, 1, 0, 0]:
                player = 3
                x = 0
            else:
                print ("Invalid Input.")


computer = random.randint(1,3)
if (player == 1):
    print ("Player Chose: Rock"+rock)
    if (computer == 1):
        print ("Computer Chose: Rock"+rock)
        print ("This is a Tie !!")
    elif (computer == 2):
        print ("Computer Chose: Paper"+paper)
        print ("You Lose !!")
    else:
        print ("Computer Chose: Scissor"+scissors)
        print ("You Win !!")
elif (player == 2):
    print ("Player Chose: Paper"+paper)
    if (computer == 2):
        print ("Computer Chose: Paper"+paper)
        print ("This is a Tie !!")
    elif (computer == 3):
        print ("Computer Chose: Scissor"+scissors)
        print ("You Lose !!")
    else:
        print ("Computer Chose: Rock"+rock)
        print ("You Win !!")
elif (player == 3):
    print ("Player Chose: Scissor"+scissors)
    if (computer == 3):
        print ("Computer Chose: Scissor"+scissors)
        print ("This is a Tie !!")
    elif (computer == 1):
        print ("Computer Chose: Rock"+rock)
        print ("You Lose !!")
    else:
        print ("Computer Chose: Paper"+paper)
        print ("You Win !!")
else:
    print ("Game Exited !! Thanks for Playing")
        
