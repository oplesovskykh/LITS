# -*- coding: utf-8 -*-
# coding=utf-8

print("Привіт! Введи своє ім\'я")
name = str(raw_input())
print("Вітаю в грі, " + name + "! Ти завжди вважав себе звичайнісінькою людиною, однак, зі всіми інколи трапляються пригоди")
print("Якось ти повертаєшся із своєї звичайнісінької роботи додому, а в тебе на дивані сидить чужинець, чоловік, середніх літ. \n Твоя реакція: \n "
      "1.Точно злодій. Шукаю щось важке під рукою і атакую\n 2.Хто ви, що ви тут робите?\n Обери відповідь 1 чи 2" )

answer1 = str(raw_input())
while answer1 == '1' or '2':
    if answer1 == '1':
        print("Чоловік направляє на тебе відкриту долонь. Невідома сила приковує тебе до стіни.\nПослухай мене - каже чоловік. Ти слухаєш, а що тобі ще лишається...")
        break
    elif answer1 == '2':
        print("Чоловік починає свою розповідь")
        break
    print("Обери відповідь")
    answer1 = str(raw_input())

print("Мене звуть Отто, я ювелір. В моїх руках з\'являються незвичайні речі, магічні. Я зробив багато добра для цього світу. Допомогав закоханим"
      "знайти шлях один до одного за допомогою магічних кілець. Захищав дітей кулонами, що їм дарували матері. Посилював воїнів золотими браслетами."
      "Але тепер допомога потрібна й мені самому.")
print("1.Так, звичайно, я готовий допомогти\n2.Не розумію, як це стосується мене. Я краще помру зараз, ніж прийматиму участь в таких квестах")

answer2 = str(raw_input())
while answer2 == '1' or '2':
    if answer2 =='1':
        print("Слухай далі. Колись я зробив магічний алмаз, що сцілить близьку мені людину. Але злий чаклун Копервольт викрав камінь і полонив ціле моє поселення."
              "З ним в бій вступив інший чаклун, але загинув в тому бою. Перед смертю він заповідав мені знайти людину, чисту серцем, і в жодному разі, не казати, для кого зроблений камінь."
              "Ти маєш відчути це, і віддати алмаз прямо їй, інакше сила втратиться, а людина ніколи не видужає")
        break
    elif answer2 == '2':
        print("Я не робитиму тобі лиха. Сумно, що в цьому світі не лишилось героїв. Прощавай назавди. Колись ти шкодуватимеш.")
        break
    print("Обери відповідь")
    answer2 = str(raw_input())

print("цю стрічку має бачити тільки той, хто вибрав 1")




