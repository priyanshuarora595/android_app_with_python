from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout


screen_helper = """
ScreenManager:
    WelcomeScreen:
    MenuScreenEng:
    engnum2word:
    engword2num:

      
<WelcomeScreen>:
    name : 'welcome'
    
    MDLabel:
        text: 'WELCOME'
        halign : 'center'
        pos_hint : {'center_x':0.5 , 'center_y' : 0.8}
        font_size : '40sp'
    
    MDLabel:
        text: 'To Continue Press Next'
        halign : 'center'
        pos_hint : {'center_x':0.5 , 'center_y' : 0.7}
        font_size : '35sp'
    
    MDRoundFlatButton:
        text: ' next '
        font_size : '45sp'
        pos_hint : {'center_x':0.5 , 'center_y' : 0.5}
        halign : 'center'
        on_press: root.manager.current = 'menuE'
        
    Image:
        source: 'images.png'
        pos_hint : {'center_x':0.5 , 'center_y' : 0.2}
        

        
<MenuScreenEng>:
    name: 'menuE'
    MDLabel:
        text: ' PLEASE CHOOSE '
        halign : 'center'
        pos_hint : {'center_x':0.5 , 'center_y' : 0.8}
        font_size : '50sp'
         
    MDRoundFlatButton:
        text: " NUMBER TO WORD "
        pos_hint: {'center_x':0.5,'center_y':0.6}
        font_size : '25sp'
        on_press : root.manager.current = 'engnum2word'
    
    MDRoundFlatButton:
        text: " WORD TO NUMBER "
        pos_hint: {'center_x':0.5,'center_y':0.4}
        font_size : '25sp'
        on_press: root.manager.current = 'engword2num'
        
    MDRoundFlatButton:
        text: " BACK "
        pos_hint: {'center_x':0.5,'center_y':0.2}
        font_size : '25sp'
        on_press: root.manager.current = 'welcome'
        
<engnum2word>:
    name : 'engnum2word'
    
    MDLabel :
        text : "WELCOME"
        halign : "center" 
        pos_hint : {'center_y': 0.9, 'center_x': 0.5}
        font_style : "H3"
        
    MDLabel : 
        text : "NUMBER TO WORD CONVERTER" 
        halign : "center" 
        pos_hint : {'center_y': 0.7, 'center_x': 0.5}
        font_style : "H4"
    
    MDTextField:
        id : txt_inpt
        hint_text:"Enter Any Number"
        helper_text : "integer only"
        helper_text_mode : "on_focus"
        pos_hint : {'center_y': 0.5, 'center_x': 0.5}
        size_hint_x:None
        width:300
        
    MDRoundFlatButton:
        text : "convert"
        pos_hint : {'center_y': 0.3, 'center_x': 0.5}
        on_release : root.shownum2word(txt_inpt.text)
    
    MDRoundFlatButton:
        text: " BACK "
        pos_hint: {'center_x':0.5,'center_y':0.2}
        font_size : '25sp'
        on_press: root.manager.current = 'menuE' ; txt_inpt.text = ''
        
<engword2num>:
    name: 'engword2num'

    MDLabel :
        text : "WELCOME"
        halign : "center" 
        pos_hint : {'center_y': 0.9, 'center_x': 0.5}
        font_style : "H3"
        
    MDLabel : 
        text : "WORD TO NUMBER CONVERTER" 
        halign : "center" 
        pos_hint : {'center_y': 0.7, 'center_x': 0.5}
        font_style : "H4"
    
    MDTextField:
        id : tx_inpt
        hint_text:"Enter words"
        helper_text : "numerical words only"
        helper_text_mode : "on_focus"
        pos_hint : {'center_y': 0.5, 'center_x': 0.5}
        size_hint_x:None
        width:300
        
    MDRoundFlatButton:
        text : "convert"
        pos_hint : {'center_y': 0.3, 'center_x': 0.5}
        on_release : root.showengword2num(tx_inpt.text)
        
    MDRoundFlatButton:
        text: " BACK "
        pos_hint: {'center_x':0.5,'center_y':0.2}
        font_size : '25sp'
        on_press: root.manager.current = 'menuE' ; tx_inpt.text = ''
    
        
"""


class WelcomeScreen(Screen):
    pass


class MenuScreenEng(Screen):
    pass


class engnum2word(Screen):

    def shownum2word(self, obj):
        def Words(n):
            units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                     "Eighteen",
                     "Nineteen"]
            tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            if n <= 9:
                return units[n]
            elif 10 <= n <= 19:
                return teens[n - 10]
            elif 20 <= n <= 99:
                return tens[(n // 10) - 2] + " " + (units[n % 10] if n % 10 != 0 else "")
            elif 100 <= n <= 999:
                return Words(n // 100) + " Hundred " + (Words(n % 100) if n % 100 != 0 else "")
            elif 1000 <= n <= 99999:
                return Words(n // 1000) + " Thousand " + (Words(n % 1000) if n % 1000 != 0 else "")
            elif 100000 <= n <= 9999999:
                return Words(n // 100000) + " Lakh " + (Words(n % 100000) if n % 100000 != 0 else "")
            elif n >= 10000000:
                return Words(n // 10000000) + " Crore " + (Words(n % 10000000) if n % 10000000 != 0 else "")

        n = int(obj)
        x = Words(n)
        close_button = MDFlatButton(text='okay', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Entered number in words is',
                               size_hint=(0.5, 1),
                               text=x,
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class engword2num(Screen):

    def showengword2num(self, obj):
        def word2num(n):
            units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                     "Nineteen"]
            tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            extra = [0, 0, "Hundred", "Thousand", 0, "Lakh", 0, "Crore"]
            i = 0
            out = []
            while i < len(n):
                num = 0
                if n[i] in units:
                    out.append(units.index(n[i]))

                elif n[i] in teens:
                    num = (10 + teens.index(n[i]))
                    out.append(num)

                elif n[i] in tens:
                    num = ((10 * (tens.index(n[i]) + 2)))
                    out.append(num)

                elif n[i] in extra:
                    if n[i - 2] in tens and i - 2 >= 0:
                        num = ((out[len(out) - 2]) * (10 ** (extra.index(n[i]))))
                        out.append(num)
                        num = ((out[len(out) - 2]) * (10 ** (extra.index(n[i]))))
                        out.append(num)
                        out.pop(len(out) - 3)
                        out.pop(len(out) - 3)
                    else:
                        if n[i - 1] in tens:
                            num = ((out[len(out) - 1]) * (10 ** (extra.index(n[i]))))
                            out.append(num)
                            out.pop(len(out) - 2)

                        elif n[i - 1] in units:
                            if len(out) > 1:
                                num = ((out[len(out) - 1]) * (10 ** (extra.index(n[i]))))
                                out.append(num)
                                out.pop(len(out) - 2)
                            elif len(out) == 1:
                                num = ((out[len(out) - 1]) * (10 ** (extra.index(n[i]))))
                                out.append(num)
                                out.pop(i - 1)
                i += 1
            sum = 0
            for j in out:
                sum += j
            return sum

        user_input = str(obj)
        user_input = user_input.title()
        user_input = user_input.split()
        y = str(word2num(user_input))
        close_button = MDFlatButton(text='okay', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Entered number in words is',
                               size_hint=(0.5, 1),
                               text=y,
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


sm = ScreenManager()

sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(MenuScreenEng(name='menuE'))
sm.add_widget(engnum2word(name='engnum2word'))
sm.add_widget(engword2num(name='engword2num'))


class converterApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


converterApp().run()
