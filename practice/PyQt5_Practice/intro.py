'''
Docstring for PyQt5_Practice.intro

an intro to frontend python dev

'''

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        #sets x, y, length, width
        self.setGeometry(700,400,500,500)
        self.setWindowIcon(QIcon("salty_hacker.png"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Times", 40))
        label.setGeometry(0,0, 500, 100)

def main():
    #sys.argv allows passing CL args
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()