import os
import numpy as np

if not os.path.exists('cornell_labels/'):
    os.makedirs('cornell_labels')
files = os.listdir('new_labels')
for file in files:
    labels = np.loadtxt('new_labels/' + file)
    if labels.shape == (5,):
        labels = labels.reshape((1, 5))
    clabels = []
    for label in labels:
        x1, y1, x2, y2, w = label
        w /= 2
        flag = False
        if x1 < x2:
            flag = True
        if x2 == x1:
            if y2 > y1:
                ltx = x2 - w
                lty = y2
                rtx = x2 + w
                rty = y2
                lbx = x1 - w
                lby = y1
                rbx = x1 + w
                rby = y1
            else:
                ltx = x1 - w
                lty = y1
                rtx = x1 + w
                rty = y1
                lbx = x2 - w
                lby = y2
                rbx = x2 + w
                rby = y2
        elif y2 == y1:
            if flag:
                ltx = x1
                lty = y1 + w
                rtx = x1
                rty = y1 - w
                lbx = x2
                lby = y2 + w
                rbx = x2
                rby = y2 - w
            else:
                ltx = x2
                lty = y2 + w
                rtx = x2
                rty = y2 - w
                lbx = x1
                lby = y1 + w
                rbx = x1
                rby = y1 - w
        else:
            a = (y2 - y1) / (x2 - x1)
            k = -1 / a
            theta = np.arctan(k)
            if flag:
                ltx = x2 - w * np.cos(theta)
                lty = y2 - w * np.sin(theta)
                rtx = x2 + w * np.cos(theta)
                rty = y2 + w * np.sin(theta)
                lbx = x1 - w * np.cos(theta)
                lby = y1 - w * np.sin(theta)
                rbx = x1 + w * np.cos(theta)
                rby = y1 + w * np.sin(theta)
            else:
                ltx = x1 - w * np.cos(theta)
                lty = y1 - w * np.sin(theta)
                rtx = x1 + w * np.cos(theta)
                rty = y1 + w * np.sin(theta)
                lbx = x2 - w * np.cos(theta)
                lby = y2 - w * np.sin(theta)
                rbx = x2 + w * np.cos(theta)
                rby = y2 + w * np.sin(theta)
        clabels.append([ltx, lty])
        clabels.append([rtx, rty])
        clabels.append([rbx, rby])
        clabels.append([lbx, lby])
    np.savetxt('cornell_labels/' + file.replace('r.txt', 'cpos.txt'), clabels, fmt="%.2f")
