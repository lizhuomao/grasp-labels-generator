import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
from matplotlib.ticker import NullLocator

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QMessageBox

from util.load_image import load_image_to_scene


def load_convert_labels_to_image(current_file):
    if os.path.exists('customdata/images_with_convert_labels/' + current_file):
        return
    current_label_file = current_file.replace('r.jpg', 'cpos.txt')
    plt.figure()
    img = np.array(Image.open('customdata/images/' + current_file))
    plt.imshow(img)
    if os.path.exists('customdata/cornell_labels/' + current_label_file):
        labels = np.array(np.loadtxt('customdata/cornell_labels/' + current_label_file))
        for i in range(0, len(labels), 4):
            x1, y1 = labels[i]
            x2, y2 = labels[i + 1]
            x3, y3 = labels[i + 2]
            x4, y4 = labels[i + 3]
            plt.plot([x1, x2], [y1, y2], 'r', linewidth=1)
            plt.plot([x2, x3], [y2, y3], 'b', linewidth=1)
            plt.plot([x3, x4], [y3, y4], 'r', linewidth=1)
            plt.plot([x4, x1], [y4, y1], 'b', linewidth=1)

    plt.axis('off')
    plt.gca().xaxis.set_major_locator(NullLocator())
    plt.gca().yaxis.set_major_locator(NullLocator())
    plt.savefig("customdata/images_with_convert_labels/" + current_file, bbox_inches="tight", pad_inches=0.0)
    plt.close()


def load_labels_to_image(current_file):
    if os.path.exists('customdata/images_with_labels_new/' + current_file):
        return
    current_label_file = current_file.replace('r.jpg', 'r.txt')
    plt.figure()
    img = np.array(Image.open('customdata/images/' + current_file))
    plt.imshow(img)
    if os.path.exists('customdata/new_labels/' + current_label_file):
        labels = np.array(np.loadtxt('customdata/new_labels/' + current_label_file))
        if len(labels.shape) == 1:
            labels = labels.reshape((1, 5))
        for i in range(0, len(labels)):
            x1, y1, x2, y2, w = labels[i]
            w /= 2
            if x2 == x1:
                y3 = (y2 + y1) / 2
                x3 = x1 + w
                y4 = y3
                x4 = x1 - w
            elif y2 == y1:
                x3 = (x2 + x1) / 2
                y3 = y1 + w
                x4 = (x2 + x1) / 2
                y4 = y1 - w
            else:
                a = (y2 - y1) / (x2 - x1)
                k = -1 / a
                theta = np.arctan(k)
                x3 = ((x1 + x2) / 2) + w * np.cos(theta)
                y3 = ((y1 + y2) / 2) + w * np.sin(theta)
                x4 = ((x1 + x2) / 2) - w * np.cos(theta)
                y4 = ((y1 + y2) / 2) - w * np.sin(theta)
            plt.plot([x1, x2], [y1, y2], 'r', linewidth=1)
            plt.plot([x3, x4], [y3, y4], 'b', linewidth=1)

    plt.axis('off')
    plt.gca().xaxis.set_major_locator(NullLocator())
    plt.gca().yaxis.set_major_locator(NullLocator())
    plt.savefig("customdata/images_with_labels_new/" + current_file, bbox_inches="tight", pad_inches=0.0)
    plt.close()


class CImageset:
    def __init__(self):
        self.image_file_list_old = []
        self.image_file_list_new = []
        self.has_compared = 0
        self.image_file_path_old = 'customdata/images_with_labels/'
        # self.image_file_path_new = 'customdata/images_with_labels_new/'
        self.image_file_path_new = 'customdata/images_with_convert_labels/'

    def save_labeled_num(self):
        np.savetxt('util/c_labeled_num.txt', np.array([self.has_compared]))

    def load_labeled_num(self):
        if not os.path.exists('util/c_labeled_num.txt'):
            return
        self.has_compared = int(np.loadtxt('util/c_labeled_num.txt'))

    def begin(self, ui):
        self.save_labeled_num()
        self.image_file_list_old = os.listdir(self.image_file_path_old)
        if not os.path.exists(self.image_file_path_new):
            os.makedirs(self.image_file_path_new)
        for file in self.image_file_list_old:
            if not os.path.exists(self.image_file_path_new + file):
                print(file)
                load_convert_labels_to_image(file)
        self.image_file_list_new = os.listdir(self.image_file_path_new)
        ui.graphicsView.setScene(load_image_to_scene(
            self.image_file_path_old +
            self.image_file_list_old[self.has_compared]))
        ui.graphicsView_2.setScene(load_image_to_scene(
            self.image_file_path_new +
            self.image_file_list_new[self.has_compared]))
        ui.pushButton_2.setEnabled(False)

    def prior(self, ui):
        if len(self.image_file_list_new) == 0:
            QMessageBox.information(ui.widget, 'Warring', '请先点击开始按钮以开始标记')
        else:
            idx = (self.has_compared - 1 + len(self.image_file_list_old) * 2) % len(self.image_file_list_old)
            old_file = self.image_file_path_old + self.image_file_list_old[idx]
            new_file = self.image_file_path_new + self.image_file_list_new[idx]
            ui.graphicsView.setScene(load_image_to_scene(old_file))
            ui.graphicsView_2.setScene(load_image_to_scene(new_file))
            self.has_compared -= 1
            self.save_labeled_num()

    def next(self, ui):
        if len(self.image_file_list_new) == 0:
            QMessageBox.information(ui.widget, 'Warring', '请先点击开始按钮以开始标记')
        else:
            idx = (self.has_compared + 1 + len(self.image_file_list_old) * 2) % len(self.image_file_list_old)
            old_file = self.image_file_path_old + self.image_file_list_old[idx]
            new_file = self.image_file_path_new + self.image_file_list_new[idx]
            ui.graphicsView.setScene(load_image_to_scene(old_file))
            ui.graphicsView_2.setScene(load_image_to_scene(new_file))
            self.has_compared += 1
            self.save_labeled_num()

    def need_relabel(self, ui):
        if len(self.image_file_list_new) == 0:
            QMessageBox.information(ui.widget, 'Warring', '请先点击开始按钮以开始标记')
        else:
            new_file = self.image_file_path_old + self.image_file_list_old[self.has_compared]
            with open('customdata/need_relabel.txt', 'a') as f:
                f.write(new_file + '\n')
