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
   - 기타 Method는 `dir()`를 통해 확인가능하다.

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
  - `sudo apt update && sudo apt install -y python3.8 && sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 0`
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
   - `git config --global user.email [EMAIL]`   
      `git config --global user.name [NAME]`
2. Commit으로 트래킹하기
   - `git add .`
   - `git commit -m "~"`
3. 프로젝트를 Github에 올리기
   - `git remote add origin [GITHUB_REPOSITORY_URL]`
   - `git push origin master`
4. `.gitignore`에 제한할 파일 설정하기
   - `touch .gitignore`
   - [PYTHON GITIGNORE](https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore)

## 1.6 Python 개발환경 세팅하기
### 1.6.1 VSCode
- Extension: Pylance 설치하기
- Interpreter를 해당 프로젝트의 poetry 가상환경에 설정하기
- Formatter를 `black`으로 설치하기
  - 파일 저장과 함께 포맷팅 진행함
- `SQLite Viewer`: `db.sqlite3`을 table 형태로 view하기
### 1.6.2 GoormIDE
- `poetry add --dev black`
  - `black [PATH]`
    - 해당 파일 formatting 진행함
  - `black [PATH] --check`
    - format이 안된 파일 갯수 세기

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
  - `config.settings`
    - `ALLOWED_HOSTS = ['*']`
- `makemigrations`: `models.py`에서 변경된 사항을 파일로 생성.
- `migrate`: 변경된 내용을 적용함.
- `createsuperuser`: 관리자 계정 생성하기
- `shell`: Django코드 테스트하기

### 2.2 Migrate
- DB의 형태를 코드에 맞게 수정하는 과정.
- `migration`: 코드와 DB 간의 동기화를 해주는 파이썬 코드파일.
- 동기화가 안된 상태로 runserver할 경우 migration하도록 촉구함
- migration하는 법
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - migrate 전에 서버 종료하기
- troubleshooting
  - `non-nullable field`
    - null값을 가지지 않는 field의 경우, default을 주어 해결한다.

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
- <https://docs.djangoproject.com/en/4.1/>
- [ield Types](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types)
- [Field Option](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options)

## 3.0 Django Application
### 3.0.1 App Folder 구조 살펴보기
- `apps.py`
  - django가 해당 app를 다루도록 할 때 사용되는 시작점.
- `models.py`
  - app의 data에 대한 구체적인 정의나 설명하는 곳.
  - `Field`: data가 어떠한지 규정하는 것.
- `admin.py`
  - model을 통해 admin panel에 어떻게 구현할지 정하는 곳.
### 3.1.0 App 생성하기
- `python manage.py startapp [APPNAME]`
- App의 이름(`[APPNAME]`)은 복수형으로 쓴다.
### 3.1.1 Django에 App을 등록하기
- `config/settings.py`
  ```python3
  INSTALLED_APPS = [~, [apps].apps.[Apps]Config]
  ```
### 3.1.2 APPS 목적에 따라 분류하기
- 자주 사용하는 분류가 `SYSTEM_APPS`, `CUSTOM_APPS`, `THIRD_PARTY_APPS`이다.
- 이 모든 분류는 `INSTALLED_APPS`에 포함되어야 한다.
  - 예시
    ```python3
    SYSTEM_APPS = [...]
    CUSTOM_APPS = [...]
    THIRD_PARTY_APPS = [...]
    INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS + THIRD_PARTY_APPS
    ```

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
- Model 만들기
  - `class [App](models.Model):`
  - 무슨 model인지 설명하는 주석 달기
    - `""" Model Deifiniton for [AppName]"""`
  - model의 구성을 다루는 entry 추가하기(`field`)
    ```python3
    [FIELD_NAME] = models.[FIELD_TYPE]([ATTRIBUTE])
    ```
### 4.2 App Model에서 Field 종류
- `CharField()`
  - 짧은 텍스트
  - `max_length=`: 글자수 제한
  - `choices=`: 드롭바 형태로 값을 선택가능함.
- `TextField()`
  - 긴 텍스트
- `PositiveIntegerField()`
  - 양의 정수
- `BooleanField()`
  - True / False
- `DateField()` / `DateTimeField()`
  - auto_now_add: 최초 등록 시간
  - auto_now: 최종 수정 시간
  
- `EmailField()`
- `FileField()`
- `ImageField()`
  - Python 패키지인 `Pillow`를 설치해야 한다.
    - `poetry add pillow`

### 4.2.1 CharField Choices 만들기
- 예시)
    ```python3
    class GenderChoices(models.TextChoices):
      MALE = ("male", "Male")
      FEMALE = ("female", "Female")
      
    ... choices=GenderChoices.choices
    ```
