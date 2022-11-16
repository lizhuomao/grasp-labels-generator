import os
import random

# with open('valid.txt', 'r') as f:
#     d = f.readlines()
#
# r = []
# for l in d:
#     l.strip().strip('\n')
#     #r.append(l.replace('images', 'labels').replace('jpg', 'txt'))
#     r.append(l.replace('data/custom', 'customdata'))
#
# with open('valid.txt_t', 'w') as f:
#     f.writelines(r)

files = os.listdir('images/')

r_f = []
for f in files:
    r_f.append('customdata/images/' + f + '\n')
random.seed(27149)

random.shuffle(r_f)

pre = 0.8
end = int(len(r_f) * pre)

train_files = r_f[:end]
val_files = r_f[end:]
print(len(train_files))
print(len(val_files))
with open('train_new.txt', 'w') as f:
    f.writelines(train_files)
with open('valid_new.txt', 'w') as f:
    f.writelines(val_files)

