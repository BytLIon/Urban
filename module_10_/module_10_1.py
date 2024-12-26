#Введение в потоки"
import threading
from time import sleep, time



def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")



if __name__ == '__main__':

    start_time = time()

    write_words(10, 'ex_1.txt')
    write_words(30, 'ex_2.txt')
    write_words(200, 'ex_3.txt')
    write_words(100, 'ex_4.txt')

    end_time = time()

    print(f"Время работы функций: {end_time - start_time:.6f} секунд")

    threads = []
    start_time_threads = time()

    thread_args = [
        (10, 'ex_5.txt'),
        (30, 'ex_6.txt'),
        (200, 'ex_7.txt'),
        (100, 'ex_8.txt')
    ]

    for args in thread_args:
        thread = threading.Thread(target=write_words, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time_threads = time()
    print(f"Время работы потоков: {end_time_threads - start_time_threads:.6f} секунд")






