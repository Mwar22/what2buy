'''
    Tela de abertura do App.

    Explicação:
      Contém a lógica principal desta tela

'''

import kivy
kivy.require('1.11.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

#Tela 1...      
class Tela1(Screen):
    __gui = None
    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)

    def setGui(self, gui):
        self.__gui = gui

    def getGui(self):
        return self.__gui

def minore(a,b):
    if a >= b:
        return b
    else:
        return a
