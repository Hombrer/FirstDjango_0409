from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"

}


def home(request):
    text = """ <h1>"Изучаем django"</h1><br>
            <strong>Автор</strong>: <i>Шиховцов В.В.</i>
           """
    return HttpResponse(text)


def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br><br>

    <a href="/"> Back to Home </a> 
    """
    # Выше пример гиперссылки
    return HttpResponse(result)


# url /item/1
# url /item/2
def get_item(request):
    pass


# <ol>
#   <li> ... </li>
#   <li> ... </li>
#   <li> ... </li>
#   <li> ... </li>
# </ol>
def items_list(request):
    pass
