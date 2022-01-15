from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,reverse
from django.views import View
from .models import MyModelName
from .forms import  NameForm 
from django.http import HttpResponseRedirect
import random
def index(request):
    form=NameForm()
    if request.method == 'POST':
        form=NameForm(request.POST)
        if form.is_valid():

            picture_id = form.save()
            request.session['id'] = picture_id.id
            id = request.session.get('id')
            return HttpResponseRedirect(reverse('display', kwargs={'id': id}))
    context={'form':form}

    return render(request,'proj/main.html',context)


def display(request,id):
    play=MyModelName.objects.get(id=id)
    possible_actions=["rock","paper","scissors"]
    play.comp_choice=random.choice(possible_actions)
    score=''
    if play.user_choice==play.comp_choice:
            score="Tie"
            
            # print("both players selected same .its  a tie!")

    elif play.user_choice=="rock":
        if play.comp_choice=="scissors":
            score ="win"
        else:
            score= "lose"

    elif play.user_choice=="paper":
        if play.comp_choice=="rock":
            score="win "
        else:
            score="lose"

    elif play.user_choice=="scissors":
        if play.comp_choice==" paper":
            score="win"
        else:
            score="lose"
    context={
        'score':score
    }
    return render(request,'proj/play.html',context)

