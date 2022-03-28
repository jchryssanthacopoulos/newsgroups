"""Preprocess into single zip file without reference to topics."""

import os
import random
import shutil
import tarfile


train_dir = os.path.join('20news-bydate', '20news-bydate-train')


topic_dirs = [drct for drct in os.listdir(train_dir) if not drct.startswith('.')]


files = []

for topic_dir in topic_dirs:
    topic_dir = os.path.join(train_dir, topic_dir)
    for file in os.listdir(topic_dir):
        files.append(os.path.join(topic_dir, file))


# randomize order
random.shuffle(files)


dest_dir = 'emails'

for idx, file in enumerate(files):
    shutil.copyfile(file, os.path.join(dest_dir, f'{(idx + 1):05}'))


# write tar file
file_name = 'emails.tar.gz'
with tarfile.open(file_name, "w:gz") as tar:
    tar.add(dest_dir)
