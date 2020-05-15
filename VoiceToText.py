import speech_recognition as speech


def listen(x):
    speech_recog = speech.Recognizer();
    if x == 0:
        print('say Hi. How can I help?')
    with speech.Microphone() as m:
        audio = speech_recog.listen(m)
        try:
            result_text = speech_recog.recognize_google(audio, language='eng-in')
            print(result_text)
            return result_text
        except:
            if x == 1:
                print('say Good Bye!')
            print('say I did not get that. Please say again.')
            listen(1)


listen(0)
