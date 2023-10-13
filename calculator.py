import PyQt5.QtWidgets as qtw
from functools import partial


NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
OPERATORS = ["-","+","/","**","*"]

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kalkulator')
        self.setLayout(qtw.QVBoxLayout())
        self.setFixedSize(330,220)
        self.UserInterface()
        self.show()
        self.temp_nums = []
        self.fin_nums = []


    def UserInterface(self):
        self.container = qtw.QWidget()
        self.container.setStyleSheet("background-color : gray")
        self.container.setLayout(qtw.QGridLayout())
        self.result_field = qtw.QLineEdit()
        self.result_field.setStyleSheet("background-color: 2px solid white")
        self.result_field.setReadOnly(True)
        self.layout().addWidget(self.container)
        self.container.layout().addWidget(self.result_field,0,0,1,4)
        self.createButtons()

    def createButtons(self):
        self.buttons={}
        buttons = {
            "7": (2, 2),
            "8": (2, 1),
            "9": (2, 0),
            "/": (5, 3),
            "4": (3, 2),
            "5": (3, 1),
            "6": (3, 0),
            "*": (4, 3),
            "1": (4, 2),
            "2": (4, 1),
            "3": (4, 0),
            "-": (3, 3),
            "+": (2, 3),
            "^": (5,2),
            "0": (1,1),
            "(": (5,0),
            ")": (5,1)
        }
        clear_button = {
            "Clear": (1,2,1,2),
        }
        equal_button = {
            "=": (1,0)
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = qtw.QPushButton(btnText,self)
            if  btnText not in NUMBERS:
               self.buttons[btnText].setStyleSheet("background-color : orange")
            self.buttons[btnText].clicked.connect(partial(self.action_click, btnText))
            self.container.layout().addWidget(self.buttons[btnText], pos[0], pos[1])

        for btnText, pos in clear_button.items():
            self.buttons[btnText] = qtw.QPushButton(btnText,self)
            self.buttons[btnText].clicked.connect(self.clear_calc)
            self.container.layout().addWidget(self.buttons[btnText], pos[0], pos[1], pos[2], pos[3])

        for btnText, pos in equal_button.items():
            self.buttons[btnText] = qtw.QPushButton(btnText,self)
            self.buttons[btnText].clicked.connect(self.equals)
            self.container.layout().addWidget(self.buttons[btnText], pos[0], pos[1])



    def action_click(self,key):
        if key in NUMBERS:
            number = str(key)
            self.temp_nums.append(number)
            temp_string = ''.join(self.temp_nums)
            if self.fin_nums:
                self.result_field.setText(''.join(self.fin_nums) + temp_string)
            else:
                self.result_field.setText(temp_string)
        else:
            temp_string = ''.join(self.temp_nums)
            self.fin_nums.append(temp_string)
            self.fin_nums.append(key)
            self.temp_nums = []
            self.result_field.setText(''.join(self.fin_nums))

    def equals(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string = str(result_string)
        self.temp_nums = []
        self.fin_nums = []
        self.result_field.setText(fin_string)
        self.fin_nums.append(fin_string)



    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

def main():
    # Wywołanie aplikcaji
    app = qtw.QApplication([])

    #Wywołanie okna i start programu
    mw = MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()
