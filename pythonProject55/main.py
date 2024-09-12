import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import speech_recognition as sr

class VoiceRecognitionApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Press the button and speak', font_size='20sp')
        self.button = Button(text='Speak', size_hint=(1, 0.2), on_press=self.recognize_speech)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def recognize_speech(self, instance):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.text = "Listening..."
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            self.label.text = f"Recognized: {text}"
        except sr.UnknownValueError:
            self.label.text = "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            self.label.text = f"Could not request results; {e}"

if __name__ == '__main__':
    VoiceRecognitionApp().run()
