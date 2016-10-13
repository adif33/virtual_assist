import redis
import warnings
import speech_recognition as sr

warnings.simplefilter("ignore")

# obtain audio from the microphone
redis_connection = redis.Redis()
while True:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        voice_command = recognizer.recognize_google(audio)
        redis_connection.publish("voice_commands", voice_command)
        print("Google thinks you said " + voice_command)
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
