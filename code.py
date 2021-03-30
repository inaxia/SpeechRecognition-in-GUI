# SPEECH TO TEXT RECOGNITION

# pip install speech_recognition
import speech_recognition

# IN CASE OF "PYAUDIO" ERROR, USE BELOW COMMANDS
# pip install pipwin 
# pipwin install pyaudio

# speech_recognition setup
bot = speech_recognition.Recognizer()

# funtion to add text to .txt file
def addTextToFile(text):
    file_object = open('text_file.txt', 'a')
    file_object.write(text)
    file_object.close()

# main function
with speech_recognition.Microphone() as source:
    print("Listening...\n")
    audioCapture = bot.listen(source)

    try:
        print("Recognizing...")
        recognizedText = bot.recognize_google(audioCapture)
        addTextToFile(recognizedText + "\n")
        print(recognizedText)

    except:
        print("Say that again!")
