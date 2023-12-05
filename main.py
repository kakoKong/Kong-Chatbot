import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import transformers

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
    return True if "hello" in text.lower() else False
  
  def text_to_speech(self, text): 
    print('AI --> ', text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("afplay res.mp3")
    os.remove("res.mp3")

  def action_time(self):
    return datetime.datetime.now().time().strftime('%H:%M')

if __name__ == "__main__":
  ai = ChatBot(name="Dev")
  nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
  while True:
    ai.speech_to_text()
    if (ai.wake_up(ai.text)):
      res = "Hello I am Dev in AI, what can I do for you?"

    elif "time" in ai.text:
      res = ai.action_time()

    elif (any(i in ai.text for i in ["thanks", "thank"])):
        res = np.random.choice(["you're welcome!", "anytime", "no problem", "chill", "Nice to meet you!"])
        exit()

    else:
      if ai.text=="ERROR":
        res="Sorry, come again?"
    
      else:
        chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("assistant: ")+11:].strip()

    ai.text_to_speech(res)