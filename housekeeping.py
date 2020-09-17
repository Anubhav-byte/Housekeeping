import os
import shutil
import re

target_path='D:\\auto_test'

os.chdir(target_path)

pdf_path= os.path.join(target_path, 'pdf')

txt_path= os.path.join(target_path, 'txt')

os.makedirs(pdf_path)

os.makedirs(txt_path)

files=os.listdir(target_path)

pdf="^.+\.([pP][dD][fF])$"

txt='^.+\.([tT][xX][tT])$'

for file in files:

    if file== 'pdf' or file== 'txt':

        continue

    if re.match(pdf , file):

        shutil.move(file , pdf_path)

    else:

        if re.match(txt , file):

            shutil.move(file  , txt_path)
