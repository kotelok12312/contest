#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QPushButton,
    QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox)


def showWin():
    victory_win = QMessageBox()
    victory_win.setText("Верно!")
    victory_win.exec()
def loseWin():
    lose_win = QMessageBox()
    lose_win.setText("Нет, в 2015 году.")
    lose_win.exec()

#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle("Конкурс")
#создание виджетов главного окна
question = QLabel("В каком году канал Crazy People получил 'золотую кнопку' от YouTube?")
rbtn1 = QRadioButton('2005')
rbtn1.clicked.connect(loseWin)
rbtn2 = QRadioButton('2010')
rbtn2.clicked.connect(loseWin)
rbtn3 = QRadioButton('2015')
rbtn3.clicked.connect(showWin)
rbtn4 = QRadioButton('2020')
rbtn4.clicked.connect(loseWin)
#расположение виджетов по лэйаутам
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
v_line = QVBoxLayout()
h_line1.addWidget(question, alignment = Qt.AlignCenter)
h_line2.addWidget(rbtn1, alignment = Qt.AlignCenter)
h_line2.addWidget(rbtn2, alignment = Qt.AlignCenter)
h_line3.addWidget(rbtn3, alignment = Qt.AlignCenter)
h_line3.addWidget(rbtn4, alignment = Qt.AlignCenter)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)
window.setLayout(v_line)
#обработка нажатий на переключатели
 
#отображение окна приложения 
window.show()
app.exec()