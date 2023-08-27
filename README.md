**Это проект бека приложения для управления миссиями ПА**

Собирать образ контейнера:
docker build . -t hydro_web_interface:your_tag

Запускать через команду 
docker run -p 9000:9000 -v ./src:/code/src hydro_web_interface:your_tag

