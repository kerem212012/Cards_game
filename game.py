import random
import time


favn = {
    'Здоровье':3,
    'Сила':1
}
dvarf = {
    'Здоровье': 2,
    'Сила': 2
}
giant ={
    'Здоровье': 4,
    'Сила': 3
}
driad = {
    'Здоровье': 5,
    'Сила': 2
}
minotaur={
    'Здоровье': 9,
    'Сила': 6
}
cintaur ={
    'Здоровье': 7,
    'Сила': 8
}

favn1 = {
    'Здоровье':3,
    'Сила':1
}
dvarf1 = {
    'Здоровье': 2,
    'Сила': 2
}
giant1 ={
    'Здоровье': 4,
    'Сила': 3
}
driad1 = {
    'Здоровье': 5,
    'Сила': 2
}
minotaur1={
    'Здоровье': 9,
    'Сила': 6
}
cintaur1 ={
    'Здоровье': 7,
    'Сила': 8
}
cards1=[favn,dvarf,giant,driad,minotaur,cintaur]
cards2=[favn1,dvarf1,giant1,driad1,minotaur1,cintaur1]
cards_comp=[favn,dvarf,giant,driad,minotaur,cintaur]
playernum=[1,2]
num=random.choice(playernum)
tour =num
win =0
win1 =0
print('*' * 10, 'Игра таинственного торговца', '*' * 10)
print('Хотите играть с компьютером?')
ans1=input()
print('Хотите играть с игроком?')
if ans1=='Нет' or ans1=='нет':
    ans2 = input()
    win =1
if ans1 =='Да' or ans1 =='да':
    while win !=1:
        if len(cards1) == 0:
            print('Вы проиграли!')
            break
        if len(cards_comp) == 0:
            print('Вы выиграли!')
            break
        print('Ваши карты:')
        if favn in cards1:
            print('Фавн', favn)
        if dvarf in cards1:
            print('Гном', dvarf)
        if giant in cards1:
            print('Великан', giant)
        if driad in cards1:
            print('Дриада', driad)
        if minotaur in cards1:
            print('Минотавр', minotaur)
        if cintaur in cards1:
            print('Кентавр', cintaur)
        card = input('Ваш ход, какую карту выберете?')
        card_comp = random.choice(cards_comp)
        if card == 'Фавн' and favn in cards1:
            print('Ваша карта:', favn)
            card = favn
        elif card == 'Гном'and dvarf in cards1:
            print('Ваша карта:', dvarf)
            card = dvarf
        elif card == 'Великан'and giant in cards1:
            print('Ваша карта:', giant)
            card = giant
        elif card == 'Дриада'and driad in cards1:
            print('Ваша карта:', driad)
            card = driad
        elif card == 'Минотавр'and minotaur in cards1:
            print('Ваша карта:', minotaur)
            card = minotaur
        elif card == 'Кентавр'and cintaur in cards1:
            print('Ваша карта:', cintaur)
            card = cintaur
        time.sleep(1)
        print('Карта противника:', card_comp)
        while True:
            print('Вы атакуете!')
            time.sleep(2)
            if card['Сила'] >= card_comp['Здоровье']:
                print('Противник повержен!')
                cards_comp.remove(card_comp)
                break
            if card['Сила'] < card_comp['Здоровье']:
                print('Противник ранен ранены')
                card_comp['Здоровье'] = card_comp['Здоровье'] - card['Сила']
            print(card_comp)
            print('Ход противника!')
            time.sleep(2)
            if card_comp['Сила'] >= card['Здоровье']:
                print('Вы проиграли')
                cards1.remove(card)
                break
            elif card_comp['Сила'] < card['Здоровье']:
                print('Вы ранены ранен')
                card['Здоровье'] = card['Здоровье'] - card_comp['Сила']
                print(card)

