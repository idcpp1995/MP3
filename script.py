import shutil
import os
import argparse


def mp3_list(src_link):
    common_list = os.listdir(path=src_link)  # выгружаем все что есть в папке
    song_list = []
    for i in common_list:
        if i.endswith('.mp3'):  # сортируем по мп3 расширению
            song_list.append(i)
    return song_list


def new_folder(src_link2, src_link, dst_link):
    song_list = mp3_list(src_link)
    for i in song_list:
        shutil.move(src_link2 + i, dst_link)  # папка источник + *.mp3, папка назначения


parser = argparse.ArgumentParser()

parser.add_argument('src_link', type=str)

parser.add_argument('src_link2', type=str)
parser.add_argument('src_link', type=str)
parser.add_argument('dst_link', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    mp3_list(args.src_link)
    new_folder(args.src_link2, args.src_link, args.dst_link)

"""
mp3_list("C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/music")
new_folder("C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/music/", "C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/music/", "C:/Users/Dima/Downloads/py.projects/gitMP3/MP3/copy")
# python script.py C:/Users/Dima/Downloads/py.projects/mp3/music C:/Users/Dima/Downloads/py.projects/mp3/music/ C:/Users/Dima/Downloads/py.projects/mp3/music/ C:/Users/Dima/Downloads/py.projects/mp3/aaaaaaaaaa
"""