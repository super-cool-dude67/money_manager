from models import engine,Products,Drinks,Base
from sqlalchemy.orm import Session
from sqlalchemy import select
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFontDialog,QColorDialog
from PyQt5.QtGui import QFont,QColor
from UI import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def get_drinks(self):
        with Session(engine) as session:
            drinks = session.scalar(select(Drinks)).all()      
        return drinks
    def update_data(self):
        items = self.ui.list_model.stringList()         
        items.append("test")
        self.ui.list_model.setStringList(items)
app = QApplication(sys.argv)     
window = MainWindow()
window.show()
window.update_data()
sys.exit(app.exec_())

