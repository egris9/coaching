from django.shortcuts import render,redirect
from coach.models import Order,Profile
from coach.forms import Editprofileform,Editimageprofileform

def profile(request):
    orders = Order.objects.all().prefetch_related("ordertoproduct_set")
    order_data = []
    full_name= request.user.first_name+' '+request.user.last_name
    img=Profile.objects.filter(user=request.user).first().image.url   

    for order in orders:
            for order_item in order.ordertoproduct_set.all():
                if order_item.training_session:
                    training_session_name = order_item.training_session.name
                else:
                    training_session_name = "No Session"
                order_data.append({
                "name":order_item.product_name,
                "price":order_item.price,
                "first_name":order.first_name,
                "last_name":order.last_name,
                "email":order.email,
                "order_total":order.order_total,
                "training_session":training_session_name,
            })

    if request.method == "POST":
         form = Editprofileform (data=request.POST, instance=request.user)
         if form.is_valid():
              form.save()
              instance= Editimageprofileform(request.POST, request.FILES , instance=request.user.profile )
              if instance.is_valid() :
                   instance.save()
                   return redirect("/profile")
        
    return render(request, 'coach/profile.html', {'product_data': order_data ,"full_name":full_name , "img":img, })