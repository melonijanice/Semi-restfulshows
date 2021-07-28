from django.shortcuts import redirect, render
from .models import Show
from django.contrib import messages


# Create your views here.
def new_show(request):
    return render(request,'new_show.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/new')
    else:
        if request.method=="POST":
            new_show=Show.objects.create(title=request.POST["title"],network=request.POST["network"],release_date=request.POST["release_date"],description=request.POST["description"])
            print(new_show.id)
        return redirect(f'/shows/{new_show.id}')

def view_show(request,id):
    context={"view_shows":Show.objects.filter(id=id)}
    return render(request,'view_shows.html',context)

def show(request):
    context={"all_shows":Show.objects.all()}
    return render(request,'shows.html',context)

def edit_show(request,id):
    context={"edit_shows":Show.objects.filter(id=id)}
    return render(request,'edit_shows.html',context)

def update_show(request,id):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{id}/edit')
    else:
        update_data=Show.objects.get(id=id)
        if request.method=="POST":
            if(request.POST["title"]!=update_data.title):
                update_data.title=request.POST["title"]
            if(request.POST["network"]!=update_data.network):
                update_data.network=request.POST["network"]
            if(request.POST["release_date"]!=update_data.release_date):
                update_data.release_date=request.POST["release_date"]
            if(request.POST["description"]!=update_data.description):
                update_data.description=request.POST["description"]
        update_data.save()       
        return redirect(f'/shows/{id}')

def delete_show(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')








