from django.http import HttpResponse
from django.shortcuts import render


posts = [
    {'id':1, 'name':'Shibu'},
    {'id':2, 'name':'German Shepard'},
    {'id':3, 'name':'Chow Chow'}
]


def home(request):
    context = {'posts': posts}
    return render(request, 'home.html', context)# send user to the templates html page cw

def topic(request, pk):
    post = None
    for i in posts:
        if i['id'] == int(pk):
            post = i
        context = {'post': post}
    return render(request, 'post.html', context)# send user to the templates html page cw