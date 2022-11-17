from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QMessageBox


def load_label_to_image(current_file):
    if os.path.exists("customdata/images_with_labels/" + current_file.split('/')[-1]):
        return
    print(current_file)
    current_label_file = current_file.replace('images', 'labels').replace('r.jpg', 'cpos.txt')
    plt.figure()
    #fig, ax = plt.subplots(1, 1)
    img = np.array(Image.open(current_file))
    print(img.shape)
    plt.imshow(img)
    if os.path.exists(current_label_file):
        labels = np.loadtxt(current_label_file)
        for i in range(0, len(labels), 4):
            x1, y1 = labels[i, 0], labels[i, 1]
            x2, y2 = labels[i + 1, 0], labels[i + 1, 1]
            x3, y3 = labels[i + 2, 0], labels[i + 2, 1]
            x4, y4 = labels[i + 3, 0], labels[i + 3, 1]
            plt.plot([x1, x2], [y1, y2], 'r', linewidth=1)
            plt.plot([x2, x3], [y2, y3], 'b', linewidth=1)
            plt.plot([x3, x4], [y3, y4], 'r', linewidth=1)
            plt.plot([x4, x1], [y4, y1], 'b', linewidth=1)
    plt.axis("off")
    plt.gca().xaxis.set_major_locator(NullLocator())
    plt.gca().yaxis.set_major_locator(NullLocator())
    plt.savefig("customdata/images_with_labels/" + current_file.split('/')[-1], bbox_inches="tight", pad_inches=0.0)
    plt.close()


def load_image_to_scene(current_file):
    img = np.array(Image.open(current_file).resize((640, 480), Image.ANTIALIAS))
    frame = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
    pix = QPixmap.fromImage(frame)
    item = QGraphicsPixmapItem(pix)
    scene = QGraphicsScene()
    scene.addItem(item)
    return scene


class ImageSet:
    def __init__(self):
        self.height = 640
        self.width = 480
        self.image_file_list = []
        self.image_with_label_file_list = []
        self.has_marked = 0
        self.image_with_label_path = 'customdata/images_with_labels/'
        self.set_path = 'customdata/images/'

    def begin(self, ui):
        ui.graphicsView.pos = []
        self.image_file_list = os.listdir(self.set_path)
        if True:
            for i in range(len(self.image_file_list)):
                current_file = self.set_path + self.image_file_list[i]
                load_label_to_image(current_file)
        self.image_with_label_file_list = os.listdir(self.image_with_label_path)
        current_file = self.image_with_label_path + self.image_with_label_file_list[self.has_marked]
        ui.graphicsView.setScene(load_image_to_scene(current_file))
        ui.pushButton.setEnabled(False)
        ui.listView.clear()

    def piror(self, ui):
        ui.graphicsView.pos = []
        ui.graphicsView.temp_pos = []
        ui.graphicsView.clicked_cnt = 0
        ui.listView.clear()
        if len(self.image_with_label_file_list) == 0:
            QMessageBox.information(ui.widget, 'Warring', '请先点击开始按钮以开始标记')
        else:
            idx = (self.has_marked - 1 + len(self.image_with_label_file_list)) % len(self.image_with_label_file_list)
            current_file = self.image_with_label_path + self.image_with_label_file_list[idx]
            ui.graphicsView.setScene(load_image_to_scene(current_file))
            self.has_marked -= 1

    def next(self, ui):
        ui.listView.clear()
        ui.graphicsView.pos = []
        ui.graphicsView.temp_pos = []
        ui.graphicsView.clicked_cnt = 0
        if len(self.image_with_label_file_list) == 0:
            QMessageBox.information(ui.widget, 'Warring', '请先点击开始按钮以开始标记')
            pass
        else:
            idx = (self.has_marked + 1) % len(self.image_with_label_file_list)
            current_file = self.image_with_label_path + self.image_with_label_file_list[idx]
            ui.graphicsView.setScene(load_image_to_scene(current_file))
            self.has_marked += 1