- CharField의 option으로 `choices`을 만든다.
- `models.TextChoices`를 inherit한 class를 model 안에 만든다.
  - `[CHOICE] = ([DB], [USER_LABEL])`
  - [CHOICE]는 variable으로, 대문자.
  - [DB]는 DB에 들어가는 내용, 소문자.
  - [USER_LABEL]는 사용자에게 보이는 내용. 제목형.
- option `choices`는 `[해당_Choices].choices`를 값으로 가진다.

* 공통 Field Option 종류
  - `default=`: 기본값
    - 다음 Field는 기본적으로 Null이 허용되지 않는다.   
    CharField / BooleanField
  - `null=`: Null을 허용
  - `blank=`: Form에서 필수인가?
  - `choices=`
  - `enum=`
  - `help_text=`
  - `primary_key=`
  - `unique=`
  - `editable=`

### 4.3 Model Method vs. Admin Method
- Model Method
  - model 안에 포함되는 function을 말한다.
    - argument는 `self`다
  - ORM을 통해 이용가능하다.
  - Model과 Admin 구분없이 넓게 사용가능하다.
- Admin Method
  - model 안에 포함되는 function을 말한다.
    - argument는 `self`와 register한 `model` 두개다.
  - Admin에서만 사용가능하다.

### 5.0 Admin Panel
### 5.1 Admin Panel 다루기
- admin과 model를 import하기
  - `django.contrib.admin`
  - `.models.[APP]`
- admin에 model 연결하기`(decorator;@)`
   ```python3
   @admin.register([MODEL])
	class [app]Admin(admin.modelAdmin):
   ```
- `admin.modelAdmin`
  - django가 default로 제공하는 admin panel
  - 그대로 사용한다면 pass할 것.
- `pass` 대신에 이하 내용을 `tuple`(소괄호 배열)로 제시할 수 있다.
- 항목이 한 개인 tuple은 쉼표를 넣어주자(종종 괄호가 사라짐.)

### 5.2 Admin Panel 기능 살펴보기
- `list_display`
  - column에 제시할 내용
  - `__str__`을 display 가능하다.
  - `list_filter`
  - 우측에 손쉽게 선택할 수 있는 필터메뉴
- `list_editable`
  - Instance를 list 자체에서 수정할 수 있도록 설정함.
- `search_fields`
  - 검색창을 표시함.
  - ^(startswith)
  - =(exact)
  - `__[ForeignKey]`: ForeignKey한 model의 특정 field 대상으로 조회함.
  - `search_help_text`: 검색방식에 대한 설명.
- `actions`
- `exclude`
  - admin panel에서 값을 수정할 수 없도록 방지함.
- `fields`/ `fieldsets`
- `readonly_fields`
  - 표시되지만 수정 안되는 구역

### 5.2.1 Custom Actions
- `admin.py` 혹은 `actions.py`를 만들어 새로 추가할 action에 대해 정의한다.
  - 예)
  ```python3
  @admin.action(description="~")
  def custom_action_name(model_admin, request, queryset):
  ```
   - `description`: admin panel에서 표시되는 action 내용
   - `model_admin`: action을 취한 model_admin
   - `request`: action을 요청한 user
   - `queryset`: action할 대상(체크박스한 instances)
- 정의한 action은 admin 내에 actions에 tuple로 넣는다.

### 5.2.2 Custom Filters
- Filter는 별도로 class를 만들고 `admin.SimpleListFilter`를 inherit한다.
  - 예시)
  ```python3
  class [FilterName](admin.SimpleListFilter):
  	title = "Custom Filter"
    parameter_name = "param"
    
    def lookups(self, request, model_admin):
    	return [("[PARAM]", "[FILTER_ITEM]")]
    
    def queryset(self, requests, queryset):
    	param = self.value()
        if param:
        	queryset ~.filter()
        else:
        	return queryset
  ```
  - `title`: Admin Panel 우측 Filter칸 제목
  - `parameter_name`: url창의 paramter
  - `lookups` method: list. tuple 항목으로 이뤄져 있으며,   
  (URL paramter값,Admin Panel 필터 항목)으로 구성되어 있다.
  - `queryset` method: parameter 값을 따와서 실제 filter과정을 거치는 곳이다.
- `request.GET.word[0]` 대신에 `self.value()`을 사용가능하다.

### 5.3 Admin Panel 상황별로 해결하기
- Instance 이름으로 설정하기
  - `models.py`: `__str__`를 `self.name`으로 return하기
  - `f""`를 사용해 여러 field 값을 나타낼 수 있다.
- Model 이름에 `_`이 들어가는 경우,
  - `apps.py`: `verbose_name = "Direct Messages"`
