import random
import speech_recognition as sr
import pyttsx3

truth_questions = [
    "What is your biggest fear?",
    "Have you ever cheated on a test?",
    "What is your most embarrassing moment?",
    "Have you ever lied to your best friend?",
    "What is your guilty pleasure?",
    "What's the most childish thing you still do?",
    "What is your weirdest habit?",
    "Have you ever stolen anything?",
    "What's the most embarrassing thing you've ever done on a date?",
    "Have you ever been caught picking your nose?",
    "What's the grossest thing you've ever eaten?",
    "What's the dumbest thing you've ever done?",
    "What's the most embarrassing thing your parents have caught you doing?",
    "What's the weirdest dream you've ever had?",
    "What's the most embarrassing thing you've ever said to someone you liked?",
    "Have you ever peed in a pool?",
    "Have you ever had a crush on a teacher?",
    "What's the strangest place you've ever fallen asleep?",
    "What's the most embarrassing nickname you've ever had?",
    "What's the most embarrassing thing you've done in school?",
    "Have you ever accidentally walked into a wall or door?",
    "What's the most embarrassing thing you've done while drunk?",
    "Have you ever sent a text to the wrong person?",
    "What's the most embarrassing thing your parents have ever done?",
    "Have you ever farted loudly in public?",
    "Have you ever been caught checking someone out?",
    "Have you ever picked your nose and eaten it?",
    "What's the most embarrassing thing you've done in front of a crowd?",
    "What's the most embarrassing thing you've ever worn?",
    "What's the worst lie you've ever told?",
    "What's the most embarrassing thing you've ever been caught doing?",
    "Have you ever walked into a glass door?",
    "What's the most embarrassing thing that's ever happened to you on stage?",
    "What's the most embarrassing thing you've ever done at a party?",
    "Have you ever laughed so hard you peed your pants?",
    "What's the most embarrassing thing you've ever done in front of your crush?",
    "What's the most embarrassing thing you've ever done at work?",
    "What's the most embarrassing thing you've ever done in front of your parents?",
    "Have you ever been caught singing in the shower?",
    "What's the most embarrassing thing you've ever done on social media?",
    "Have you ever accidentally called someone the wrong name?",
    "What's the most embarrassing thing you've ever done while on a date?",
    "Have you ever walked into the wrong restroom?",
    "What's the most embarrassing thing you've ever done at school?",
    "What's the most embarrassing thing you've ever done in front of your siblings?",
    "Have you ever accidentally sent a text to the wrong person?",
    "What's the most embarrassing thing you've ever done in front of your boss?",
    "What's the most embarrassing thing you've ever done at a sleepover?",
    "Have you ever gotten caught lip-syncing in public?",
    "What's the most embarrassing thing you've ever done at a family gathering?",
    "Have you ever fallen asleep in class?",
    "What's the most embarrassing thing you've ever done on a video call?",
    "Have you ever had food stuck in your teeth and not realized it?",
    "What's the most embarrassing thing you've ever done in front of your crush's parents?",
    "What's the most embarrassing thing you've ever done at the gym?",
    "Have you ever walked into a glass window?",
    "What's the most embarrassing thing you've ever done at a restaurant?",
    "Have you ever walked into a wall while texting?",
    "What's the most embarrassing thing you've ever done in front of a celebrity?",
    "What's the most embarrassing thing you've ever done in front of your grandparents?",
     "Have you ever tripped in public and pretended it didn't happen?",]
dare_questions = [
    "Dance to a random song for one minute.",
    "Do your best impression of a famous celebrity.",
    "Speak in an accent for the next three rounds.",
    "Take a silly selfie and post it on your social media.",
    "Do 10 jumping jacks in a row.",
    "Send a funny meme to the third person in your contact list.",
    "Wear socks on your hands for the next three turns.",
    "Give yourself a funny nickname and use it for the rest of the game.",
    "Do your best robot dance for two minutes.",
    
"Call a friend and sing 'Happy Birthday' to them, regardless of whether it's their birthday or not.",

    "Speak in rhyme for the next three turns.",
    "Take a silly face selfie and set it as your profile picture for the next hour.",
    "Create a short rap about the person to your left.",
    "Send a text message to your crush (or someone you like) saying you have a crush on them.",
    "Do 15 push-ups right now.",
    "Call a family member and sing them a song.",
    "Wear a sock puppet on one hand for the next five rounds.",
    "Send a message to the fifth person in your contact list with just emojis.",
    "Do your best impression of a famous cartoon character.",
    "Take a funny video of yourself doing a random dance and share it with the group.",
    "Tell a joke that makes everyone laugh.",
    "Post a random fact about yourself on your social media.",
    "Do 20 squats right now.",
    "Take a screenshot of your recent calls and send it to the group.",
    "Draw a funny picture of the person to your right and show it to everyone.",
    "Send a voice message to your best friend saying something random and funny.",
    "Wear a hat for the rest of the game.",
    "Act out a scene from your favorite movie for one minute.",
    "Send a silly selfie to the second person in your contact list.",
    "Do your best animal impression for the next three turns.",
    "Post a poll on your social media asking a random and funny question.",
    "Wear sunglasses indoors for the next five rounds.",
    "Send a message to the seventh person in your contact list with a cheesy pick-up line.",
    "Do 10 cartwheels in a row.",
    "Create a short skit with another player.",
    "Send a funny meme to the first person in your contact list.",
    "Act like a news reporter and give a dramatic report on a random object in the room.",
    "Wear a mustache made of drawn-on marker for the next three turns.",
    "Send a text message to a friend confessing a made-up secret and see how they respond.",
    "Do 10 high fives in a row with different people.",
    "Tell a funny story from your childhood.",
    "Wear a towel as a cape for the next five rounds.",
    "Send a message to the tenth person in your contact list with a joke.",
    "Do the floss dance for two minutes.",
    "Create a funny poem on the spot about a topic chosen by the group.",
    "Send a voice message to the group singing a silly song.",
    "Wear mismatched shoes for the rest of the game.",
    "Send a message to the fourth person in your contact list with a compliment.",
    "Do your best impersonation of a famous singer for one minute.",
    "Take a silly group photo with everyone playing the game and share it on social media.",
    "Wear a funny hat for the next five rounds.",
    "Send a text message to your parents saying you won the lottery (but it's just a joke).",
    "Do a handstand for as long as you can.",
    "Create a funny jingle about a random object in the room.",
    "Send a message to the sixth person in your contact list with a pun.",
    "Act like a superhero for the next three turns.",
    "Tell a funny joke that involves everyone in the group.",
    "Wear a tie around your head for the next five rounds."
]
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak(("Enter the number of players: "))
r = int(input())
playernames = []
play=[]
for i in range(r):
    player_name = input("Enter player name: ")
    playernames.append(player_name)
    
while(r!=0):
 
    
 for i in range(2):
   mainplayers = random.sample(playernames,i)
   play.append(mainplayers)

 speak(play [0])
 print(play [0])
 speak(  "is the questionare")
 speak( play[1] )
 print(play [1])
 speak("to answer")
 
   
 q = random.randint(0,60)
 if(q%2==0):
     speak("truth")
     print("truth" , truth_questions[q])
     speak(truth_questions[q])
     
 else: 
     speak("dare") 
     print("dare" , dare_questions[q])
     speak(dare_questions[q])
 speak("one more round")
 
 e = int(input()) 
 
 if(e==0): r = 0
 else: r==r
 play = []
    
    