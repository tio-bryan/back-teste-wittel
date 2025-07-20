sudo docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=Teste@123 -d mysql:latest
sudo docker start mysql-container
sudo docker exec -it mysql-container bash
mysql -u root -p
CREATE DATABASE backtestewittel;

python3 -m venv venv
source venv/bin/activate
deactivate

python3 manage.py makemigrations back_teste_wittel
python3 manage.py migrate
python3 manage.py runserver

pip install -r requirements.txt