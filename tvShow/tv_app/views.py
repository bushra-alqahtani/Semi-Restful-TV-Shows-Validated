
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from tv_app.models import Show

# Create your views here.
def index(request):
    return render(request,"index.html")


def shows(request):
    shows=Show.objects.all()
    context={
       "shows":shows
    }

    return render(request,"shows.html",context)


def create(request):# create show from the form 
    
        errors=Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value) # bag message of errors
            return redirect("/show/create")
        else:
            
                #create obj of model
            newShow=Show.objects.create(
                title=request.POST['title'],
                network=request.POST["network"],
                releseDate=request.POST["releseDate"],
                desc=request.POST["desc"]
                )
            newShow.save()
            
                
        return redirect(f"/show/{newShow.id}")



def showbyid(request,id):
    #fetch the show by id in model

    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,'showbyid.html',context)




def edit(request,id):#for edit btn 
    show = Show.objects.get(id=id)
    show.releseDate = show.releseDate.strftime("%Y-%m-%d")
    context={
        "show":show,
    }

    if request.method == "POST": #check for post method 
        errors = Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(f'/show/{id}/edit')

      
        else:
       #if one field changed| no need for change the old value
            show.title= request.POST.get('title') if request.POST.get('title')  else show.title

            show.network=request.POST.get('network') if request.POST.get('network') else show.network

            show.releseDate=request.POST.get('releseDate') if request.POST.get('releseDate') else show.releseDate	

            show.desc=request.POST.get('desc') if request.POST.get('desc') else show.desc
            show.save()
            return redirect(f"/show/{show.id}")
    return render(request,'edit.html',context)



def delete(request,id):
    show = Show.objects.get(id=id)

    show.delete()
    return redirect("/shows")









