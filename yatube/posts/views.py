from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import *


def index(request):
    latest = Post.objects.all()
    context = {"posts": latest}
    return render(request, "index.html", context)


def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных
    # или возвращает сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).all()
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "group.html", context)
