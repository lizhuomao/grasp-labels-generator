import os
import numpy as np
import shutil

file_list = np.array(os.listdir('customdata/images/'))
one_list = file_list[:int(len(file_list) / 3)]
two_list = file_list[int(len(file_list) / 3) : int(2 * (len(file_list) / 3))]
three_list = file_list[int(2 * (len(file_list) / 3)) :]
for i in range(len(one_list)):
    shutil.move('customdata/images/' + one_list[i], 'customdata/images_1/' + one_list[i])

for i in range(len(two_list)):
    shutil.move('customdata/images/' + two_list[i], 'customdata/images_2/' + two_list[i])

for i in range(len(three_list)):
    shutil.move('customdata/images/' + three_list[i], 'customdata/images_3/' + three_list[i])