- Model 복수명이 올바르지 않을 때
  ```python3
  class Meta:
  	verbose_name_plural="~"
  ```
- 필수 내용이 아닐 때(description처럼)
  - `blank=True`

### 5.4 Admin Panel를 Method로 확장하기
- foreign_key된 instance가 몇 개인가?
  - `.count()`
- foreign_key된 instance의 integer field의 평균은 얼마인가?
  - instance 갯수가 0일 때, exception 처리하기
  ```python3
  if count = 0:
  	return "-"
  ```
  - for문으로 하되, `.all()`이 아닌 `.all().values("~")`로 한다.
    - `.all()`은 instance의 모든 것을 불러오므로 data량이 많을수록 DB에 과부하를 일으킨다.
    - `.all().values("~")는 필요한 field 값만 불러온다.`
    - `.values()`한 값은 dict에 있으므로 `dict[value]`로 값을 빼낸다.
    - 평균값은 (총합) / (Instance 개수)
    - 소수점아래 두자리까지만 return한다. (`round`)

### 6.0 Django Users App
- Django에서 자체적으로 User App을 제공한다.
  - User가 기본적으로 가져야할 요소가 있다.(Name/Email/Password)
  - permission을 자세하게 설정할 수 있다.
- 새로 시작하기보다 기존 User App을 확장하는 방향이 효율적이다.
  - `Substituting a custom User model` 참고바람.
  - [Doc:Substituting a custom user model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model)
- 프로젝트 처음 시작할 때 User App을 Custom으로 전환하는 것이 수월하다.
  - 프로젝트 개발 도중에 user model를 대체하는 것은 relationship에 영향을 준다.
  - 따라서 처음 `runserver`하기 전에 Custom User Model로 전환하거나
  - 이미 진행했다면 `db.sqlite3`과 migration(폴더,__init__.py 제외)을 제거하고 진행한다.
- User App에 추가하면 좋은 요소들
  - Profile Image

### 6.1 Custom한 User App 만들기
1. App 만들고 django에 등록하기
- `python manage.py startapp users`
- `config.settings`
   - appsConfig 추가하기
2. 기존 User Model을 inherit한 Custom Model 만들기
   - `config.settings`
   ```python3
   # Custom User Model
	AUTH_USER_MODEL = 'users.User'
   ```
   - User Model을 만들되, 기존 `models.Model`이 아닌   
   `django.contrib.auth.models.AbstractModel`를 inherit하기
3. 기존 default user App이 이미 db에 있으므로 초기화한다.
   - `db.sqlite3`과 `migrations`(폴더, __init__.py 제외)파일들 제거
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. 기존 UserAdmin을 inherit하기
   - `CustomUserAdmin`은 `django.contrib.admin`이 아닌   
   `django.contrib.auth.admin.UserAdmin`을 inherit하기

### 6.2 User Model 확장하기
- 사용하지 않는 field는 `editable=False` 한다
  - Admin 수정 페이지에도 뜨지 않게 설정하자
- `fields`와 `fieldsets`의 차이
   - `fields`는 단순나열이라면,   
   `fieldsets`은 세션별로 나눌 수 있다.
   - `fieldsets`의 경우, 여러 괄호로 나타내어 다소 난해할 수 있다.
   ```python3
	fieldsets = (("Title", {"fields: ("Item"),},),)
   ```
     - `fieldsets = (([SECTION]),([SECTION]),)`
     - `[SECTION]: ("[TITLE]", {[FIELD_TYPE]},{[CLASSES]},)`
     - `[FIELD_TYPE]: {"fields": ("[ENTRY]", "[ENTRY]", ...),}`
   - [TITLE]을 None으로 하면 제목을 생략할 수 있다.
   - 괄호 끝에 `,`(쉼표) 넣는 습관을 들이자(종종 개체가 하나면 괄호가 포맷팅되면서 사라지는 오류가 발생함)

## 7.0 Django Relationship
- Relationship: 해당 모델과 다른 모델간의 연결 관계를 나타낸다.
- Django는 data가 DB에 등록되면 자동으로 `pk(id)`를 부여한다.
- DB는 다른 모델와 relation을 맺을 때, 모델 자체를 가져오는게 아닌 `pk`를 참조한다. 
### 7.1 ForeignKey(OneToMany, ManyToOne)
- 예)
```python3
models.ForeignKey("[MODEL]", on_delete=)
```

- [MODEL]: `[App].[Model]`
- `on_delete`는 relationship인 모델이 삭제되었을 때 조치사항을 말한다.
  - models.CASCADE
    - 삭제되면 함께 없어진다
  - models.SET_NULL && Null=True
    - 삭제되어도 데이터는 남는다.
    - `Null=True`를 추가하여 Null이 가능하게 한다.
