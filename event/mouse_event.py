import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore


class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, ui, parent=None):
        super(MyGraphicsView, self).__init__(parent)
        self.pos = []
        self.temp_pos = []
        self.clicked_cnt = 0
        self.ui = ui

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() == QtCore.Qt.LeftButton:
            x, y = float(event.pos().x()), float(event.pos().y())
            print("x = {}, y = {}".format(x, y))
            if self.clicked_cnt == 0:
                self.temp_pos.append([x, y])
                self.clicked_cnt += 1
            elif self.clicked_cnt == 1:
                self.temp_pos.append([x, y])

                line1 = QtWidgets.QGraphicsLineItem()
                line1.setZValue(3)
                pen = QtGui.QPen()
                color = QtGui.QColor()
                color.setGreen(255)
                pen.setColor(color)
                pen.setWidth(2)
                line1.setPen(pen)
                line1.setLine(self.temp_pos[0][0], self.temp_pos[0][1],
                              self.temp_pos[1][0], self.temp_pos[1][1])
                self.scene().addItem(line1)

                self.clicked_cnt += 1
            elif self.clicked_cnt == 2:
                self.temp_pos.append([x, y])

                a = (self.temp_pos[1][1] - self.temp_pos[0][1]) \
                    / (self.temp_pos[1][0] - self.temp_pos[0][0])
                b = self.temp_pos[0][1] - (a * self.temp_pos[0][0])
                x_c = (((1 / a) - a) * self.temp_pos[2][0] + 2 *
                       self.temp_pos[2][1] - 2 * b) / (a + (1 / a))
                y_c = self.temp_pos[2][1] - (x_c - self.temp_pos[2][0]) / a

                self.temp_pos.append([x_c, y_c])
                line2 = QtWidgets.QGraphicsLineItem()
                line2.setZValue(3)
                pen = QtGui.QPen()
                color = QtGui.QColor()
                color.setRgb(255, 0, 255)
                pen.setColor(color)
                pen.setWidth(2)
                pen.setStyle(QtCore.Qt.DashDotLine)
                line2.setPen(pen)
                line2.setLine(self.temp_pos[2][0], self.temp_pos[2][1],
                              self.temp_pos[3][0], self.temp_pos[3][1])
                self.scene().addItem(line2)
                self.temp_pos = np.around(self.temp_pos, 2)
                width = np.around(np.sqrt((self.temp_pos[3][0] - self.temp_pos[2][0]) ** 2
                                          + (self.temp_pos[3][1] - self.temp_pos[2][1]) ** 2), 2)

                pos_str_list = [str(x) + " " + str(y) for x, y in self.temp_pos]
                pos_str = pos_str_list[0] + " " + pos_str_list[1] + " " + str(width)
                self.ui.listView.addItem(pos_str)

                self.pos.append([self.temp_pos[0][0], self.temp_pos[0][1], self.temp_pos[1][0], self.temp_pos[1][1], width])
                self.clicked_cnt = 0
                self.temp_pos = []
                print(self.pos)
