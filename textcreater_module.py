import os
from os import path

def textcreater(str):
    if path.exists ('file.txt') :
        text_file_delete ( )
        textcreater(str)
    else:
        f = open('file.txt', 'w+')
        for i in str:
            f.write(i)
        f.close()

def text_file_delete():
    os.remove('file.txt')