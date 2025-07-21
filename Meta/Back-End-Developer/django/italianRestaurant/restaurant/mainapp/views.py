from django import http
from django.shortcuts import get_object_or_404, redirect, render
from .models import MenuItem
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'mainapp/index.html')

def menu(request):
    category = request.GET.get('category')

    if category:
        # Filtered by category
        items = MenuItem.objects.filter(category=category, available=True)
        return render(request, 'mainapp/menu.html', {
            'items': items,
            'selected_category': category,
        })
    else:
        # Group by category
        categories = ['starter', 'main', 'dessert', 'drink']
        grouped_items = {
            cat: MenuItem.objects.filter(category=cat, available=True)
            for cat in categories
        }
        return render(request, 'mainapp/menu.html', {
            'grouped_items': grouped_items,
            'selected_category': None,
        })

def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'mainapp/menu_item_detail.html', {'item': item})


def add_to_cart(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        item = get_object_or_404(MenuItem, id=item_id)
        cart = request.session.get('cart', {})

        if str(item_id) in cart:
            cart[str(item_id)]['quantity'] += 1
        else:
            cart[str(item_id)] = {
                'name': item.name,
                'price': float(item.price),
                'quantity': 1,
            }

        request.session['cart'] = cart
        print(f"Cart updated: {cart}")

        total_quantity = sum(i['quantity'] for i in cart.values())

        return http.JsonResponse({
            'success': True,
            'message': f"{item.name} added to cart.",
            'cart_total_quantity': total_quantity
        })

    return http.JsonResponse({'success': False}, status=400)

@csrf_exempt
def remove_from_cart(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        print(f"Received request to remove item with ID: {item_id}")
        if not item_id:
            return http.JsonResponse({'success': False, 'message': 'Item ID is required.'}, status=400)
        cart = request.session.get('cart', {})
        print(f"Current cart: {cart}")
        print(f"Attempting to remove item {item_id} from cart.")
        if str(item_id) in cart:
            print(f"Removing item {item_id} from cart.")
            del cart[str(item_id)]
            request.session['cart'] = cart
            print(f"Item {item_id} removed from cart.")

            return http.JsonResponse({'success': True, 'message': 'Item removed from cart.'})

        return http.JsonResponse({'success': False, 'message': 'Item not found in cart.'}, status=404)

    return render(request, 'mainapp/cart.html', {'error': 'Invalid request method.'})

def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'mainapp/cart.html', {
        'cart': cart,
        'total_price': total_price
    })
    
def clear_cart(request):
    if request.method == "POST":
        request.session['cart'] = {}
        return http.JsonResponse({'success': True, 'message': 'Cart cleared.'})
    return http.JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)