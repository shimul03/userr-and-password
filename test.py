

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy import Config
Config.set('graphics', 'multisamples', '0')

class loging(GridLayout):
    def __init__(self, **kwargs):
        super(loging,self).__init__(**kwargs)
        self.cols=2
    
        self.add_widget(Label(text="Username"))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)
    
        self.add_widget(Label(text="password"))
        self.password=TextInput(multiline=False,password=True)
        self.add_widget(self.password)
    


class simpleclass(App):
    def build(self):
        return loging()
    
    
if __name__=="__main__":
    
    
    simpleclass().run()
    

