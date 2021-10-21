# completionOfCourseWork
Repository with references, documentation and proposed solution for the Completion of Course Work (CCW)

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
1. [Clone](https://github.com/jvsouza/completionOfCourseWork.git) | [download](https://github.com/jvsouza/completionOfCourseWork/archive/refs/heads/main.zip) the repository;

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
[![](https://img.shields.io/github/languages/top/jvsouza/completionOfCourseWork)]()
[![](https://img.shields.io/github/languages/count/jvsouza/completionOfCourseWork)]()
[![](https://img.shields.io/github/license/jvsouza/completionOfCourseWork)]()
[![](https://img.shields.io/github/languages/code-size/jvsouza/completionOfCourseWork)]()
[![](https://img.shields.io/github/repo-size/jvsouza/completionOfCourseWork)]()
[![](https://img.shields.io/github/last-commit/jvsouza/completionOfCourseWork)]()

## Badges 
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
