#! python3
#-*- coding: cp1251 -*-
import random

capitals = {
	'Австралия':'Канберра',
	'Австрия':'Вена',
	'Азербайджан':'Баку',
	'Албания':'Тирана',
	'Алжир':'Алжир',
	'Ангола':'Луанда',
	'Андорра':'Андорра-ла-Велья',
	'Аргентина':'Буэнос-Айрес',
	'Армения':'Ереван',
	'Беларусь':'Минск',
	'Бельгия':'Брюссель',
	'Болгария':'София',
	'Боливия':'Ла-Пас',
	'Бразилия':'Бразилиа',
	'Великобритания':'Лондон',
	'Венгрия':'Будапешт',
	'Вьетнам':'Ханой',
	'Германия':'Берлин',
	'Греция':'Афины',
	'Грузия':'Тбилиси',
	'Дания':'Копенгаген',
	'Египет':'Каир',
	'Израиль':'Иерусалим',
	'Индия':'Нью-Дели',
	'Индонезия':'Джакарта',
	'Иран':'Тегеран',
	'Ирландия':'Дублин',
	'Исландия':'Рейкьявик',
	'Испания':'Мадрид',
	'Италия':'Рим',
	'Казахстан':'Нур-Султан(Астана)',
	'Канада':'Оттава',
	'Китай':'Пекин',
	'Колумбия':'Богота',
	'Корея(Южная)':'Сеул',
	'Куба':'Гавана',
	'Латвия':'Рига',
	'Ливан':'Бейрут',
	'Литва':'Вильнюс',
	'Люксембург':'Люксембург',
	'Мексика':'Мехико',
	'Молдова':'Кишинев',
	'Монголия':'Улан-Батор',
	'Нидерланды':'Амстердам',
	'Норвегия':'Осло',
	'Пакистан':'Исламабад',
	'Перу':'Лима',
	'Польша':'Варшава',
	'Португалия':'Лиссабон',
	'Россия':'Москва'
    }

for quizNum in range(35):
    quizFile = open("Tests\capitalsquiz%s.txt" % (quizNum + 1), 'w')
    answerKeyFile = open("Tests\capitalsquiz_answers%s.txt" % (quizNum + 1), 'w')
    quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quizFile.write((' ' * 15) + 'Проверка знаний столиц стран (Билет %s)' % (quizNum + 1))
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
        quizFile.write('%s. Выберите столицу страны %s.\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' %('ABCD'[i], answerOptions[i]))
            
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()