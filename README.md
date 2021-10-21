# CCW
Repository with references, documentation and proposed solution for the Completion of Course Work (CCW)

![Progress](https://progress-bar.dev/1/?title=Completed%20&width=160&color=54aeff)

> [As specified by IFSC](https://sigaa.ifsc.edu.br/sigaa/verProducao?idProducao=361773&key=b0753324de8a4266395e87af40c58f2e#:~:text=O%20trabalho%20acad%C3%AAmico%20digital%20precisa,ano%20de%20apresenta%C3%A7%C3%A3o%20do%20trabalho.&text=Fonte%3A%20Elabora%C3%A7%C3%A3o%20pr%C3%B3pria%20(2018)), the CCW (Completion of Course Work) is partial requirement for obtaining the title of electronic engineer.


## Brief structure of folders and files
```text

app
├── assets
│   ├── static_dev
│   └── static_prod
├── core
│   ├── utils.py
│   └── views.py
├── defines
│   └── settings
│       ├── common.py
│       ├── development.py
│       └── production.py
│   └── urls
│       ├── common.py
│       ├── development.py
│       └── production.py
├── requirements
│   ├── common.txt
│   ├── development.txt
│   └── production.txt
├── templates
│   ├── contents
│   ├── includes
│   ├── layouts
│   └── tags
├── .gitignore
├── debug.log
├── LICENSE
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt

```

## Prerequisites
- [Python 3+](https://www.python.org)
- [Pip](https://pypi.org/project/pip)
- [Vitrualenv](https://virtualenv.pypa.io/)

## Installation;
1. [Clone](https://github.com/jvsouza/ccw.git) | [download](https://github.com/jvsouza/ccw/archive/refs/heads/main.zip) the repository;

2. Make a virtual environment;
	```sh
	$ virtualenv venv
	```

3. Install package list;
	```sh
	(venv) $ pip install -r requirements.txt
	```
4. Update the database;
	```sh
	(venv) $ python manager.py migrate
	```
5. Run the server.
	```sh
	(venv) $ python manager.py runserver
	```

## Deploy
- [Heroku platform](https://jvsouza-ccw.herokuapp.com/)

## Shields
[![](https://img.shields.io/github/languages/top/jvsouza/ccw)]()
[![](https://img.shields.io/github/languages/count/jvsouza/ccw)]()
[![](https://img.shields.io/github/license/jvsouza/ccw)]()
[![](https://img.shields.io/github/languages/code-size/jvsouza/ccw)]()
[![](https://img.shields.io/github/repo-size/jvsouza/ccw)]()
[![](https://img.shields.io/github/last-commit/jvsouza/ccw)]()

## Badges 
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
