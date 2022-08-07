from django.shortcuts import render
from django.http import HttpResponse

cook_book = {}
with open('cook/recept.txt', 'r', encoding='utf-8') as file:
    for i in range(4):
        q = file.readline().strip()
        cook_book[q] = []
        w = file.readline().strip()
        for i in range(int(w)):
            r = file.readline().strip().replace('|', ',').split(',')
            cook_book[q].append({'ingredient_name': r[0], 'quantity': int(r[1]), 'measure': r[2]})
        file.readline().strip()


def get_shop_list_by_dishes(dishes, person_count=1):
    a = []
    for el in cook_book:
        if el in dishes:
            for e in cook_book[el]:
                a.append(f"{e['ingredient_name']}, {e['measure']}: {e['quantity'] * person_count}")
    return a


def omlet(request):
    if 'servings' in request.GET:
        servings = int(request.GET['servings'])
    else:
        servings = 1
    oml = get_shop_list_by_dishes('omlet', servings)
    context = {'data': oml}
    return render(request, 'cook.html', context)


def duck(request):
    if 'servings' in request.GET:
        servings = int(request.GET['servings'])
    else:
        servings = 1
    duck = get_shop_list_by_dishes('duck', servings)
    context = {'data': duck}
    return render(request, 'cook.html', context)


def potato(request):
    if 'servings' in request.GET:
        servings = int(request.GET['servings'])
    else:
        servings = 1
    potato = get_shop_list_by_dishes('potato', servings)
    context = {'data': potato}
    return render(request, 'cook.html', context)


def fahitos(request):
    if 'servings' in request.GET:
        servings = int(request.GET['servings'])
    else:
        servings = 1
    fahitos = get_shop_list_by_dishes('fahitos', servings)
    context = {'data': fahitos}
    return render(request, 'cook.html', context)
