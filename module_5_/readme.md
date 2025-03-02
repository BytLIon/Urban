# Модуль 5. Классы и объекты  

## Классы и объекты — human_class  
Класс в Python — шаблон, по которому создаются объекты.  
Конструкцию ``def __init__`` — инициализатор, методе указывается, что будет создаваться при инициализации объекта.  
Объекты в Python существуют до тех пор, пока на них ссылается хотя бы одна ссылка.  
self — указателем на сам объект.  

## Атрибуты и методы объекта — module_5_1  
Атрибуты — переменные внутри класса.  
Методы — функции, определенные внутри него.  

## Специальные методы классов — module_5_2  
Для удаления объекта можно воспользоваться оператором ``__del__``, который активирует деструктор.  
Объектно-ориентированное программирование (ООП):  
- **Наследование** — этот принцип позволяет создавать новые классы на основе существующих, что даёт возможность расширять и изменять поведение базового класса, делая производные классы более уникальными.
- **Инкапсуляция** — позволяет скрывать внутренние детали реализации класса от пользователей, предоставляя доступ только к необходимым элементам. Это способствует более безопасной работе и предотвращает случайные ошибки.
- **Полиморфизм** — позволяет использовать объекты разных классов через единый интерфейс, что упрощает взаимодействие с ними и делает код более гибким.  

## Перегрузка операторов — module_5_3  
Метод ``__lt__()`` можно интерпретировать как «меньше чем» (Lower than).  
Метод ``__gt__()`` интерпретируется как «больше чем» (Greater than).  

## Различие атрибутов класса и экземпляра — module_5_4  
Класс Object является базовым классом всей иерархии классов.  
Метод ``__init__()`` вызывается после создания объекта класса и отвечает за присвоение уникальных характеристик каждому объекту.  
Метод ``__new__()`` вызывается перед созданием объекта класса.  
Функция super() позволяет вызывать методы родительского класса.  
Для реализации паттерна Singleton в классе создаётся специальный классовый атрибут '__instance = None', который будет хранить ссылку на единственный экземпляр класса.  

## Классы и объекты. Свой YouTube — module_5_hard  
Подобие YoyTube на классах.  

## Система регистрации на классах — pract_1-3_class  
Система регистрации на классах.  

