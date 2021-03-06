# Python Learning.
---

## Задачи:

__1.__ Создать класс с именем `Toy`. В методе `__init__` должны быть свойства `name` - имя игрушки. И `year` - дата покупки игрушки.  И создать методы `play` и `sleep`. Метод `sleep` - выводит на экран `Я иду спать`. Метод `play` - выводит на экран `Я играюсь с игрушкой под именем {name_of_toy}`. А так же, создать метод `year_of_toy` - который возвращает дату создания/покупки игрушки.

__2.__ Найти сумму чисел от `a` до `b` включительно на двух отрезках. `a` и `b` вводятся с клавиатуры

__3.__ Реализуйте справочник столиц стран. На вход программе поступают следующие запросы:

* __CHANGE_CAPITAL__ country new_capital — изменение столицы страны country на new_capital, либо добавление такой страны с такой столицей, если раньше её не было.

* __RENAME__ old_country_name new_country_name — переименование страны из old_country_name в new_country_name.

* __ABOUT__ country — вывод столицы страны country.
     
* __DUMP__ — вывод столиц всех стран.

     * __Формат ввода__
* В первой строке содержится количество запросов Q, в следующих Q строках — описания запросов. Все названия стран и столиц состоят лишь из латинских букв, цифр и символов подчёркивания.

__Формат вывода__
__Выведите результат обработки каждого запроса:__

* В ответ на запрос __CHANGE_CAPITAL__ country new_capital выведите
    * __Introduce new country country with capital new_capital__, если страны country раньше не существовало;

    * __Country country hasn't changed its capital__, если страна country до текущего момента имела столицу new_capital;
    * __Country country has changed its capital from old_capital to new_capital__, если страна country до текущего момента имела столицу old_capital, название которой не совпадает с названием new_capital.

* В ответ на запрос __RENAME old_country_name new_country_name__ выведите
    * __Incorrect rename, skip__, если новое название страны совпадает со старым, страна old_country_name не существует или страна new_country_name уже существует;
    * __Country old_country_name with capital capital has been renamed to new_country_name__, если запрос корректен и страна имеет столицу capital.

* В ответ на запрос __ABOUT__ country выведите
    * __Country country doesn't exist__, если страны с названием country не существует;
    * __Country country has capital capital__, если страна country существует и имеет столицу capital.
* В ответ на запрос __DUMP__ выведите
    * __There are no countries in the world__, если пока не было добавлено ни одной страны;

Последовательность пар вида country/capital, описывающую столицы всех стран, если в мире уже есть хотя бы одна страна. При выводе последовательности пары указанного вида необходимо упорядочить по названию страны и разделять между собой пробелом.



## Основы GIT

- ```git init``` - инициализация репозитория. Делается всего лишь один раз для каждого репозитория.
- ```git add [name_of_file]``` - добавить файл в commit
- ```git add .``` - добавить все файлы в commit
- ```git commit -m "Your_comment"``` - закомитить изменения и добавить свой комментарий на место "Your_comment"
- ```git push -u origin master``` - залить изменения на github
