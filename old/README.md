# django-api
Api Rest using Django





### Ativando a virtualenv

```bash
  python -m venv venv 

  . venv/bin/activate
```

### Instalando as dependências

```bash
  pip install django
  pip install djangorestframework
  pip install markdown
  pip install django-filter
  # pip install django-cors-headers
```

### Criando o projeto

```bash
  django-admin startproject api
```

### Criando a aplicação

```bash
  cd api
  python manage.py startapp core
```

### Criando o banco de dados

```bash
  python manage.py migrate
```

### Criando o super usuário

```bash
  python manage.py createsuperuser
```

### Rodando o servidor

```bash
  python manage.py runserver
```

<!-- route > view > models > serializer -->

https://youtu.be/GE0Q8YNKNgs