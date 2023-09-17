import pyttsx3

robot_brain = "I'm robot"

robot_mouth = pyttsx3.init() #khởi tạo hàm pyttsx3
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()