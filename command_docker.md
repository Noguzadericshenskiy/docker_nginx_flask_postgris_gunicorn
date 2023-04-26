
- Удалить контейнер `sudo docker rm  conteiner_name`
  - Посмотреть образы `sudo docker ps -a`
  - Удалить образ `sudo docker rmi name_images`
  - Посмотреть образы `docker images`
  - Посмотреть кто сидит на порту `sudo ss -lptn 'sport = :5432'`
  - Убить процес `sudo kill PID` 
  - изменить права доступа на файл или директорию `sudo chmod -R 777 .db ` рекурсивно включая 
    все папки и подпапки всем, 777 могут все, .db - путь до файла или директории
  - посмотреть права `ls -ld .db`
  - Удаление контейнера и его тома (volume) `docker rm -v <id_cont>`, `docker-compose down -v`
  - Удалять контейнеры все же лучше с опцией -v
  - Удаление всех остановленных контейнеров `docker container prune`
  - удалить все контейнеры `docker system prune`, `docker prune`
  - удалить все образы `docker rmi $(docker images -a -q)`
  - создать сеть `docker network create -d overlay \
                  --subnet=192.168.0.0/16 \
                  --aux-address="my-router=192.168.1.5" \
                  --aux-address="my-switch=192.168.1.6"` 
  - удаление сети `docker network rm MyOverlayNetwork`
  - Получение информации о сети `docker network connect MyOverlayNetwork nginx`
  - Подключение контейнера к сети при его запуске `docker run -it -d --network=MyOverlayNetwork nginx`
  - Отключение контейнера от сети `docker network disconnect MyOverlayNetwork nginx`
  - 
  - Удаление неиспользуемых (dangling) томов `docker volume prune`, `docker volume rm $(docker volume ls -f dangling=true -q)`
  - AppArmor (или "Application Armor") - это модуль безопасности ядра Linux, который позволяет системному 
    администратору ограничивать возможности программ с помощью профилей для каждой 
    программы.`sudo aa-remove-unknown`
  - ``   
