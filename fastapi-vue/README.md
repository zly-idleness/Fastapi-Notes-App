# Introduction

- This is a simple web project based on FASTAPI + VUE  

- Just made it for fun ,no need to be too serious , haha

- Well , maybe also for learning some basic web development skills


# Structure

## Overview
```
.
©À©¤©¤ docker-compose.yml
©À©¤©¤ README.md
©¸©¤©¤ services
   ©À©¤©¤ backend
   ©¦  ©À©¤©¤ Dockerfile
   ©¦  ©À©¤©¤ migrations
   ©¦  ©À©¤©¤ pyproject.toml
   ©¦  ©À©¤©¤ requirements.txt
   ©¦  ©¸©¤©¤ src
   ©¸©¤©¤ frontend
      ©À©¤©¤ babel.config.js
      ©À©¤©¤ dist
      ©À©¤©¤ Dockerfile
      ©À©¤©¤ jsconfig.json
      ©À©¤©¤ node_modules
      ©À©¤©¤ package-lock.json
      ©À©¤©¤ package.json
      ©À©¤©¤ public
      ©À©¤©¤ README.md
      ©À©¤©¤ src
      ©¸©¤©¤ vue.config.js

```
## Backend
```
.
©À©¤©¤ Dockerfile
©À©¤©¤ migrations
©¦  ©¸©¤©¤ models
©¦     ©¸©¤©¤ 0_20230802123924_init.py
©À©¤©¤ pyproject.toml
©À©¤©¤ requirements.txt
©¸©¤©¤ src
   ©À©¤©¤ __pycache__
   ©¦  ©¸©¤©¤ main.cpython-311.pyc
   ©À©¤©¤ auth
   ©¦  ©À©¤©¤ __pycache__
   ©¦  ©À©¤©¤ jwthandler.py
   ©¦  ©¸©¤©¤ users.py
   ©À©¤©¤ crud
   ©¦  ©À©¤©¤ __pycache__
   ©¦  ©À©¤©¤ notes.py
   ©¦  ©¸©¤©¤ users.py
   ©À©¤©¤ database
   ©¦  ©À©¤©¤ __pycache__
   ©¦  ©À©¤©¤ config.py
   ©¦  ©À©¤©¤ models.py
   ©¦  ©¸©¤©¤ register.py
   ©À©¤©¤ main.py
   ©À©¤©¤ routes
   ©¦  ©À©¤©¤ __pycache__
   ©¦  ©À©¤©¤ notes.py
   ©¦  ©¸©¤©¤ users.py
   ©¸©¤©¤ schemas
      ©À©¤©¤ __pycache__
      ©À©¤©¤ notes.py
      ©À©¤©¤ token.py
      ©¸©¤©¤ users.py
```
## Frontend
```
.
©À©¤©¤ App.vue
©À©¤©¤ assets
©¦  ©À©¤©¤ logo-w.png
©¦  ©¸©¤©¤ logo.png
©À©¤©¤ components
©¦  ©À©¤©¤ HelloWorld.vue
©¦  ©¸©¤©¤ NavBar.vue
©À©¤©¤ main.js
©À©¤©¤ router
©¦  ©¸©¤©¤ index.js
©À©¤©¤ store
©¦  ©À©¤©¤ index.js
©¦  ©¸©¤©¤ modules
©¦     ©À©¤©¤ notes.js
©¦     ©¸©¤©¤ users.js
©¸©¤©¤ views
   ©À©¤©¤ DashboardView.vue
   ©À©¤©¤ EditNoteView.vue
   ©À©¤©¤ HomeView.vue
   ©À©¤©¤ LoginView.vue
   ©À©¤©¤ NoteView.vue
   ©À©¤©¤ ProfileView.vue
   ©¸©¤©¤ RegisterView.vue
```
# Reference
[fastapi-vue by Michael Herman](https://github.com/testdrivenio/fastapi-vue)  

Thanks to these guy, my app is mostly developed within their tutorial.

Also, thanks to ChatGPT, it has worked hard and provided perfect assistance, writing a lot of code for me.

