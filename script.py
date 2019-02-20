import shutil
import os
import argparse
import re

def new_folder(src_link, dst_link):
    common_list = os.listdir(path=src_link)  # выгружаем все что есть в папке-источнике
    dst_folder = os.listdir(path=dst_link)  # выгружаем все что есть в папке-приемнике
    song_list = []  # все mp3 файлы папки-источника

    copy_counter = 0  # счетчик копий
    final_list_counter = 0  # счетчик уникальных mp3

    for i in common_list:
        if re.search(r'копія', i):  # проверка на копии
            path = os.path.join(os.path.abspath(os.path.dirname(src_link)), i)
            os.remove(path)  # delete копий
            copy_counter += 1
        elif i.endswith('.mp3'):  # сортируем по мп3 расширению
            song_list.append(i)
    for i in common_list:  # удаляет дубликаты из папки-источника, если такие уже есть в папке-приемнике
        for j in dst_folder:
            if i == j:
                path2 = os.path.join(os.path.abspath(os.path.dirname(src_link)), j)
                os.remove(path2)
    print("Копий удалено в размере: " + str(copy_counter))

    a = os.listdir(path=src_link)
    final_list = []  # список mp3 файлов папки-источника без копий и дубликатов в папке-приемнике
    for i in a:
        if i.endswith('.mp3'):
            final_list.append(i)
            final_list_counter += 1
    print("Файлов скопировано в размере: " + str(final_list_counter))

    if os.path.exists(dst_link):  # проверка на наявность папки-приемника
        for i in final_list:
            shutil.move(src_link + i, dst_link)  # папка источник + *.mp3, папка назначения
    else:  # создание папки-приемника
        print("Вы указали несуществующее место назначения \n")
        yes_no = input("Желаете создать папку ?(y/n): ")
        if yes_no == 'y':
            newdir = input("Введите адрес для новой папки: ")
            os.makedirs(newdir)
            for i in final_list:
                shutil.move(src_link + i, newdir)
        else:
            print("End")

parser = argparse.ArgumentParser()

parser.add_argument('src_link', type=str)
parser.add_argument('dst_link', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        new_folder(args.src_link, args.dst_link)
    except FileNotFoundError:
        print("Вы указали неверный источник \nEnd")

"""
пример парса 
python script.py C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/music/ C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/copy/
"""