### Project 개요
- 내용: 파이썬 웹프레임워크 Django와 프론트엔드 React를 사용해 Airbnb 사이트를 클론코딩하기
- 목적1: 웹프레임워크 처음부터 배포까지 경험하기
- 목적2: React를 활용한 프론트엔드 개발경험 쌓기
- 소요예상시간: 3개월(22.09.03 ~ )

### 선행강의 듣기
- Python for Beginners
- ReactJS로 영화 웹 서비스 만들기


# 0.0 이론공부
### 0.1 왜 Django인가?
- 적은 시간과 코드로 많은 효과를 볼 수 있다
- 웹 개발을 하면서 발생하는 반복적이고 지엽적인 과정을 줄여준다
- 웹어플리케이션이 기본적으로 가져야 할 기능을 쉽게 가져다 사용할 수 있다
- 프로젝트의 특색인 부분에 집중할 수 있게 해준다

### 0.2 Django에서 제공하는 기능들
- 관리자패널(AdminPanel)
- 사용자(User)관련 기능: Login/Logout/속성(Attribute)/비밀번호보안(Password Authentication)
- DB & Migration
- 그외: 사용자인증/컨텐츠관리/사이트맵/RSS피드
- 보안: SQL 삽입, 사이트간 스크립팅, 요청위조, 클릭재킹 방지

### 0.3 Flask vs. Django
- Django: 풍부한 기능을 제공함. Django 자체를 이해하면서 사용하려 노력해야 함.
- Flask: 작고 가볍다. 마치 처음부터 부품을 조립하는 것과 같이 개발가능함.

### 0.3.1 Framework vs. Library
- Library
  - 개발자가 library를 호출함.
  - 코드를 import해서 call하면 끝남.
- Framework
  - framework가 우리 코드를 사용해 구현함.
  - framework가 정해놓은 이름과 규칙에 따라야 한다

### 0.4 OOP(Object-Oriented Programming) 기본 개념
1. Encapsulation
   - Class 안에 Data와 Function를 두는 것.
   - Class: Instance를 찍어내는 설계도
   - Instance: Class에 의해 찍어낸 결과물
   - Method: Class 안에 있는 Function
     - Class를 조작할 수 있는 UI를 제공함
2. Inheritance
   - Class를 재사용하고 확장할 수 있음
   - 부모클래스 속성이 상속받는 클래스에 그대로 전달됨
3. Abstraction
   - 인터페이스를 제공해 편의성을 주되 구체적인 구현과정을 숨기는 것
4. Polymorphism
   - Poly(여러) + Morphism(형태)
   - 부모클래스의 Method를 overwrite하되 datatype과 같은 규칙은 준수함
### 0.5 Python에서 Class 사용하기
1. Constructer
   - class가 생성될 때 호출되는 method
   - python에서는 "__init__"가 constructor 역할을 함.
   - "__init__" method는 `self` 인자를 가짐
   - `self`는 instance 자신을 의미한다(javascript `this`)
   - `self`외에 인자를 추가하면 instance로부터 개별값을 받을 수 있다.
   - method가 `self`를 사용하든 안하든간에 필수적으로 인자로 두어야 한다.
2. Inherit하는 법
   - 상속받을 class의 인자로 부모class를 넣는다
   - 상속이 이뤄지면 부모class의 method를 사용가능하다
   - 다만, 부모class와 이름이 같은 method를 다시 선언하면 덮어쓰기(overwriting)이 되어 기존 내용이 사라진다.
   - 따라서, 부모 class의 내용을 살리고 싶다면 `super()`를 사용한다.
3. Underscore Method(`__`)
   - `__init__`
   - `__str__`: class를 문자열로 호출할 때 return하는 method

