import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox = QCheckBox("Check me!",self)
        self.initUI()
        
    def initUI(self):
      self.checkbox.setGeometry(150,200,200,100)
      self.checkbox.setStyleSheet("font-size: 30px;"
       "font-family: Arial;"                           )  
      self.checkbox.setChecked(False)
      self.checkbox.stateChanged.connect(self.checbox_changed)
      
    def checbox_changed(self,state):
        if state == Qt.Unchecked:
            print("Checkbox is unchecked")
        else:
            print("Checkbox is checked")
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
