import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 200)
    w.move(300, 300)
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    w.show()
    sys.exit(app.exec_())