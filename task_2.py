# Завдання 2
# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям
# та перевіряє наявність рядка «Wow!». Якщо файлу немає, то засипає на 5 секунд,
# а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!».
# За наявності цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію
# і у разі її виникнення виконує видалення цього файлу. Якщо рядки «Wow!» не було знайдено у файлі,
# то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.


import threading
import time
import os

file_ready_event = threading.Event()
PATH = os.path.abspath(__file__ + '/..')

def search_wow(PATH:str, file_name: str):
    while True:
        if os.path.exists(os.path.join(PATH, file_name)):
            with open(os.path.join(PATH, file_name), 'r') as f:
                content = f.read()
                if "Wow!" in content:
                    print("Рядок 'Wow!' знайдено у файлі!")
                    file_ready_event.set()
                    return
            print("Рядок 'Wow!' не знайдено, перевіряю знову через 5 секунд...")
            time.sleep(5)
        else:
            print("Файл не знайдено, очікую 5 секунд...")
            time.sleep(5)

def delete_file(PATH:str, file_name: str):
    file_ready_event.wait()
    if os.path.exists(os.path.join(PATH, file_name)):
        os.remove(file_name)
        print("Файл видалено.")

def create_file(PATH:str, file_name: str):
    with open(os.path.join(PATH, file_name), 'w') as f:
        f.write("Перевіряємо файл...")
    print("Файл створено без рядка 'Wow!'")
    time.sleep(20)
    with open(os.path.join(PATH, file_name), 'a') as f:
        f.write("\nWow!")
    print("Рядок 'Wow!' додано у файл через 20 секунд!")

file_name = "test_file.txt"

thread1 = threading.Thread(target=search_wow, args=(PATH, file_name,))
thread2 = threading.Thread(target=delete_file, args=(PATH, file_name,))
thread3 = threading.Thread(target=create_file, args=(PATH, file_name,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Всі потоки завершено!")
