#! python3
#-*- coding: cp1251 -*-
import random

capitals = {
	'���������':'��������',
	'�������':'����',
	'�����������':'����',
	'�������':'������',
	'�����':'�����',
	'������':'������',
	'�������':'�������-��-�����',
	'���������':'������-�����',
	'�������':'������',
	'��������':'�����',
	'�������':'��������',
	'��������':'�����',
	'�������':'��-���',
	'��������':'��������',
	'��������������':'������',
	'�������':'��������',
	'�������':'�����',
	'��������':'������',
	'������':'�����',
	'������':'�������',
	'�����':'����������',
	'������':'����',
	'�������':'���������',
	'�����':'���-����',
	'���������':'��������',
	'����':'�������',
	'��������':'������',
	'��������':'���������',
	'�������':'������',
	'������':'���',
	'���������':'���-������(������)',
	'������':'������',
	'�����':'�����',
	'��������':'������',
	'�����(�����)':'����',
	'����':'������',
	'������':'����',
	'�����':'������',
	'�����':'�������',
	'����������':'����������',
	'�������':'������',
	'�������':'�������',
	'��������':'����-�����',
	'����������':'���������',
	'��������':'����',
	'��������':'���������',
	'����':'����',
	'������':'�������',
	'����������':'��������',
	'������':'������'
    }

for quizNum in range(35):
    quizFile = open("Tests\capitalsquiz%s.txt" % (quizNum + 1), 'w')
    answerKeyFile = open("Tests\capitalsquiz_answers%s.txt" % (quizNum + 1), 'w')
    quizFile.write('���:\n\n����:\n\n����:\n\n')
    quizFile.write((' ' * 15) + '�������� ������ ������ ����� (����� %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    countries = list(capitals.keys())
    random.shuffle(countries)
    
    for questionNum in range(50):
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s. �������� ������� ������ %s.\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' %('ABCD'[i], answerOptions[i]))
            
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()