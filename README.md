# python_requests_pytest
Автотесты API: Python, Pytest + Requests
<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> Поддерживается (активный) 

## Описание проекта
Проект предназначен для автоматизации части регрессионных проверок с помощью Pytest и Requests.

## Автоматизированные тест-кейсы
* Создание покемона → `POST /pokemons`
* Смена имени покемона → `PUT /pokemons`
* Добавление покемона в покебол → `POST /trainers/add_pokeball`
* Запрос списка покемонов для подбора противника → `GET /pokemons`
* Проведение битвы с подходящим противником из списка выше → `POST /battle`
* Проверка ответа метода → `GET /trainers`

Ожидаемые результаты 
* `status code` ответа = 201
* в `json` возвращается корректный `id`
* `status code` ответа = 200
* в `json` приходит список покемонов
* в `json` приходит сообщение с результатом проведенной битвы, `status code` ответа = 200
* в `json` присутствует корректное поле `trainer_name`

## Детали реализации

1. Тесты написаны с использованием Pytest
2. Используется библиотека Requests
3. Применена параметризация через декоратор `@pytest.mark.parametrize`

![image](https://raw.githubusercontent.com/lonmakson/python_requests_pytest/refs/heads/main/static/pytest_request.png)

![image](https://raw.githubusercontent.com/lonmakson/python_requests_pytest/refs/heads/main/static/requests.png)

## Локальный запуск тестов
1. Клонировать проект
2. Перейти в директорию проекта через терминал
3. Создать виртуальное окружение, введя команды:
   
Для MacOS (для Windows инструкция [доступна здесь](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemon.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.

