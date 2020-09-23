__author__ = 'Rafeusfox'

#Prepare dirs for data: split train, validation and test image data
import os, shutil

original_dataset_dir = r"PATH/TO/TRAIN/DATASET/DIR"
base_dir = r"PATH/TO/BASE/DIR"
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

train_first_class_images_dir = os.path.join(train_dir, 'first_class_images')
os.mkdir(train_first_class_images_dir)

train_second_class_images_dir = os.path.join(train_dir, 'second_class_images')
os.mkdir(train_second_class_images_dir)

validation_first_class_dir = os.path.join(validation_dir, 'first_class')
os.mkdir(validation_first_class_dir)

validation_second_class_dir = os.path.join(validation_dir, 'second_class')
os.mkdir(validation_second_class_dir)

test_first_class_dir = os.path.join(test_dir, 'first_class')
os.mkdir(test_first_class_dir)
test_second_class_dir = os.path.join(test_dir, 'second_class')
os.mkdir(test_second_class_dir)

fnames = ['first_class_name.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_first_class_images_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['first_class_name.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_first_class_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['first_class_name.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_first_class_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['second_class_name.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_second_class_images_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['second_class_name.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_second_class_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['second_class_name.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_second_class_dir, fname)
    shutil.copyfile(src, dst)

print('total training first_class images:', len(os.listdir(train_first_class_images_dir)))
print('total training second_class images:', len(os.listdir(train_second_class_images_dir)))
print('total validation first_class images:', len(os.listdir(validation_first_class_dir)))
print('total validation second_class images:', len(os.listdir(validation_second_class_dir)))
print('total test first_class images:', len(os.listdir(test_first_class_dir)))
print('total test second_class images:', len(os.listdir(test_second_class_dir)))

