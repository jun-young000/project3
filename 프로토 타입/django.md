# Django



**0. 설치**

```terminal
# virtual environment (venv) 생성
python -m venv pyweb

# venv 실행
source pyweb/bin/activate
# window : .\pyweb\Scripts\activate.bat

# django module 설치
pip install django

# terminal 위치 확인! (${django project folder} 로 이동)
# django-admin 이용해서 프로젝트 생성
django-admin startproject mysite

# 실행
cd mysite
python manage.py runserver

# port 변경하고 싶을 때 (0: 0.0.0.0을 의미)
python manage.py runserver localhost:8888

```



### hello

```terminal
# ${django project foder} 로 이동
django-admin startproject hello

```



*/hello/views.py*

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

```



*/hello/urls.py*

```python
"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]

```



*실행*

`python manage.py runserver`



**hello01**

```terminal
# ${django project folder}/hello 로 이동
python manage.py startapp hello01

```



*hello01/views.py*

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1><a href="/hello01/test">Hello, Django!</a></h1>')

```



*hello01/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

```



*hello/urls.py*

```python
"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('hello01/', include('hello01.urls')),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello01/



*hello01/views.py*

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1><a href="/hello01/test">Hello, Django!</a></h1>')


def test(request):
    return HttpResponse('<h1><a href="/hello01">return</a></h1>')

```



*hello01/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('test', views.test)
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello01/test



**hello02**

```terminal
# ${django project folder}/hello 로 이동
python manage.py startapp hello02

```



*hello/settings.py*

```python
# 생략

# DIRS 에 폴더경로 추가
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 생략

```



*hello/templates/hello02.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello, {{name}}!</h1>
</body>
</html>
<!-- html:5 를 치면 vsc가 자동으로 만들어준다!! 기억하기 -->

```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})

```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
]

```



*hello/urls.py*

```python
"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('hello01/', include('hello01.urls')),
    path('hello02/', include('hello02.urls')),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/



*${django project folder}/template/variables01.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{lst.0}}</h1>
    <p>{{lst.1}}</p>

</body>
</html>

```



*hello02/views.py*

```PYTHON
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})

```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('var01', views.variables01),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/var01



*hello/template/variables02.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>{{dct.class}}반 {{dct.name}}님 환영합니다</h1>

</body>
</html>

```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})


def variables02(request):
    dct = {'class': 'qclass', 'name': 'dongheon'}
    return render(request, 'variables02.html', {'dct': dct})

```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('var01', views.variables01),
    path('var02', views.variables02),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/var02



*hello/template/for.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% for i in number %}
    <p>{{i}}</p>
    {% endfor %}
</body>
</html>

```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})


def variables02(request):
    dct = {'class': 'qclass', 'name': 'dongheon'}
    return render(request, 'variables02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'number', range(1, 10)})

```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('var01', views.variables01),
    path('var02', views.variables02),
    path('for', views.forLoop),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/for



*hello/templates/if01.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% if user.id  %} <h1>Hello, {{user.name}}!</h1>{% endif %}
</body>
</html>


```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})


def variables02(request):
    dct = {'class': 'qclass', 'name': 'dongheon'}
    return render(request, 'variables02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'number': range(1, 10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id': 'qclass', 'name': 'teacher'}})


```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('var01', views.variables01),
    path('var02', views.variables02),
    path('for', views.forLoop),
    path('if01', views.if01),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/if



*hello/templates/if02.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% if role == 'admin' %}
        <h1>Admin Page</h1>
        <a href="#">user list</a>
        <a href="#">user delete</a>
    {% elif role == 'manager' %}
        <h1>Manager Page</h1>
        <a href="#">user list</a>
    {% else %}
        <h1>User Page</h1>
    {% endif %}
</body>
</html>
```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})


def variables02(request):
    dct = {'class': 'qclass', 'name': 'dongheon'}
    return render(request, 'variables02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'number': range(1, 10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id': 'qclass', 'name': 'teacher'}})


def if02(request):
    return render(request, 'if02.html', {'role': 'manager'})


```



*hello02/urls.py*

```python
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('var01', views.variables01),
    path('var02', views.variables02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/



*hello/templates/href.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="{% url 'index' %}">go index page</a>
</body>
</html>

```



*hello02/views.py*

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name': 'django'})


def variables01(request):
    lst = ['Python', 'Django', 'Tempaltes']
    return render(request, 'variables01.html', {'lst': lst})


