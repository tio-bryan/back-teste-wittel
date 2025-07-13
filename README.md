docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=Teste@123 -d mysql:latest
sudo docker exec -it mysql-container bash
mysql -u root -p
CREATE DATABASE backtestewittel;