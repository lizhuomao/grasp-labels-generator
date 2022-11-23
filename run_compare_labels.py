import sys
import compare_labels
from util.load_compare_image import CImageset


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = compare_labels.Ui_MainWindow()
    ui.setupUi(mainWindow)
    imageset = CImageset()
    ui.pushButton.clicked.connect(lambda: imageset.prior(ui))
    ui.pushButton_2.clicked.connect(lambda: imageset.begin(ui))
    ui.pushButton_3.clicked.connect(lambda: imageset.next(ui))
    ui.pushButton_4.clicked.connect(lambda: imageset.need_relabel(ui))
    mainWindow.show()
    sys.exit(app.exec_())