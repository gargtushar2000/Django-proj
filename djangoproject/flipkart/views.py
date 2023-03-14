

# Create your views here.


from django.shortcuts import render
from flipkart.forms import RegisterForms,FlipForm
from flipkart.models import Flipkart



def add_cart(request):
     form=FlipForm()
     if request.method == 'POST':
        form = FlipForm(request.POST)
        if form.is_valid():
            flip = form.save()
            flip.is_ordered = True
            flip.save()
     return render(request,'order.html',{'form': form})

    




def p_detail(request):
    prod = Flipkart.objects.all()
    return render(request,'product.html',{'prod':prod})



