from random import randint


def attack(name, char_class):
    if char_class == 'warrior':
        return (f'{name} нанёс урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{name} нанёс урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{name} нанёс урон противнику равный {5 + randint(-3, -1)}')
def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{name} блокировал {10 + randint(2, 5)} урона')
def special(name, char_class):
    if char_class == 'warrior': 
        return (f'{name} применил специальное умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{name} применил специальное умение «Защита {10 + 30}»')




def start_training(name, char_class):
    if char_class == 'warrior':
        print(f'{name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence — чтобы блокировать атаку противника или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(name, char_class))
        if cmd == 'defence':
            print(defence(name, char_class))
        if cmd == 'special':
            print(special(name, char_class))
    return 'Тренировка окончена.'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    name = input('...назови себя: ')
    print(f'Здравствуй, {name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(name, char_class))
    

main()