### 7.2 ManyToMany Relationship
- 예)
```python3
[ENTRY] = models.ManyToManyField("[Model]")
```
### 7.3 Reverse Accessor
- 해당 Model이 얼마나 ForeignKey되어졌는지 알 수 있다.
  - Room에게 Owner는 User를 가리킨거라면,
     Reverse Accessor는 해당 User가 얼마나 많은 Room들에게 가리켜졌는지 확인가능하다.
- Filter Lookup으로 ForeignKey 접속하기
  - ForeignKey한 model의 field를 참조가능하다.
  ```python3
  Room.objects.filter(owner__username="admin")
  ```
  - chaining도 가능하다.
- ForeignKey할 시, 대상 model에 대해`[model_name]_set`으로 QuerySet을 받을 수 있다.
- 모든 Relationship에 대해 `related_name` 속성을 추가하면 `_set`의 이름을 바꿀 수 있다.
  - `room_set`을 `related_name="rooms"`으로 바꾸면 `.rooms`로 대상 model을 접속가능하다.

### 7.4 Relationship 실전에서 쓰기
- 두 모델간의 연결관계가 있다. (Relationship)
- `多:1 관계`: ForeignKey(ManyToOne). related_name은 복수형.
- `多:多 관계`: ManyToManyField. related_name은 복수형.
- `1:1 관계`: OneToOneField. related_name은 단수형.
- `多:1 관계`: ForeignKey의 Reverse Accessor(`_set`)

### 7.4.1 Reverse Accessors Clashes(`fields.E304`) 해결하기
- 다른 두 관계의 역(Reverse)가 같은 관계를 가질 때 충돌이 발생한다.
- `[model]_[models]`로 각각 이름을 정한다.

## 8.0 Airbnb Project's App List
### 8.1 Common App
- `python manage.py startapp common`
- `commonConfig`을 `config/settings.py`에 등록하기
- `TimeStampedModel`의 Entires
  - `created` / `updated` (`DateTimeField`)
  	```python3
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ```
- `abstract model`으로 설정하기
  - 해당 Model의 Entries를 DB에 들어가지 않게 한다.
  ```python3
  class Meta:
  	abstract = True
  ```
- 대부분 model은 등록 및 수정시간이 필요하므로   
`models.Model` 대신에 `TimeStampedModel`을 inherit한다.
```python3
from common.models import TimeStampedModel

class [Model명](TimeStampedModel):
```
### 8.2 Rooms App
- `python manage.py startapp rooms`
- `RoomsConfig`을 `config/settings.py`에 등록하기
- Room Model의 Entries 추가하기
  - name(`CharField`)
  - country / city
  - address / description(`CharField / TextField`)
  - price / rooms / toilets(`PositiveIntegerField`)
  - pet_friendly / kind(`BooleanField / Choices`)
  - owner(`ForeignKey`)
  - amenities(`ManyToManyField`)
- Amenity Model의 Entries 추가하기
  - name(`CharField`)
  - description(`TextField`)
- RoomAdmin/AmenityAdmin 구현하기
  - `__str__`을 self.name을 return하기
  - Amenity의 복수형 이름을 `Amenities`으로 바꾸기
  - list_display할 field를 정하기
  - list_filter할 field를 정하기
  - Amenity 수정 페이지에 `created_at`와 `updated_at`을 readonly로 나타나게 하기

### 8.3 Experiences App
- `python manage.py startapp experiences`
- `ExperiencesConfig`을 `config/settings.py`에 등록하기
- Experience Model의 Entries 추가하기
  - name(`CharField`)
  - country / city
  - host(`ForeignKey`)
  - price(`PositiveIntegerField`)
  - address(`CharField`)
  - start / end(`TimeField`)
  - description(`TextField`)
  - perks(`ManyToManyField`)
- Perk Model의 Entries 추가하기
  - name(`CharField`)
  - details(`CharField`)
  - description(`TextField`)
- ExperienceAdmin/PerkAdmin 구현하기
  - `__str__`을 self.name을 return하기
  - list_display할 field를 정하기
  
### 8.4 Categories App
- `python manage.py startapp categories`
- `CategoriesConfig`을 `config/settings.py`에 등록하기
- Category Model의 Entries 추가하기
  - name(`CharField`)
  - kind(`Choices`)
- Room Model과 Experience Model에 `category` 추가하기
  ```python3
  category = models.ForeignKey(
    "categories.Category",
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
  )
  ```
- CategoryAdmin 구현하기
  - `__str__`을 self.name을 return하기
  - Category의 복수형 이름을 `Categories`으로 바꾸기
  - list_display할 field를 정하기
  - list_filter할 field를 정하기

