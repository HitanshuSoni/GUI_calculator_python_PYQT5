#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
'''
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):

        label = QLabel("Hi there I'm a label")
            okButton = QPushButton("OK")
            cancelButton = QPushButton("Cancel")

            horizontal = QHBoxLayout()
            horizontal.addStretch(1)

            horizontal.addWidget(okButton)
            horizontal.addWidget(cancelButton)

            vertical = QVBoxLayout()
            vertical.addWidget(label)
            vertical.addStretch
            vertical.addLayout(horizontal)

            self.setLayout(vertical)
            
        
        self.text_label = QLabel("There has been no name entered, so I can't do anything yet.")
        self.label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.button = QPushButton("Clicked: 0")
        self.button.setText("Set Name")

        #button.clicked.connect(self.clickedButton)
        self.button.pressed.connect(self.alterName)

        self.button.released.connect(self.clickedButton)
        
        h = QHBoxLayout()
        
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Nothing is clicked")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        print(inputted_text)
        our_string = "You've entered"+ inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text+"'s Window")

    def clickedButton(self):
        print("Button released")

    def pressButton(self):
        print("Button Pressed")
        self.counter+=1
        self.button.setText("Clicked:"+str (self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(app.exec_())
    

'''



class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda:self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        
        elif v=="AC":
            self.results.setText("")

        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))

        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])

        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)


class Appliction(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()

    def CreateApp(self):
        # Create our grid
        grid = QGridLayout()
        results = QLineEdit()

        '''button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Last Button")

        grid.addWidget(button1, 0, 0, 1, 1)
        grid.addWidget(button2, 0, 1, 1, 1)
        grid.addWidget(button3, 0, 2, 1, 1)
        grid.addWidget(button4, 1, 0, 1, 2)'''

        buttons = ["AC", "DEL", "√", "/", 
                    7, 8, 9, "*",
                    4, 5, 6, "-", 
                    1, 2, 3, "+", 
                    0, ".", "="]
        
        grid.addWidget(results, 0, 0, 1, 4)
        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                col = 0
                row+=1

            buttonObject = Button(button, results)
            if button == 0:
                grid.addWidget(buttonObject.b, row, col, 1, 2)
                col+=1
            else:
                grid.addWidget(buttonObject.b, row, col, 1, 1)

            col+= 1


        

        self.setLayout(grid)



        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Appliction()
    sys.exit(app.exec_())
    