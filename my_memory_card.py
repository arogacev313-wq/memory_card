from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout ,QRadioButton, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    


#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(300, 250)
main_win.setWindowTitle('Memory Card')

#создание виджетов главного окна
answer = QPushButton('Ответить')

question = QLabel('Вопрос, Пример')
RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('Вариант 1')
btn_answer2 = QRadioButton('Вариант 2')
btn_answer3 = QRadioButton('Вариант 3')
btn_answer4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
true_answer = QLabel('Правильный ответ')

layout_res = QVBoxLayout()

layout_res.addWidget(result)
layout_res.addWidget(true_answer)

AnsGroupBox.setLayout(layout_res)

AnsGroupBox.hide()
RadioGroupBox.show()

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnsGroupBox)
layout_main.addWidget(answer, stretch = 1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    true_answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
    

def show_correct(text):
    result.setText(text)
    show_result()

def next_question():
    main_win.total += 1
    print('Статистика:', main_win.total,'Правильных ответов:', main_win.score, 'Рейтинг:', (main_win.total/main_win.score)*100, '%')
    qur_question = randint(0, len(qu)-1)
    q = qu[qur_question]
    ask(q)

def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

qu = list()

qu.append(Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'changing', 'variant'))
qu.append(Question('Выбери перевод слова "цикл"', 'loop', 'line', 'list', 'logic'))
qu.append(Question('Выбери перевод слова "функция"', 'function', 'formula', 'fraction', 'future'))
qu.append(Question('Выбери перевод слова "условие"', 'condition', 'connection', 'construction', 'collection'))
qu.append(Question('Какой национальный язык США?', 'Английский', 'Официального национального языка нет', 'Испанский', 'Французский'))
qu.append(Question('Столица Франции?', 'Париж', 'Марсель', 'Лион', 'Ницца'))
qu.append(Question('Какая страна известна пирамидами?', 'Египет', 'Италия', 'Греция', 'Индия'))
qu.append(Question('Какой язык является официальным в Бразилии?', 'Португальский', 'Испанский', 'Английский', 'Французский'))
qu.append(Question('Столица Японии?', 'Токио', 'Киото', 'Осака', 'Пекин'))
qu.append(Question('Какой язык является официальным в Германии?', 'Немецкий', 'Английский', 'Французский', 'Польский'))
qu.append(Question('Какая самая большая страна по площади?', 'Россия', 'Канада', 'США', 'Китай'))
qu.append(Question('Столица Канады?', 'Оттава', 'Торонто', 'Ванкувер', 'Монреаль'))
qu.append(Question('На каком континенте находится Австралия?', 'Австралия', 'Азия', 'Европа', 'Африка'))
qu.append(Question('Какой язык является официальным в Мексике?', 'Испанский', 'Английский', 'Португальский', 'Итальянский'))
qu.append(Question('Столица Италии?', 'Рим', 'Милан', 'Венеция', 'Неаполь'))
qu.append(Question('Какая валюта используется в Японии?', 'Иена', 'Юань', 'Вона', 'Доллар'))
qu.append(Question('Какая река самая длинная в мире?', 'Нил', 'Амазонка', 'Волга', 'Миссисипи'))
qu.append(Question('Какой океан самый большой?', 'Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый'))
qu.append(Question('Столица Казахстана?', 'Астана', 'Алматы', 'Шымкент', 'Караганда'))

main_win.total=0
main_win.score=0
answer.clicked.connect(click_ok)
main_win.setLayout(layout_main)
main_win.show()
app.exec_()