def variables02(request):
    dct = {'class': 'qclass', 'name': 'dongheon'}
    return render(request, 'variables02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'number': range(1, 10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id': 'qclass', 'name': 'teacher'}})


def if02(request):
    return render(request, 'if02.html', {'role': 'manager'})


def href(request):
    return render(request, 'href.html')

```



*hello02/urls.py*

```python
from django.urls import path
# from . import views
from hello02 import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('var01', views.variables01),
    path('var02', views.variables02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
    path('href', views.href),
]

```



*실행*

`python manage.py runserver` -> localhost:8000/hello02/href



---



### dbtest

```terminal
# ${django project foder} 로 이동
django-admin startproject dbtest

```

*window only*

[sqlite](https://www.sqlite.org/index.html) home page 가서 다운로드 받은 후, # ${django project foder}/dbtest 폴더에 압축 해제하기!! (file 3개)

`for windows` 에서  `A bundle of command-line tools for managing SQLite database files,... `  꼭 확인!

[sqlite-tools-win32-x86-3330000.zip](https://www.sqlite.org/2020/sqlite-tools-win32-x86-3330000.zip) 



*mac은 그냥 실행 가능*



*db 설정*

```terminal
cd dbtest
python manage.py migrate
# sqlite3 접속
sqlite3 db.sqlite3
# 생성된 테이블 확인
.table
# sqlite3 종료
.quit

```



*dbtest/models.py*

```python
from django.db import models

class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField('date published')

```



*dbtest/apps.py*

```python
from django.apps import AppConfig


class DbtestConfig(AppConfig):
    name = 'dbtest'

```



*dbtest/settings.py*

```python
import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbtest.apps.DbtestConfig',
]


```



*model 생성*  :  `python manage.py makemigrations dbtest`

*model 확인* : `python manage.py sqlmigrate dbtest 0001`

*table 생성* : `python manage.py migrate`



*table 확인*

```terminal
sqlite3 db.sqlite3
.table
.schema dbtest_myboard

```



*${django project folder}/dbtest/templates/index.html*

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Hello, Django with sqlite3</h1>

    <table border=1>
        <col width="50">
        <col width="100">
        <col width="500">
        <col width="100">
        <tr>
            <th>번호</th>
            <th>작성자</th>
            <th>제목</th>
            <th>작성일</th>
        </tr>
        {% if not list %} 
            <tr>
                <th colspan="4">----------작성된 글이 존재하지 않습니다----------</th>
            </tr>
        {% else %}
            {% for data in list %}
                <tr>
                    <td>{{data.id}}</td>
                    <td>{{data.myname}}</td>
                    <td><a href="">{{data.mytitle}}</a></td>
                    <td>{{data.mydate|date:"Y-m-d"}}</td>
                </tr>
            {% endfor %}
        {% endif %}
        <tr>
            <td colspan="4" align="right">
                <input type="button" value="글 작성" onclick="location.href=''" />
            </td>
        </tr>
    </table>


</body>
</html>
````



*dbtest/views.py*

```python
from django.shortcuts import render
from django.http import HttpResponse
from dbtest.models import MyBoard


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})

```



*dbtest/urls.py*

```python
"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

```



*실행* 

`python manage.py runserver`



*db 값 넣어보기*

```python
python manage.py shell

from dbtest.models import MyBoard
from django.utils import timezone

test = MyBoard(myname='admin', mytitle='test', mycontent='test1234', mydate=timezone.now())
test.save()
MyBoard.objects.all()
exit()

```



*실행* 

`python manage.py runserver`



*dbtest/templates/detail.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Detail</h1>

    <table border="1">
        <tr>
            <th>작성자</th>
            <td><input type="text" value="{{dto.myname}}" readonly></td>
        </tr>
        <tr>
            <th>제목</th>
            <td><input type="text" value="{{dto.mytitle}}" readonly></td>
        </tr>
        <tr>
            <th>내용</th>
            <td><textarea rows="10" cols="60" readonly>{{dto.mycontent}}</textarea></td>
        </tr>
        <tr>
            <td colspan="2" align="right">
                <input type="button" value="목록" onclick="" >
                <input type="button" value="수정" onclick="" >
                <input type="button" value="삭제" onclick="" >
            </td>
        </tr>
    </table>

</body>
</html>

```



*dbtest/views.py*

```python
from django.shortcuts import render
from django.http import HttpResponse
from dbtest.models import MyBoard


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})

```



*dbtest/urls.py*

