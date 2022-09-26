import kivy
import re

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

# [^*/+-]{1}
# [^0-9]
# [A-Z][A-Za-z0-9]{1,15}

class IntInput(TextInput):
    # pat = re.compile('[^0-9+-/*]') # всё кроме этих символов изменяется на '' в re.sub(pat, '', string)
    # pat = re.compile('[0-9]|[\-]+|[\+]+|[\*]+|[\/]+')
    # pat = re.compile('[0-9]|[\-]+|[\+]+')

    f = 0
    def replacing(self, matchobj):
        nm = [str(i) for i in range(10)]
        if self.f == 1 and matchobj.group(0)[0] not in nm:
            return ""
        if matchobj.group(0)[0] == '-':
            self.f = 1
            return "-"
        if matchobj.group(0)[0] == '+':
            self.f = 1
            return "+"
        # if matchobj.group(0)[0] == '*':
        #     self.f = 1
        #     return "*"
        # if matchobj.group(0)[0] == '/':
        #     self.f = 1
        #     return "/"
        s = ""
        self.f = 0
        for i in matchobj.group(0):
            if i in nm:
                s += str(i)
        return s

    def keyboard_on_key_up(self, window, keycode):
        if keycode[1] == "backspace":
            self.f = 0

    def insert_text(self, substring, from_undo=False):
        # pat = self.pat
        # if '+' in self.text:
        #     s = re.sub(pat, '', substring)
        # else:
        #     s = '+'.join(
        #         re.sub(pat, '', s)
        #         for s in substring.split('+', 1)
        #     )
        # return super().insert_text(s, from_undo=from_undo)

        # s = re.sub(self.pat, '', substring)

        s = re.sub('[0-9]|[\-]+|[\+]+', self.replacing, re.sub('[^0-9+-/*]','',substring))

        return super().insert_text(s, from_undo=from_undo)

class MyApp(App):
    total_sum = 0

    def build(self):
        # main_layout = BoxLayout(orientation='vertical')
        # main_layout = GridLayout(rows =2)
        main_layout = FloatLayout()

        self.label_total = Label(text='Current total sum = '+str(self.total_sum),
                            size_hint=(1., .05),
                            pos_hint={'center_x': .5, 'center_y': .475}
                            )
        self.input = IntInput(
            multiline=True, readonly=False, halign="right", font_size=20,
            size_hint=(1., .25),
            pos_hint={'center_x': .5, 'center_y': .875}
        )
        self.solution = IntInput(
            multiline=True, readonly=True, halign="right", font_size=20,
            size_hint=(1., .25),
            pos_hint={'center_x': .5, 'center_y': .625}
        )
        rbutton = Button(text='Run',
                        size_hint=(.5, .25),
                        pos_hint={'center_x': .25, 'center_y': .25}
                        )
        cbutton = Button(text='Clear',
                         size_hint=(.5, .25),
                         pos_hint={'center_x': .75, 'center_y': 0.25}
                         )

        main_layout.add_widget(self.label_total)
        main_layout.add_widget(self.input)
        main_layout.add_widget(self.solution)
        main_layout.add_widget(rbutton)
        main_layout.add_widget(cbutton)

        rbutton.bind(on_press=self.on_press_button)
        cbutton.bind(on_press=self.on_press_buttonC)
        self.label_total.bind(on_change=self.on_change_label)

        return main_layout

    def on_change_label(self):
        self.label_total.text = 'Current total sum = '+str(self.total_sum)
        return

    def choose_operator(self, op, a, b):
        if op == '+':
            ret = a+b
            return a+b
        if op == '-':
            return a-b
        if op == '*':
            return a*b
        if op == '/':
            return a/b

    def on_press_buttonC(self, instance):
        self.total_sum = 0
        self.solution.text = ''
        self.input.text = ''
        self.on_change_label()
        return

    def on_press_button(self, instance):
        out = 0
        if self.input.text != '':
            if self.input.text[-1] in ['+','-','*','/']:
                self.input.text = self.input.text[:-1]
            if self.input.text[0] in ['+','*','/']:
                self.input.text = self.input.text[1:]
            nums = re.findall('[0-9]+', self.input.text)
            operators = re.findall('[^0-9]', self.input.text)
            if self.input.text[0] == '-':
                nums[0] = str(int(nums[0])*(-1))
                operators.pop(0)
                self.solution.text = str(self.total_sum) + self.input.text
                self.input.text = self.input.text[1:]
            else:
                self.solution.text = str(self.total_sum) + '+' + self.input.text
            out = int(nums[0])
            for i in range(len(operators)):
                a = out
                b = int(nums[i+1])
                out = self.choose_operator(operators[i], a, b)

        #     print(kivy.app.App.user_data_dir)

        # fname = str(kivy.app.App.user_data_dir) + '/save_file.txt'
        # f = open(fname, 'r+')
        # f.write(str(out))
        # f.close()

        self.total_sum += out
        self.solution.text += '='+str(self.total_sum)
        self.input.text = ''
        self.on_change_label()
        return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()