# 1.0 개발환경 준비하기
### 1.1 Python에서 가상환경이 필요한 이유
- Django로 개발하려면 Package를 관리할 수 있는 개발환경을 구축해야한다.
- 기본적으로 Python은 package를 Global(광역)하게 설치하므로
- poetry와 같이 가상환경 관리자를 통해 project간 독립적인 환경을 제공해줘야 한다.
- 가상환경 관리자를 통해 project마다 다른 버젼의 package를 관리하기 수월하다.

## 1.2 Poetry 준비하기
### 1.2.1 Poetry를 로컬PC에서 설치하기
### 1.2.2 Poetry를 GoormIDE에서 설치하기
1. Python 3.8로 버전올리기
   - `sudo apt update && sudo apt install -y python3.9 && sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.9 0`
2. Poetry 설치하기
   - `curl -sSL https://install.python-poetry.org | python3 -`
3. Poetry를 PATH에 추가하기(`~/.profile`)
   - `const PATH=$PATH:$HOME/.local/bin`
   - 다시 시작하거나 `source ~/.profile`

## 1.3 Poetry로 Django 설치하기
- `poetry init`: poetry env 만들기
- `pyproject.toml`: poetry env에 대한 명세
- `poetry add django`: Django를 poetry로 설치하기
- `poetry shell`: 버블 접속하기
- `exit`: 버블 나가기

## 1.4 Django Project 시작하기
- `django-admin startproject config .`
- `manage.py`와 `config/`이 생성된다

## 1.5 Git 세팅하기
1. Git 시작하기
- `git init`
- `git config --global user.email [EMAIL]` / `git config --global user.name [NAME]`
2. Commit으로 트래킹하기
- `git add .`
- `git commit -m "~"`
3. 프로젝트를 Github에 올리기
- `git remote add origin [GITHUB_REPOSITORY_URL]`
- `git push origin master`
4. `.gitignore`에 제한할 파일 설정하기
- `touch .gitignore`
- [PYTHON GITIGNORE](https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore)

# 2.0 Django 4.0 알아보기
## 2.1 Django Project 구조 살펴보기
- `manage.py`
  - Terminal에서 Django 명령을 실행할 수 있도록 함.
- `db.sqlite3`
  - Dev 단계에서 Django가 사용하는 DB 파일
  - 첫 runserver에서 빈 파일로 생성됨.
  - migration을 통해 코드에 알맞는 DB 모양이 되도록 동기화함.
- `config.settings`
  - `TIME_ZONE = 'Asia/Seoul'`
    - 시간대를 대한민국으로 변경함.

### 2.1.1 manage.py 활용한 명령어
- `python manage.py [명령어]`로 사용가능하다.
- `runserver`: Django 서버 시작하기
  - `python manage.py runserver 0.0.0.0:8000`
  - config.settings: `ALLOWED_HOSTS = ['*']`
- `makemigrations`
- `migrate`: Migration 진행하기
- `createsuperuser`: 관리자 계정 생성하기

### 2.2 Migrate
- DB의 형태를 코드에 맞게 수정하는 과정.
- `migration`: 코드와 DB 간의 동기화를 해주는 파이썬 코드파일.
- 동기화가 안된 상태로 runserver할 경우 migration하도록 촉구함
- migration하는 법
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - migrate 전에 서버 종료하기

### 2.3 Admin Panel
- 첫 Migration 이후에 사용할 수 있음.
- Admin Panel 특징
  - 계정 생성/관리가 수월함.
  - 계정 정보 수정도 수월함.(비밀번호)
  - 로그인 보안
  - 비밀번호 유효성 검사
- 관리자 계정(Super User) 만들기
  - `python manage.py createsuperuser`

### 2.4 App
- App은 마치 Folder와 같다. 각 Folder에는 같은 주제의 Functionality가 들어가 있다.
- App은 특정 Data와 그에 대한 Logic들을 묶어 놓은 것이다.
- App들은 별개의 Folder에 들어가 있지만 밀접하게 연결되어 있다.
### 2.4.1 Airbnb Project에 필요한 App 생각해보기
- Room
  - Photo
  - Description
  - Amenity
  - Rule
  - Price
