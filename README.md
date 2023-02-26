
scrapy_parser_pep - парсер документов PEP на базе фреймворка Scrapy

Как запустить проект:

    Клонировать репозиторий и перейти в него в командной строке:

        git clone https://github.com/stas-zatushevskii/scrapy_parser_pep
        cd scrapy_parser_pep

    Cоздать и активировать виртуальное окружение:

        python / python3  -m venv env
        source env/bin/activate

    Установить зависимости из файла requirements.txt:

        python3 -m pip install --upgrade pip
        pip3 install -r requirements.txt

    Запустить проект:

        scrapy crawl pep


!! Результат работы парсера будет сохранен в папку - results