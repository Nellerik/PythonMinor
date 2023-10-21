#-*- coding: cp1251 -*-
import re

pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
keywords = {
    'ADJECTIVE':'прилагательное',
    'NOUN':'существительное',
    'ADVERB':'наречие',
    'VERB':'глагол'
    }

file = open("text.txt", "r")

fileStr = file.read()
matches = re.finditer(pattern, fileStr)

for match in matches:
    print('Введите %s:' % (keywords[match.group()]))
    userResp = input()
    fileStr = re.sub(match.group(), userResp, fileStr, 1)
    
file.close()
file = open("text.txt", "w")
file.write(fileStr)
file.close()