```python
"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
]

```



*실행* 

`python manage.py runserver`



*dbtest/templates/update.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Update</h1>

    <form action="/updateres" method="POST">{%csrf_token%}
        <input type="hidden" name="id" value="{{dto.id}}">
        <table border="1">
            <tr>
                <th>작성자</th>
                <td><input type="text" readonly value="{{dto.myname}}"></td>
            </tr>
            <tr>
                <th>제목</th>
                <td><input type="text" value="{{dto.mytitle}}" name="mytitle"></td>
            </tr>
            <tr>
                <th>내용</th>
                <td><textarea name="mycontent" cols="60" rows="10">{{dto.mycontent}}</textarea></td>
            </tr>
            <tr>
                <td colspan="2" align="right">
                    <input type="button" value="취소" onclick="location.href='detail/{{dto.id}}'">
                    <input type="submit" value="수정">
                </td>
            </tr>
        </table>
    </form>

</body>
</html>

```

*csrf : cross-site request forgery*



*dbtest/views.py*

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from dbtest.models import MyBoard


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def updateForm(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def updateRes(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    resultTitle = myboard.update(mytitle=mytitle)
    resultContent = myboard.update(mycontent=mycontent)

    if resultTitle + resultContent == 2:
        return redirect('detail/'+id)
    else :
        return redirect('updateform/'+id)
        
```



*dbtest/urls.py*

```python
"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('updateform/<int:id>', views.updateForm, name='updateform'),
    path('updateres', views.updateRes),
]

```



*실행* 

`python manage.py runserver`



*dbtest/views.py*

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from dbtest.models import MyBoard


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def updateForm(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def updateRes(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:
        return redirect('detail/'+id)
    else :
        return redirect('updateform/'+id)


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0] == 1:
        return redirect('index')
    else:
        return redirect('detail/'+id)

```



*dbtest/urls.py*

```python
"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('updateform/<int:id>', views.updateForm, name='updateform'),
    path('updateres', views.updateRes),
    path('delete/<int:id>', views.delete),
]

```



*실행* 

`python manage.py runserver`



*dbtest/templates/insert.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Insert</h1>

    <form action="/insertres" method="POST">{%csrf_token%}
        <table border="1">
            <tr>
                <th>작성자</th>
                <td><input type="text" name="myname"></td>
            </tr>
            <tr>
                <th>제목</th>
                <td><input type="text" name="mytitle"></td>
            </tr>
            <tr>
                <th>내용</th>
                <td><textarea name="mycontent" cols="60" rows="10"></textarea></td>
            </tr>
            <tr>
                <td colspan="2" align="right">
                    <input type="button" value="취소" onclick="location.href='/index'">
                    <input type="submit" value="작성">
                </td>
            </tr>
        </table>
    </form>

</body>
</html>

```



*dbtest/views.py*

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from dbtest.models import MyBoard
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def updateForm(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def updateRes(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:
        return redirect('detail/'+id)
    else :
        return redirect('updateform/'+id)


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect('detail/'+id)


def insertForm(request):
    return render(request, 'insert.html')


def insertRes(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
    
    if result:
        return redirect('index')
    else:
        return redirect('insertform')

```



*dbtest/urls.py*

```python
"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('updateform/<int:id>', views.updateForm, name='updateform'),
    path('updateres', views.updateRes),
    path('insertform', views.insertForm, name='insertform'),
    path('insertres', views.insertRes),
]

```



*실행* 

`python manage.py runserver`



---



### dbtest2

```terminal
# ${django project foder} 로 이동
django-admin startproject dbtest2

pip install mysqlclient
# error 일 경우 둘 중 하나 선택
# 1. 관련 패키지 설치
# pip install python3.7-dev -y
# 2. conda 명령어로 설치
# conda install -c quantopian mysqlclient

```



*dbtest2/settings.py*

```python
# 생략

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 생략
```



*dbtest2/models.py*

```python
from django.db import models

class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField('date published')
    def __str__(self):
        return str({'myname':self.myname, 'mytitle':self.mytitle, 'mycontent':self.mycontent, 'mydate':self.mydate})

```



*dbtest2/apps.py*

```python
from django.apps import AppConfig


class DbtestConfig(AppConfig):
    name = 'dbtest2'

```



*dbtest/settings.py*

```python
import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbtest2.apps.DbtestConfig',
]

```



*db 생성*

```terminal
python manage.py makemigrations
python manage.py migrate

```

