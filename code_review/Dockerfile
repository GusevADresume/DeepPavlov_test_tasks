FROM python:3.9.7-slim
#образ slim выбран для уменьшения размера

WORKDIR /app

RUN apt-get update 

ADD data.tgz ./
#команда ADD позволяет не устанавливать пакет tar для распаковки архива

COPY csv_sum.py ./

#команды с изменяемыми файлами расположены ниже остальных команд для ускорения кеширования

CMD [ "python", "./csv_sum.py" ]
#запуск csv_sum.py