### 8.4.1 Categories API
- `/categories`를 config.urls의 urlpatterns에 넣기
  - `path("categories/", include("categories.urls"))`
- 세부 url과 views 만들기
  - view 함수 만들기
  - views들을 import하기
  - view함수와 세부 url 연결하기

### 8.5 Reviews App
- `python manage.py startapp reviews`
- `ReviewsConfig`을 `config/settings.py`에 등록하기
- Reivew Model의 Entries 추가하기
  - user / room / experience(`ForeignKey`)
  - payload(`TextField`)
  - rating(`PositiveIntegerField`)
- ReviewAdmin 구현하기
  - `__str__`에 `user` 이름과 `rating` 넣기
  - `__str__`을 list_display하기
  - list_filter할 field를 정하기
  
### 8.6 Wishlists App
- `python manage.py startapp wishlists`
- `WishlistsConfig`을 `config/settings.py`에 등록하기
- Wishlist Model의 Entries 추가하기
  - name(`CharField`)
  - rooms / experiences (`ManyToManyField`)
  - owner(`ForeignKey`)
- WishlistAdmin 구현하기
  - `__str__`을 self.name을 return하기
  - list_display할 field를 정하기
  
### 8.7 Bookings App
- `python manage.py startapp bookings`
- `BookingsConfig`을 `config/settings.py`에 등록하기
- Booking Model의 Entries 추가하기
  - kind(`Choices`)
  - user / room / experience(`ForeignKey`)
  - check_in / check_out(`DateField`)
  - experience_time(`DateTimeField`)
  - guesets(`PositiveIntegerField`)
- BookingAdmin 구현하기
  - `__str__`에 `user`와 `kind`를 return하기
  - list_display할 field를 정하기
  - list_filter할 field를 정하기
  
### 8.8 Medias App
- `python manage.py startapp medias`
- `MediasConfig`을 `config/settings.py`에 등록하기
- Photo / Video Model의 Entries 추가하기
  - file(`ImageField`/`FileField`(Video))
  - description(`CharField`)
  - room / experience(`ForeignKey`)
    - if chooseable, make sure `null` and `blank` is `True`

### 8.9 Direct Messages
- `python manage.py startapp direct_messages`
- `DirectMessagesConfig`을 `config/settings.py`에 등록하기
- AdminPanel에서 `Direct_Messages`를 `Direct Messages`로 바꾸기
  - `apps.py`: `verbose_name="Direct Messages"`
- ChatRoom Model의 Entries 추가하기
  - participants(`ManyToManyField`)
- Message Model의 Entries 추가하기
  - text(`TextField`)
  - user / room(`ForeignKey`)
- ChatRoomAdmin, MessageAdmin 구현하기

## 9.0 ORM(Object Relational Mapper)
- DB와 소통하여 data를 CRUD하는 API
- `python manage.py shell`: InteractiveConsole(Django)
- Django는 Model을 만들 때, Manager라 불리는 `.objects` method가 추가되며,   
이는 DB와 소통하는 기능을 제공한다.
- QuerySet: 개선된 Array로 연이은 작업을 가능하게 한다.
  - chaining: 연이은 작업을 통해 원하는 결과를 구체적으로 받을 수 있다.
  - lazy-load: DB 과부하를 방지하고자 구체적으로 요청한 내용만 DB를 호출함.
