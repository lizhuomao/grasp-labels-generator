import sys
import label_test
from util.load_image import ImageSet
from event.button_event import add_new_labels, delete_labels


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = label_test.Ui_MainWindow()
    ui.setupUi(mainWindow)
    imageset = ImageSet()
    ui.pushButton.clicked.connect(lambda: imageset.begin(ui))
    ui.pushButton_2.clicked.connect(lambda: imageset.piror(ui))
    ui.pushButton_3.clicked.connect(lambda: imageset.next(ui))
    ui.pushButton_4.clicked.connect(lambda: add_new_labels(ui, imageset))
    ui.pushButton_5.clicked.connect(lambda: delete_labels(ui, imageset))
    mainWindow.show()
    sys.exit(app.exec_())