if ans2 =='Да' or 'да':
    while win1 !=1:
        if len(cards1) == 0:
            print('Вы проиграли!')
            break
        if len(cards2) == 0:
            print('Вы выиграли!')
            break
        print('Карты первого игрока:')
        if favn in cards1:
            print('Фавн', favn)
        if dvarf in cards1:
            print('Гном', dvarf)
        if giant in cards1:
            print('Великан', giant)
        if driad in cards1:
            print('Дриада', driad)
        if minotaur in cards1:
            print('Минотавр', minotaur)
        if cintaur in cards1:
            print('Кентавр', cintaur)
        card = input('Ход первого игрока, какую карту выберете?')
        if card == 'Фавн' and favn in cards1:
            print('Ваша карта:', favn)
            card = favn
        elif card == 'Гном'and dvarf in cards1:
            print('Ваша карта:', dvarf)
            card = dvarf
        elif card == 'Великан'and giant in cards1:
            print('Ваша карта:', giant)
            card = giant
        elif card == 'Дриада'and driad in cards1:
            print('Ваша карта:', driad)
            card = driad
        elif card == 'Минотавр'and minotaur in cards1:
            print('Ваша карта:', minotaur)
            card = minotaur
        elif card == 'Кентавр'and cintaur in cards1:
            print('Ваша карта:', cintaur)
            card = cintaur
        print('Карты второго игрока:')
        if favn1 in cards2:
            print('Фавн', favn1)
        if dvarf1 in cards2:
            print('Гном', dvarf1)
        if giant1 in cards2:
            print('Великан', giant1)
        if driad1 in cards2:
            print('Дриада', driad1)
        if minotaur1 in cards2:
            print('Минотавр', minotaur1)
        if cintaur1 in cards2:
            print('Кентавр', cintaur1)
        card1 = input('Ход второго игрока, какую карту выберете?')
        if card1 == 'Фавн' and favn1 in cards2:
            print('Ваша карта:', favn1)
            card1 = favn1
        elif card1 == 'Гном' and dvarf1 in cards2:
            print('Ваша карта:', dvarf1)
            card1 = dvarf1
        elif card1 == 'Великан' and giant1 in cards2:
            print('Ваша карта:', giant1)
            card1 = giant1
        elif card1 == 'Дриада' and driad1 in cards2:
            print('Ваша карта:', driad1)
            card1 = driad1
        elif card1 == 'Минотавр' and minotaur1 in cards2:
            print('Ваша карта:', minotaur1)
            card1 = minotaur1
        elif card1 == 'Кентавр' and cintaur1 in cards2:
            print('Ваша карта:', cintaur1)
            card1 = cintaur1
        time.sleep(1)
        print('Карта противника:', card1)
        if tour ==1:
            while True:
                tour =2
                print('Вы атакуете!')
                time.sleep(2)
                if card['Сила'] >= card1['Здоровье']:
                    print('Противник повержен!')
                    cards2.remove(card1)
                    break
                if card['Сила'] < card1['Здоровье']:
                    print('Противник ранен ранены')
                    card1['Здоровье'] = card1['Здоровье'] - card['Сила']
                print(card1)
                print('Ход противника!')
                time.sleep(2)
                if card1['Сила'] >= card['Здоровье']:
                    print('Вы проиграли')
                    cards1.remove(card)
                    break
                elif card1['Сила'] < card['Здоровье']:
                    print('Вы ранены ранен')
                    card['Здоровье'] = card['Здоровье'] - card1['Сила']
                    print(card)
        elif tour==2:
            while True:
                tour = 1
                print('Ход противника!')
                time.sleep(2)
                if card1['Сила'] >= card['Здоровье']:
                    print('Вы проиграли')
                    cards1.remove(card)
                    break
                elif card1['Сила'] < card['Здоровье']:
                    print('Вы ранены ранен')
                    card['Здоровье'] = card['Здоровье'] - card1['Сила']
                    print(card)
                    print('Вы атакуете!')
                    time.sleep(2)
                if card['Сила'] >= card1['Здоровье']:
                    print('Противник повержен!')
                    cards2.remove(card1)
                    break
                if card['Сила'] < card1['Здоровье']:
                    print('Противник ранен ранены')
                    card1['Здоровье'] = card1['Здоровье'] - card['Сила']
                print(card1)