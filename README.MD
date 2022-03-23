DESAFIO - EMPRESA Mobi2Buy

Um desafio criado pela empresa para criar .

Os pré-requisitos é Ter instalado Python3+, pip e instalar o requirements do projeto.

`pip install -r requirements.txt`

Após instalar, rodar os comando abaixo para criar o banco de dados.

`python manage.py makemigrations`

`python manage.py migrate`

Com o banco de dados criado, crie o superuser para a tela de administração do django. O mesmo irá 
pedir um nome de usuário, e-mail e senha.

`python manage.py createsuperuser`

Por fim basta rodar o projeto.

`python manage.py runserver`


