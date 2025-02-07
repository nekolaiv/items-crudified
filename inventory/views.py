from django.shortcuts import redirect, render

from inventory.models import Food, Gadget

# Create your views here.

def index(request):
    foods = Food.objects.all()
    gadgets = Gadget.objects.all()
    return render(request, 'index.html', {'foods': foods, 'gadgets': gadgets})


def add_food(request):
    return render(request,'add_food.html')


def add_food_form(request):
    food_id=request.POST['id']
    food_name=request.POST['name']
    food_price=request.POST['price']
    foods=Food(id=food_id, name=food_name,price=food_price)
    foods.save()
    return redirect("/")


def add_gadget(request):
    return render(request,'add_gadget.html')


def add_gadget_form(request):
    gadget_id=request.POST['id']
    gadget_name=request.POST['name']
    gadget_price=request.POST['price']
    gadgets=Gadget(id=gadget_id, name=gadget_name,price=gadget_price)
    gadgets.save()
    return redirect("/")


def edit_food(request, id):
    foods=Food.objects.get(id=id)
    return render(request,'edit_food.html',{'foods':foods})


def edit_food_form(request, id):
    food_id=request.POST['id']
    food_name=request.POST['name']
    food_price=request.POST['price']
    food=Food.objects.get(id=id)
    food.id=food_id
    food.name=food_name
    food.price=food_price
    food.save()
    return redirect("/")


def edit_gadget(request, id):
    gadgets=Gadget.objects.get(id=id)
    return render(request,'edit_gadget.html',{'gadgets':gadgets})


def edit_gadget_form(request, id):
    gadget_id=request.POST['id']
    gadget_name=request.POST['name']
    gadget_price=request.POST['price']
    gadget=Gadget.objects.get(id=id)
    gadget.id=gadget_id
    gadget.name=gadget_name
    gadget.price=gadget_price
    gadget.save()
    return redirect("/")


def delete_food(request,id):
    foods=Food.objects.get(id=id)
    foods.delete()
    return redirect("/")


def delete_gadget(request,id):
    gadgets=Gadget.objects.get(id=id)
    gadgets.delete()
    return redirect("/")