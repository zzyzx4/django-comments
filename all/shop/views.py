from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Commentary
from .forms import CommentaryForm


def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    commentary = Commentary.objects.filter(product=pk, moderation=True)
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect("product", pk)
    else:
        form = CommentaryForm()
    return render(request, "shop/product.html", {"product": product,
                                                 "commentary": commentary,
                                                 "form": form
                                                 })
