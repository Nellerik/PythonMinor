#! python3
#-*- coding: cp1251 -*-
import re

pattern = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
keywords = {
    'ADJECTIVE':'прилагательное',
    'NOUN':'существительное',
    'ADVERB':'наречие',
    'VERB':'глагол'
    }

File = open("text.txt", "r")
fileText = File.read()

for match in re.finditer(pattern, fileText):
    print('Введите %s:' % (keywords[match.group()]))
    userResp = input()
    fileText = re.sub(match.group(), userResp, fileText, 1)
    
txtFile = open("text.txt", "w")
txtFile.write(fileText)
txtFile.close()