- User
  - profile
  - socialLogin
  - identity
  - email address
- Review
  - Upload
  - See
  - Reply
  - link to `Room` and `User`
- Experience
- Favorites
### 2.5 Django Documentation 살펴보기
- Field Types
- Field Option

## 3.0 Django Application
### 3.0.1 App Folder 구조 살펴보기
- `apps.py`
  - django가 해당 app를 다루도록 할 때 사용되는 시작점.
- `models.py`
  - app의 data에 대한 구체적인 정의나 설명하는 곳.
  - field: data가 어떠한지 규정하는 것.
- `admin.py`
  - model을 통해 admin panel에 어떻게 구현할지 정하는 곳.
### 3.1.0 App 생성하기
- `python manage.py startapp [APPNAME]`
- App의 이름(`[APPNAME]`)은 복수형으로 쓴다.
### 3.1.1 Django에 App을 등록하기
- `config/settings.py`
  - `INSTALLED_APPS = [~, [apps].apps.[Apps]Config]`

### 4.0 App Model
### 4.0.1 App Model 구조 알아보기
- App Model은 각 App의 `models.py`에서 다룬다.
- model은 `django.db.models.Model`을 상속한 class이다.
- model를 관례적으로 대문자.단수형으로 이름을 짓는다.
- model은 `entry`들을 가지며, 각 entry는 적합한 datatype을 규정하는 `field`로 이뤄진다.
- `field`는 data의 모양과 종류를 규정하며, attribute로 자세히 data가 어떠해야 하는지 설명한다.
### 4.0.2 Django Model의 장점
- python코드로 작성한 model을 DB가 이해할 수 있는 SQL코드로 변환해 DB와 소통한다.
- 개발자가 정의한 데이터에 대해 admin panel을 자동으로 생성해준다.
### 4.1 App Model 다루기
- django에서 model를 import하기
  - `from django.db import models`
- model 만들기
  - `class [App](models.Model):`
  - 무슨 model인지 설명하는 주석 달기
    - `""" Model Deifiniton for [AppName]"""`
  - model의 구성을 다루는 entry 추가하기(`field`)
    - `[FIELD_NAME] = models.[FIELD_TYPE]([ATTRIBUTE])`
### 4.1.2 App Model에서 Field 종류
- CharField()
  - 짧은 텍스트
  - `max_length=`: 글자수 제한
- TextField()
  - 긴 텍스트
- PositiveIntegerField()
  - 양의 정수
- BooleanField()
  - True / False
- DateField()
  - auto_now
  - auto_now_add
- EmailField()
- FileField()
- ImageField()

* 공통 Field Option 종류
  - `default=`: 기본값
  - null
  - blank
  - choice
  - enum
  - help_text
  - primary_key
  - unique
  - verbose_name

### 5.0 Admin Panel
### 5.1 Admin Panel 다루기
- admin과 model를 import하기
  - `django.contrib.admin`
  - `.models.[APP]`
- admin에 model 연결하기(decorator;@)
```
@admin.register([MODEL])
class [app]Admin(admin.modelAdmin):
```
- `admin.modelAdmin`
  - django가 default로 제공하는 admin panel
  - 그대로 사용한다면 pass할 것.
### 5.2 Admin Panel 상황별로 해결하기
- Instance 이름으로 설정하기
  - `models.py`: `__str__`를 `self.name`으로 return하기
- Admin Panel 기능 살펴보기
  - `pass` 대신에 이하 내용을 `tuple`(소괄호 배열)로 제시할 수 있다.
  - `list_display`
    - column에 제시할 내용
  - `list_filter`
    - 우측에 손쉽게 선택할 수 있는 필터메뉴
  - `list_editable`
    - Instance를 list 자체에서 수정할 수 있도록 설정함.
  - `search_fields`
    - 검색을 통해 조회할 내용
  - `actions`
  - `exclude`
    - admin panel에서 값을 수정할 수 없도록 방지함.
  - `fieldsets`