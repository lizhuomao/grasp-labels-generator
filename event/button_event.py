import os
import numpy as np
from util.load_image import load_image_to_scene


def add_new_labels(ui, img_set):
    labels = np.around(np.array(ui.graphicsView.pos), 2)
    if not os.path.exists('customdata/new_labels'):
        os.makedirs('customdata/new_labels')
    current_file = 'customdata/new_labels/' + 'pcd%04d' % (100 + img_set.has_marked) + 'r.txt'
    np.savetxt(current_file, labels, fmt="%.2f")
    print("success save labels in {}".format(current_file))


def delete_labels(ui, img_set):
    ui.graphicsView.pos = []
    ui.graphicsView.temp_pos = []
    scene = load_image_to_scene(
        'customdata/images_with_labels/' + 'pcd%04d' % (100 + img_set.has_marked) + 'r.jpg')
    ui.graphicsView.setScene(scene)
    ui.listView.clear()
