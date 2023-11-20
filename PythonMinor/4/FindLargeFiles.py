import os

for folderName, subfolders, filenames in os.walk('C:\\Program Files'):
    for filename in filenames:
        filesize = os.path.getsize(folderName + '\\' + filename) / (1024 * 1024)
        if filesize >= 100:
            print(str(int(filesize)) + 'mb FILE: ' + folderName + '\\' + filename)