- query값을 variable에 저장해 사용할 수 있다.
- ForeignKey를 통해 다른 연관된 Model도 다룰 수 있다.
- variable 값을 수정한 후, `.save()`하면 DB에 저장된다.
### 9.1 Django Manager(`.objects`)
- QuerySet을 return하는 method들
  - `.objects.all()`: 모든 Instance를 QuerySet로 제공함.
  - `.get([PROP]=[VALUE]): 조건에 해당하는 유일한 instance를 QuerySet로 제공함.
  - `.filter([PROP]=[VALUE])`: 조건에 해당하는 instance들을 QuerySet로 제공함.
    - filter에 여러 조건을 둘 수도 있다.
    - `.filter([PROP1]=[VALUE], [PROP2]=[VALUE])`
  - `.exclude([PROP]=[NAME])`: 결과 중 해당되는 값을 제외한다
  - `.values("[PROP]")`: Instance 전체가 아닌 특정 field 값만 추려낸다.
- DB에서 CRUD 역할을 하는 method들
  - `.create()`
    - `get_or_create()`: 중복되지 않게 DB에 data를 추가함.
  - `.delete()`
- DB State를 return하는 method들
  - `.exists()`: 해당 조건의 QuerySet이 존재하는지 True나 False를 return함.
  ```python3
  Room.filter(price__gte=150).exists() -> True
  ```
  - `.count()`: 해당 조건의 QuerySet에 item이 몇 개인지 return함.
### 9.1.1 Field Lookups
- SQL에서 Where절에 해당함.
- Lookup도 Chaining이 가능하다.
  - `pub_date__month__gte`
  - 예)
  ```python3
  [Model].objects.filter(price__gte=50)
  ```
- [PROP] 바로 뒤에 __[Lookup]을 적으면 조건에 해당한 결과를 받을 수 있다.
- NUMBER 관련
  - `gt(e)` / `lt(e)`: greater than (equal) / less than (equal)
- TEXT 관련
  - `iexact`: 대문자/소문자 구분없이(case_insensitive)
  - `contains`: VALUE를 포함하는가?
  - `icontains` = `iexact` + `contains`
  - `startswith`: value로 시작하는가?
  - `endswith`
- DATE 관련
  - `year`
  ```python3
  Room.objects.filter(created_at__year=2022)
  ```
  
## 10.0 Django Views & Templates
- `view`: URL을 접속했을 때 실행되는 function(=controller)
  - view을 통해 HTML을 render하거나   
  JSON으로 만들어 API를 구현할 수 있다.
- `template`: view 데이터를 동적으로 구현한 HTML
  - `HttpResponse`, `render`방식이 있다.
### 10.1 Django가 URL을 구현하는 과정
- 작업순서: `models > urls > views`
- `config/urls.py`: 프로젝트의 모든 URL을 관리하는 곳.
  - 예시)
  ```python3
  from django.urls import path, include
  
  urlpatterns = [
      path('[URL]/', include("[app_name].urls")),
  ]
  ```
  - `urlpatterns`: path들의 배열
  - `path`: `url`과 각 app의 `views`에서 import된 function을 연결함.
  - `include`: app마다 urls.py를 별도로 관리할 경우,   
  `config.urls`과 `[app].urls`을 연결함.
    - `django.urls.include`
- `[APP]/urls.py`
  - 예시)
  ```python3
  from django.urls import path
  from . import views
  
  urlpatterns = [
  	path('[URL]/', [View]),
    ...
  ]
  ```
  - `path`로 `url`과 `view`를 연결한다.
  - `views.py`를 import한다.
- `[APP]/views.py`
  - 예시)
  ```python3
  def [VIEW_FUNCTION] (request):
  	...(data processing)
    return ~
  ```
  - URL 접속할 때 실행되는 function들을 담은 파일.
  - view 함수는 항상 `request`라는 argument를 가짐.
  - Model을 import하고 Manager로 데이터를 불러온다.
  - 목적에 따라 HTML 혹은 JSON을 return한다.
### 10.2 View 데이터를 Template로 구현하기
1. HttpResponse
   - `django.http.HttpResponse`를 import하기
   ```python3
   return HttpResponse("[CONTENT]")
   ```
   - String이나 짧은 HTML을 보낼 수 있다.
2. render
   - `django.shortcuts.render`를 import하기
   - 예시)
   ```python3
   return render([REQUEST], "[TEMPLATE].html", {VARIABLE_DICTS})
   ```
     - `[REQUEST]`는 views function의 argument인 request를 말한다.
     - `[TEMPLATE]`은 해당 app의 `templates/` 폴더의 html 파일을 말한다.
     - `{VARIABLE_DICTS}`은 dictionary 형식으로 Template에 변수를 보낼 수 있다. 
### 10.3 URL에 Variable 넣는 방법
- url이 variable을 받으려면
  - `<int:[VAR]>` / `<str:[VAR]>`
  - views function에 argument에 variable을 받을 수 있다.
  ```python3
  def [view_function](request, pk):
  	...
  ```
- variable을 view function에서 template으로 넘기기
- template에서 variable 사용하기
  - `{{[VAR]}}`
- Template에서 if문 사용하기
  - `{% if [CONDITION] %}` / `{% else %}` / `{% endif %}`
- Template에서 for문 사용하기
  - `{% for [ITEM] in [LIST] %}` / `{% endfor %}`
- Template에서 404 처리하기
  - try...except문 사용하기
  - 만약 특정 pk의 instance가 `.get`되지 않을 경우, `render`에서 error가 뜨게 된다.
  - 이때 `except [App].DoesNotExist`
### 10.4 View 데이터를 JSON으로 return하기
- JsonResponse
  - `django.http.JsonResponse`를 import하기
  ```python3
  return JsonResponse({JSON})
  ```
  - 단, QuerySet을 JsonResponse로 보내려면 변환과정이 필요하다.
- Serializer
  - QuerySet를 Json으로 변환하거나 Json을 QuerySet으로 만드는 Formatter
  - `django.core.serializers`를 import하기
  - 예시)
  ```python3
  serializers.serialize("json", [QUERYSET]),
  ```
- 다음과 같은 방식으로 DB 내용을 JSON으로 넘길 수 있으나   
  data를 가공하기 어려운 점이 있다.   
  (Django REST framework을 써야할 이유)

## 11.0 Django REST framework(DRF)
- 쓰임새
  - `RestAPI`를 보다 수월하게 관리하고 제작하는데 도움을 주는 library.
  - DRF는 선택하여 url과 view에 적용할 수 있다.
  - API 서버를 구축하는데 많이 사용된다.
- 설치하기
  - `poetry add djangorestframework`
- THIRD_PARTY_APPS에 등록하기
  - `rest_framework`
- API URL 만들기
  - 관례적으로 API 링크는 다음과 같은 구조를 가진다.
    - `api/v1/categories`
  - 자세한 내용은 11.0.1을 참고하기
- 사용할 views에 import하기
  - `import res_framework`

### 11.0.1 잘 설계한 REST API 만들기
1. API가 사용할 url들을 나열해보자
2. verb를 제거하고 공통 domain을 뽑아보자
  - create_movies/ (x)
  - movies/
3. 공통 domain 옆에 두번째 path에는 고유식별자(unique-identifer) 두자
  - movies/inception
4. verb 대신에 HTTP Method를 사용하자
   - `GET /movies/inception`
5. 다른 object와의 관련성은 세번째 path에 넣는다.
   - `DELETE /movies/inception/actors`
6. 필터나 조건을 넣고 싶다면 `query parameter`를 이용한다.
   - `GET /movies?release_date=2021`
7. `query parameter`로 pagination도 추가할 수 있다.
   - `GET /movies?release_date=2021&page=1`
   
* HTTP Method(CRUD) 종류
   - `GET`(=READ): 서버로부터 data를 가져옴
   - `POST`(=CREATE): 서버에 data를 보냄
   - `PUT`(=UPDATE)
   - `DELETE`

### 11.0.2 Categories로 API 만들기 (예시)
- GET /categories
- POST /categories
- GET /categories/1
- PUT /categories/1
- DELETE /categories/1

### 11.1 DRF Response와 Serializer
1. DRF Response
   - "django.http.JsonResponse"를 개선함
   - `rest_framework.response.Response`를 import하기
   - 자료형을 제시하지 않고 Response할 data를 return하면 된다
   - 예시)
   ```python3
   def [VIEW](request):
   	...
    return Response([DATA])
   ```
2. DRF Serializer
   - "django.core.serializers"를 개선함
   - `rest_framework.serializers`를 import하기
   - Serializer는 Model에 대응하여 만든다
     - `serializers.Serializer`를 inherit하기
     - `serializers.[FIELD]`로 json처리할 entry 정하기
   - `ORM`로부터 받은 `queryset`을 `Serializer`에 넣는다.
     - 단, queryset이 `여러 항목`일 경우, `many=True`하기
   - serializer를 통과한 queryset을 `.data`해서 `Response`한다.
     - 예시)
     ```python3
     ...View
     queryset = Model.objects.all()
     serializer = customSerializer(queryset, many=True)
     return Response(serializer.data)
     ```

### 11.1.1 Serializer 상황에 따른 구성하기
- Serializer는 `serializers.py`를 만들어 관리한다.
- Model의 Choice를 활용하고 싶다면 Choice를 Model에서 import한다.
- queryset에 여러 항목이 있다면 `many=True`한다.
  - 예시)
  `customSerializer(queryset, many=True)`
- Serializer를 이용해 POST한다면 data에 대해 자세히 설명한다.
  - 자세히 설명한만큼 serializer는 데이터가 유효한지 검증해줄 것이다.
  - client가 입력하지 않고 DB 데이터를 넣을 경우, `read_only=True`하기
- POST할 경우, create 메서드를 만든다.
  - client가 입력한 data가 유효한지(valid) 확인한 후, save할시 실행된다.
  - `self`와 `validated_data`를 인자로 받는다.
    - `validated_data`는 form으로 받은 POST할 data를 말한다.
  - `ORM`으로 create하되, validated_data를 unpacking(**)한다.
  - 예시)
  ```python3
  def create(self, validated_data):
    	return Model.objects.create(**validated_data)
  ```
- PUT할 경우, update 메서드를 만든다.
  - client가 입력한 data가 유효한지(valid) 확인한 후, save할시 실행된다.
  - `self`, `instance`, `validated_data`를 인자로 받는다.
    - `instance`는 DB에 불러온 기존 data를 말한다.
    - `validated_data`는 form으로 받은 수정된 data를 말한다.
  - DB 데이터를 form 데이터로 덮어씌우는 과정이 필요하다.
    - `DICT.get([key], [DEFAULT])`를 사용한다.
  - form 데이터를 적용한 instance를 return한다.

### 11.2 `@api_view`로 API 관리하기
- `api_view`는 일종의 Admin Panel로 API 관리를 용이하게 한다.
- `api_view`로 API 관리하기
  - `rest_framework.decorators.api_view`를 import하기
  - 해당 view 함수 바로 앞에 `@api_view`를 붙인다.
  - 예시)
  ```python3
  @api_view()
  def [VIEW](request):
  	...
  ```
- api_view에 여러 `HTTP Method`들을 허용하기
   - `api_view`는 default로 `GET`을 제시한다.
   - 여러 HTTP Method를 보여주려면   
   데코레이터(`@`)에 표시할 HTTP METHOD들을 array로 준다.
     - 예시)
     ```python3
     @api_view(["GET", "POST"])
     def [VIEW](request):
   	 	...
     ```
   - `api_view`는 `POST`가 허용되면 입력창을 제공한다.
   - API의 HTTP METHOD는 `request.method`로 확인 가능하다.
     - if문으로 method마다 실행할 코드를 작성한다.
     - 예시)
     ```python3
     if request.method == "POST":
     	...
     ```

### 11.2.1 pk Parameter가 없는 페이지 대처하기(404)
- try/except문
- ORM으로 pk값인 data을 get한다.
- 없으면(DoesNotExist) DRF식 Error인 `NotFound`를 Throw한다.
  - `rest_framework.exceptions.NotFound`
- 예시)
```python3
try:
	qs = Model.objects.get(pk=pk)
