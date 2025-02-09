# Модуль 10. Мультипоточность  

## Введение в потоки — module_10_1  
Процесс — экземпляр программы, запущен и выполняется операционной системой.  
Каждый процесс может иметь один или несколько потоков, работают параллельно.
Потоки работают с общим состоянием и памятью родительского процесса.  
В Python для работы с потоками можно использовать модуль threading, предоставляет все необходимые средства для создания и управления потоками.  
Функцией ``current_thread()`` вернёт объект потока, и в случае с основным потоком результатом будет ‘MainThread’.  
Функцию ``enumerate()`` возвращает список всех активных потоков в программе.  
Для создания потока существует два способа:
1) Создание потока с использованием класса Thread и функции: это самый простой и часто используемый способ. Здесь для создания потока используется класс Thread из модуля threading, и в качестве задачи потока передается функция, которую нужно выполнить.  
2) Создание потока через наследование класса Thread: в этом случае создается собственный класс, наследующий от Thread, и переопределяется метод ‘run()’, который будет выполняться в потоке.  
Метод start() запускает созданный поток.
Метод is_alive() позволяет определить, активен ли поток в данный момент, то есть выполняет ли он ещё какие-то задачи.
Метод join() Главный поток создает вспомогательный, запускает его и приостанавливается, ожидая завершения работы вспомогательного потока.
Потоки-демоны работают в фоновом режиме и автоматически завершаются, как только завершатся все основные потоки программы.

## Потоки на классах — module_10_2  
Создадим класс MyThread(threading.Thread).  
Необходимо переопределить метод run().  
Часто возникает необходимость передать в объект класса-потока определенные параметры.  
Сделать это можно двумя способами:
1) Использование функции super().
2) Прямой вызов конструктора родительского класса.

## Блокировки и обработка ошибок — module_10_3  
Проблема под названием «deadlock». 2 потока могут бесконечно ожидать друг от друга снятия блокировки.  
Для работы с замком нужно создать объект «lock» из модуля «threading» и в нужных местах блокировать или разблокировать его.  

## Очереди для обмена данными между потоками — module_10_4  
GIL (Global Interpreter Lock) — глобальная блокировка интерпретатора.  
GIL не блокирует операции, не связанные с непосредственной обработкой Python-кода, такие, как запись данных на диск или ожидание ответа от сервера.  
Для работы с очередью достаточно импортировать из встроенного модуля «queue» класс «queue».  

# Многопроцессность  

## Многопроцессное программирование — module_10_5  

