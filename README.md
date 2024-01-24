Для запуска проекта введите следующие команды.

    poetry install 

    python3 manage.py migrate

    python3 manage.py runserver

По адресу /get-current-usd/ выводится список запросов, в том числе самым первый запрос - актуальный запрос пользователя. Запрос обрабатывается 10 сек через time.sleep, конкретно троттлинг реализовать не получилось.

Для получения API KEY и работе с API курса обрахался к этому сайту:
        
        https://fixer.io

Пример заполнения .env файла:

    SECRET_KEY_DJANGO=''
    POSTGRES_USER='postgres'
    POSTGRES_PASSWORD='qwerty'
    POSTGRES_DB='test'
    POSTGRES_HOST='localhost'
    CUR_API_KEY='api key, полученный при регистрации на сайте выше'
