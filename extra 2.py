import os
from collections import Counter
import string
def compare_by_second(point):
    return point[1]

def counterofwordz(filename):
    # Проверка наличия файла в текущей директории
    if not os.path.isfile(filename):
        print(f"Файл {filename} не найден.")
        return
    
    # Считывание содержимого файла
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text = text.lower()
    text = text.replace(",","")
    text = text.replace(".","")
    text = text.replace("!","")
    text = text.replace("?","")
    words = text.split()
    #считаем, кол-во вхождений
    count_each_word = Counter(words)
    
    ovrl = []
    for i,j in count_each_word.items():
        ovrl.append([i,j])
    
    ovrl = sorted(ovrl,key=compare_by_second)
    print(ovrl[::-1])
    

# Пример использования функции
filename = "example.txt"
counterofwordz(filename)