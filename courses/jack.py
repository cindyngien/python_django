from django.shortcuts import render, redirect
from .models import Product

def index(request):
	context = {
		"products": Product.objects.all()
	}
	return render(request, "products/index.html", context)

def create(request):
	print(request.POST)
	# Maybe validations?
	# new_product = Product()
	# new_product.name = request.POST["name"]
	# new_product.price = request.POST["price"]
	# new_product.save()

	Product.objects.create(name=request.POST["name"], price=request.POST["price"])

	return redirect("/")

def update(request, product_id):
	print(request.POST)
	prod = Product.objects.get(id=product_id)

	prod.name = request.POST["name"]
	prod.price = request.POST["price"]

	prod.save()

	return redirect("/")

def delete(request, product_id):
	prod = Product.objects.get(id=product_id)
	prod.delete()
	return redirect("/")
