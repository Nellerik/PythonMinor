import os

for folderName, subfolders, filenames in os.walk('4\\FilesToRename'):
    ExpectedFileNum = 1
    for filename in filenames:
        if filename.startswith('prefix'):
            fileNum = int(filename.removeprefix('prefix').removesuffix('.txt'))
            if fileNum != ExpectedFileNum:
                os.rename(folderName + '\\' + filename, folderName + '\\' + 'prefix' + str(ExpectedFileNum).zfill(3) + '.txt')
        ExpectedFileNum += 1