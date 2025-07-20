# O que é?

Este repositório é uma API Restful que faz o CRUD de clientes para que o repositório [front-teste-wittel](https://github.com/tio-bryan/front-teste-wittel) possa consumir.

O objeto cliente possui os seguintes campos:

* **Nome**: Texto de até 150 caracteres;
* **CPF**: Texto de até 11 caracteres, somente dígitos, com validação de CPF, sem permitir duplicidades;
* **Data de Nascimento**: Campo de data, obrigatório, não permitindo datas futuras;
* **Data de Cadastro**: Campo de data de leitura única, preenchido automaticamente com a data atual na criação do cliente;
* **Renda Familiar**: Campo decimal opcional, com valor mínimo de 0 (zero).

Feito no Ubuntu 24.04.2 LTS dentro de um WSL 2 do Windows 11 Pro 24H2.

# Quais framworks/bibliotecas foram utilizadas?

[Django](https://www.djangoproject.com/)  
[Django Rest Framework](https://www.django-rest-framework.org/)

# Como executar?/Pré-requisitos

* Instale o [Git](https://git-scm.com/downloads) caso não tenha
* Clone este repositório: `git clone https://github.com/tio-bryan/back-teste-wittel.git`
* Entre na pasta do repositório: `cd back-teste-wittel`;
* Instale [Python](https://www.python.org/downloads/) versão maior igual a 3.12.3 caso não tenha
* Crie um ambiente virtual: `python3 -m venv {{nome_do_ambiente_virtual}}`
* Ative o ambiente virtual:
    - Linux: `source {{nome_do_ambiente_virtual}}/bin/activate`
    - Windows: `nome_do_ambiente_virtual\Scripts\Activate`
* Instale as dependências/bibliotecas: `pip install -r requirements.txt`
* Instale [Docker Engine](https://docs.docker.com/engine/install/)
* Crie um container de MySQL: `sudo docker run -p 3306:3306 --name {{nome_do_container}} -e MYSQL_ROOT_PASSWORD={{senha}} -d mysql:latest`
* Inicie o container: `sudo docker start mysql-container`
* Entre no Bash do container: `sudo docker exec -it mysql-container bash`
* Entre no terminal do MySQL: `mysql -u root -p`
* Digite a senha que foi criada no momento da criação do container
* Crie um database: `CREATE DATABASE {{nome_do_database}};`
* Saia do terminal MySQL e do Bash apertando duas vezes `Ctrl + D`
* Entre no arquivo `my.cnf` e preencha as informações do banco criado
* Rode o projeto com o comando: `python3 manage.py runserver`

## Observações
* Caso queira acessar a interface do DRF, acesse [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)
* Caso altere algo no `models.py`, será necessário realizar as migrações com os comandos:
```
python3 manage.py makemigrations back_teste_wittel
python3 manage.py migrate
```
* Caso queira desativar o ambiente virtual:
`deactivate`
