from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Client, Product, Order
from datetime import date

# Функция для создания клиента
def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        client = Client.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('client_detail', pk=client.pk)
    return render(request, 'create_client.html')

# Функция для чтения информации о клиенте
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})

# Функция для обновления информации о клиенте
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.name = request.POST['name']
        client.email = request.POST['email']
        client.phone = request.POST['phone']
        client.address = request.POST['address']
        client.save()
        return redirect('client_detail', pk=client.pk)
    return render(request, 'update_client.html', {'client': client})

# Функция для удаления клиента
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients_list')
    return render(request, 'delete_client.html', {'client': client})

# Функция для отображения списка клиентов
def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return redirect('product_detail', pk=product.pk)
    return render(request, 'create_product.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'update_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    return render(request, 'delete_product.html', {'product': product})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def create_order(request):
    if request.method == 'POST':
        client_id = request.POST['client']
        products_ids = request.POST.getlist('products')
        total_amount = 0
        products = []
        for product_id in products_ids:
            product = Product.objects.get(pk=product_id)
            total_amount += product.price
            products.append(product)
        client = Client.objects.get(pk=client_id)
        order = Order.objects.create(client=client, total_amount=total_amount)
        order.products.set(products)
        return redirect('order_detail', pk=order.pk)
    return render(request, 'create_order.html')

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        client_id = request.POST['client']
        products_ids = request.POST.getlist('products')
        total_amount = 0
        products = []
        for product_id in products_ids:
            product = Product.objects.get(pk=product_id)
            total_amount += product.price
            products.append(product)
        client = Client.objects.get(pk=client_id)
        order.client = client
        order.total_amount = total_amount
        order.products.set(products)
        order.save()
        return redirect('order_detail', pk=order.pk)
    return render(request, 'update_order.html', {'order': order})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders_list')
    return render(request, 'delete_order.html', {'order': order})

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})



# Create your views here.
