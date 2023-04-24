- nginx -s сигнал
  - stop — быстрое завершение
  - quit — плавное завершение
  - reload — перезагрузка конфигурационного файла
  - reopen — переоткрытие лог-файлов

sudo service nginx start     
nginx -s quit
nginx -s reload

sudo service nginx status

docker build . -f Dockerfile -t static
docker run -ti -p 80:80 static
docker run -ti static bash