# -*-coding: utf-8 -*-


import os
import shutil

def create():
    """Создать файл"""
    print('Что хотите создать:\n1 - файл\n2 - директорию')
    try:
        choise = int(input('Ваш выбор: '))
        name = input('Укажите название: ')

        if choise == 1:
            with open(name, 'w') as f:
                print(f'Файл {name} создан.')
        elif choise == 2:
            os.makedirs(name)
            print(f'Директория {name} создана.')
        else:
            print('Ничего не выброно')

    except ValueError:
        print('Необходимо ввести число из меню выбора')


def delete():
    """Удалить директорию / файл"""
    src = input('Введите файл / директорию, которые хотите удалить: ')
    if os.path.isdir(src):
        os.removedirs(src)
        print(f'Директория {src} удалена')
    elif os.path.isfile(src):
        os.remove(src)
        print(f'Файл {src} удален')


def move():
    """Переместить файл"""
    dst = input('Введите новое название / директорию (если хотите переместить в конце укажите "/"): ')
    src = input('Введите файл, который хотите переместить: ')

    if src != '' and dst != '':
        try:
            shutil.move(src, dst)
            print(f'Файл {src} успешно перемещен')

        except FileNotFoundError:
            print(f'Директории назначения {dst} не существует.')
            print(f'Директоия {dst} будет создана.')
            os.makedirs(dst)
            shutil.move(src, dst)
            print(f'Файл {src} перемещен')
    else:
        print('Файл / директоря не указаны.')


def copy():
    """Копировать файл"""
    src = input('Укажите имя копируемого файла: ')
    dst = input('Укажите куда скопировать файл: ')
    if src != '' and dst != '':
        try:
            shutil.copy2(src, dst)

        except FileNotFoundError:
            dirs = os.path.dirname(dst)
            print(f'Директории назначения {dst} не существует.')
            print(f'Директоия {dirs} будет создана.')
            os.makedirs(dirs)
            shutil.copy2(src, dst)
            print(f'Файл {dst} скопирован')
    else:
        print('Файл / директоря не указаны.')


def change_dir():
    """Перейти в другую директорию"""
    set_path = input('Введите директорию для перехода: ')
    if set_path != '':
        try:
            os.chdir(set_path)
            print(f'Вы успешно перешли в директорию {os.getcwd()}')
        except FileNotFoundError:
            print('Такой диретории не существует.')
    else:
        print('Директория назначения не указана.')


def now_path():
    """Где сейчас"""
    print(os.getcwd())


def cls():
    # очистка консоли
    os.system('cls' if os.name=='nt' else 'clear')


def main():
    menu_list = [
            '1. Создать файл / директорию',
            '2. Удалить файл',
            '3. Переместить файл',
            '4. Копировать файл',
            '5. Перейти в другую директорию',
            '6. Выход'
            ]
    menu = {
            1: create,
            2: delete,
            3: move,
            4: copy,
            5: change_dir,
            }
    while True:
        for i in menu_list:
            print(i)

        print(f'Текущая директория: {os.getcwd()}')
        try:
            action = int(input('Введите желаемое действие (укажите цифру меню): '))
        except ValueError:
            print("Необходимо ввести число пункта меню.")
            input('Нажмите Enter чтобы продолжить.')
            cls()
            continue

        if action in menu:
            menu[action]()
        elif action == 6:
            break
        else:
            print("Указанного пункта нет в меню.")

        print()
        input('Нажмите Enter чтобы продолжить.')
        cls()

if __name__ == '__main__':
    main()
