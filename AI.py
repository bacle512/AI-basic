import speech_recognition
import pyttsx3
from datetime import *

robot_mouth = pyttsx3.init() #khởi tạo hàm pyttsx3
robot_ear = speech_recognition.Recognizer() #khởi tạo 1 biến có thể nghe
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...") #để kiểm tra xem giọng nói đã nhận đc chưa

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
        
    elif "hello" in you:
        robot_brain = "Hello, how are you?"
        
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
        
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
        
    elif "bye" in you:
        robot_brain = "Bye, see you later!"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
        
    else:
        robot_brain = "I'm fine thank"

    print(robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()