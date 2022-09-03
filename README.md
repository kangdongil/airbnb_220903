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


# 1.0 개발환경 준비하기
### 1.1 Python에서 가상환경이 필요한 이유
- Django로 개발하려면 Package를 관리할 수 있는 개발환경을 구축해야한다.
- 기본적으로 Python은 package를 Global(광역)하게 설치하므로
- poetry와 같이 가상환경 관리자를 통해 project간 독립적인 환경을 제공해줘야 한다.
- 가상환경 관리자를 통해 proejct마다 다른 버젼의 package를 관리하기 수월하다.

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

## 1.4 Git 세팅하기
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
