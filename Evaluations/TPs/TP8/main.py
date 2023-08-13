from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class AgeCalculatorForm(BoxLayout):
    number1_input = ObjectProperty()
    number2_input = ObjectProperty()
    addition = False
    soustraction = False
    multiplication = False
    division = False
    result_app = ObjectProperty()

    def on_checkbox_Active_add(self, instance, value):
        if value:
            self.addition = True

        else:
            print("checkbox add off")
            self.addition = True
            self.soustraction = False
            self.multiplication = False
            self.division = False

    def on_checkbox_Active_sous(self, checkboxInstance, value):
        if value:
            print("Checkbox sous on")
            self.addition = False
            self.soustraction = True
            self.multiplication = False
            self.division = False
        else:
            print("checkbox sous off")
            self.soustraction = False

    def on_checkbox_Active_mul(self, checkboxInstance, value):
        if value:
            print("Checkbox mult on")
            self.addition = False
            self.soustraction = False
            self.multiplication = True
            self.division = False
        else:
            print("checkbox mult off")
            self.multiplication = False

    def on_checkbox_Active_div(self, checkboxInstance, value):
        if value:
            print("Checkbox div on")
            self.addition = False
            self.soustraction = False
            self.multiplication = False
            self.division = True
        else:
            print("checkbox div off")
            self.division = False

    def buttonClicked(self, btn):
        global tot
        try:
            if self.addition:
                print(self.addition)
                tot = int(self.number1_input.text) + int(self.number2_input.text)

            if self.soustraction:
                tot = int(self.number1_input.text) - int(self.number2_input.text)

            if self.multiplication:
                tot = int(self.number1_input.text) * int(self.number2_input.text)

            if self.division:
                tot = int(self.number1_input.text) / int(self.number2_input.text)

            if not self.division and not self.addition and not self.soustraction and not self.multiplication:
                self.result_app.text = "veuillez choisir une operation"

            self.result_app.text = "le résultat est: {}".format(tot)

        except:
            self.result_app.text = "veuillez entrer un chiffre"


class AgeCalculatorApp(App):
    pass


if __name__ == '__main__':
    AgeCalculatorApp().run()