except Model.DoesNotExist:
	raise NotFound
```

### 11.2.2 DRF로 StatusCode 보내기
- StatusCode는 `rest_framework.status`에서 import하기
- 다음은 프로젝트에서 사용한 status-code이다.
  - `HTTP_204_NO_CONTENT`: queryset을 delete한다

### 11.3 Serializer로 Form 데이터를 POST하기
- Form 데이터를 POST하는 경우,   
  Serializer는 반대로 Json을 queryset으로 변환한다.
- Serializer에 입력한 데이터에 대해 자세히 설명한다.
  - DB가 관리하는 데이터는 `read_only=True`하기
- Serializer로 POST할 때, `data=request.data`를 받는다.
  - 예시)
  ```python3
  def VIEW(request):
  	...
    Serializer(data=request.data)
  ```
- serializer를 통과한 data가 유효한지(valid)한지 확인한다.
  - 유효하다면 `.save()`하여 create 메서드를 부른다.
  - 유효하지 않다면 `.errors`를 Response한다.
  - 예시)
  ```python3
  if serializer.is_valid():
  	new_instance = serializer.save()
    ...
  else:
  	return Response(serializer.errors)
  ```
- save한 데이터를 serializer에 넣고 .data를 Response한다
  - 예시)
  ```python3
  ...
  return Response(Serializer(new_instance).data)
  ```

### 11.4 Serializer로 data를 PUT하기
- Form 데이터를 Update하려면,   
  먼저 GET하고 이를 수정한 후 POST해야한다.
- Serializer로 PUT할 때, 수정할 DB data와 수정될 Form data를 입력한다.
  - 예시)
  ```python3
  Serializer(
  	queryset,
    data=request.data,
    partial=True,
  )
  ```
  - `queryset`은 수정하고자 하는 data다.
  - `data-request.data`는 form 데이터로 바뀔 데이터다.
  - `partial=True`는 required인 entry와 상관없이 입력되지 않은 data를 유지한다.
- serializer를 통과한 data가 유효한지(valid)한지 확인한다.
  - 유효하다면 `.save()`하여 create 메서드를 부른다.
  - 유효하지 않다면 `.errors`를 Response한다.
  - 예시)
  ```python3
  if serializer.is_valid():
  	updated_instance = serializer.save()
    ...
  else:
  	return Response(serializer.errors)
  ```
- save한 데이터를 serializer에 넣고 .data를 Response한다
  - 예시)
  ```python3
  ...
  return Response(Serializer(updated_instance).data)
  ```

### 11.5 Serializer로 data를 DELETE하기
- `[QUERYSET].delete`하기
- 204 StatusCode를 Response하기

### 11.6 FBV(Function-based)를 CBV(Class-based)로 바꾸기
- `rest_framework.views.APIView`
- `APIView`를 inherit한 CBV를 만든다.
- APIView는 메서드로 `get`, `post`, `put`, `delete`를 가진다.
- 메서드 인자는 `self`와 url에서 받은 인자이다.
- pk인 페이지가 존재하는지는 메서드 `get_object`에서 확인하여 queryset을 return한다.
- get_object가 return한 queryset은 `self.get_object(pk)`로 받는다