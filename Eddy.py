from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pyttsx3

F =" FFFF \n"





Form, Window = uic.loadUiType("menu.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def bp():
    engine = pyttsx3.init()
    engine.say(F)
    engine.runAndWait()
    form.plainTextEdit.setText(F)
    form.label.setText(F)




form.pushButton.clicked.connect( bp )


app.exec_()