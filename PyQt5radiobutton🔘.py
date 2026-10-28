import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio_button1 = QRadioButton("Visa", self)
        self.radio_button2 = QRadioButton("MasterCard", self)
        self.radio_button3 = QRadioButton("GIFT Card", self)
        self.radio_button4 = QRadioButton("In-Store", self)
        self.radio_button5 = QRadioButton("Online", self)
        self.button_group1= QButtonGroup(self)
        self.button_group2= QButtonGroup(self)
        self.initUI()
        
    def initUI(self):
        self.radio_button1.setGeometry(0, 0, 300, 50)
        self.radio_button2.setGeometry(0, 50, 300, 50)
        self.radio_button3.setGeometry(0, 100, 300, 50)
        self.radio_button4.setGeometry(0, 150, 300, 50)
        self.radio_button5.setGeometry(0, 200, 300, 50)
        
        self.setStyleSheet("QRadioButton {font-size: 40px; font-family: Arial;padding: 10px;}")

        self.button_group1.addButton(self.radio_button1)
        self.button_group1.addButton(self.radio_button2)
        self.button_group1.addButton(self.radio_button3)
        
        self.button_group2.addButton(self.radio_button4)
        self.button_group2.addButton(self.radio_button5)
        
        self.radio_button1.toggled.connect(self.radio_button_changed)
        self.radio_button2.toggled.connect(self.radio_button_changed)
        self.radio_button3.toggled.connect(self.radio_button_changed)
        self.radio_button4.toggled.connect(self.radio_button_changed)
        self.radio_button5.toggled.connect(self.radio_button_changed)
        
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())