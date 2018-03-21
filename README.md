# Ближайшие бары

На сайте [data.mos.ru](https://data.mos.ru/) есть много разных данных, в том числе список московских баров. 
Его можно скачать в формате JSON. Для этого нужно:

	1. зарегистрироваться на сайте и получить ключ API;
	2. скачать файл по ссылке вида ```https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.```

А можно не тратить на это время и воспользоваться [ранее скачанным файлом](https://devman.org/fshare/1503831681/4/).

Скрип покажет:

* самый большой бар;
* самый маленький бар;
* самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python

Самый большой бар: 
	 · Спорт бар «Красная машина»: 450 мест.

Самый маленький бар: 
	 · Фреш-бар: 0 мест.
	 · БАР. СОКИ: 0 мест.
	 · Бар в Деловом центре Яуза: 0 мест.
	 · Соки: 0 мест.

Введите Ваши координаты: 
долгота: 37.617299900000035
широта: 55.755826

Ближайший бар: 
	 · Бар столовой № 1.
	 · Бар «Ракета».

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
