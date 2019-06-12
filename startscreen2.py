'''
    Segunda tela de abertura do App.

    Explicação:
      Tela de pesquisa por produtos faltantes.

'''

import kivy
kivy.require('1.11.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class Tela2(Screen):
    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
