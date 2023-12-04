import numpy as np
import pyaudio
import speech_recognition as sr

class ChatBot():
  def __init__(self, name):
    print("----- starting up", name, "------")
    self.name = name

  def speech_to_text(self):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
      print("Listening...")
      audio = recognizer.listen(mic)
    try:
      self.text = recognizer.recognize_google(audio)
      print("me --> ", self.text)

    except Exception as e:
      print("me --> ERROR", str(e))

  def wake_up(self, text):
    return True if self.name in text.lower() else False

if __name__ == "__main__":
  ai = ChatBot(name="Dev")
  while True:
    ai.speech_to_text()
    if (ai.wake_up(ai.text)):
      res = "Hello I am Dev in AI, what can I do for you?"