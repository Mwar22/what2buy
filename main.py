__version__ = '0.1'
import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen


#Importa as bibliotecas pessoais auxiliares
from startscreen import Tela1
from startscreen2 import Tela2


class What2buyApp(App):

    def build(self):

        #Carrega os layouts das telas
        Builder.load_file('startscreen.kv')
        Builder.load_file('startscreen2.kv')
        return Gui()

#Widget principal
class Gui(ScreenManager):
    __telas = []
    __count = 0

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        t1 = Tela1(name = 't1')
        t2 = Tela2(name = 't2')
        
        t1.setGui(self)
        

        self.add_widget(t1)
        self.add_widget(t2)

        self.__telas.append(t1)
        self.__telas.append(t2)

    def nextscreen(self):
        self.switch_to(self.__telas[1])     
        
if __name__ == '__main__':
    What2buyApp().run()
