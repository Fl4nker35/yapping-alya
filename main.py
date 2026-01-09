import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

app = QApplication(sys.argv)
label = QLabel()

label.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
label.setAttribute(Qt.WA_TranslucentBackground)

gif = QMovie("alya_small.gif")
label.setMovie(gif)
gif.start()

label.show()
sys.exit(app.exec_())
