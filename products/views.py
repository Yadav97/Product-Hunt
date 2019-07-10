from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def home(request):
    productsfromdb = Product.objects
    return render(request,"products/home.html",{'productsfromdb':productsfromdb})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':  #if method is not post so redirect to create.html or have get method
        #check all fields is filled by the user if one or field is not field by user redirect to create.html
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = "https://"+request.POST['url']

            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now() 
            product.hunter = request.user
            product.save() #this method is used to store this data to model in db    
            return redirect('/products/' + str(product.id))
        else:
            return render(request,"products/create.html",{'error':'all fields is required'})


    else:
        return render(request,"products/create.html")


def detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,"products/detail.html",{'product':product})



@login_required(login_url="/accounts/signup")

def upvote(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product,pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))


