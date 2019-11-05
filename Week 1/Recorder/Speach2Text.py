import speech_recognition as sr
from pygame import mixer
from tkinter import messagebox
import pygame as pg
import time
import os
import sys
sys.path.append('../summary/')
from Base_Summary import Final_Summary

class STT:
    def display_summary():
        messagebox.showinfo("Summary", Final_Summary.Get_Summary())
    def play_summary(self):
        mixer.init()
        mixer.music.load('../recorded/summary.wav')
        mixer.music.play()

    def save_file(self):
        pass

    def callback(self):
        pass

    def play_original():
        try:
            mixer.init()
            mixer.music.load('../recorded_audio/microphone-results.wav')
            mixer.music.play()
        except:
            print("No Audio File is Found")

    def buttonClick():
        mixer.init()
        mixer.music.load('../sound/chime1.mp3')
        mixer.music.play()

        r = sr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 400
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=5)
                message = str(r.recognize_google(audio))
                mixer.music.load('../sound/chime2.mp3')
                mixer.music.play()
                messagebox.showinfo("You Said....", message)
                file = open("../transcripts/transcript.txt", "w")
                file.write(message)
                file.close()

            except sr.UnknownValueError:
                print('Google Speech Recognition could not Understand audio')
            except sr.RequestError as e:
                print('Could not request result from Google Speech Recogniser Service')
            else:
                pass

        with open("../recorded_audio/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())