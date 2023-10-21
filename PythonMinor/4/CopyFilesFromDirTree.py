import shutil
import os
import string

for folderName, subfolders, filenames in os.walk('4\\DirTree1'):
    for filename in filenames:
        if filename.endswith('.txt'):
            shutil.copy(folderName + '\\' + filename, '4\\FilesCopies')