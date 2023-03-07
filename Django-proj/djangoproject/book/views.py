from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,Http404
from book.forms import RegisterForms,BookForm
from book.models import Book



def create_book(request):
    form=BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.is_published = True
            book.save()
    return render(request,'create.html',{'form': form})


def list_book(request):
    book = Book.objects.all()
    return render(request,'list.html', {'book': book})



def update_book(request,**kwargs):
    context = {}
    form = BookForm()
    if id:= kwargs.get('id'):
        obj = Book.objects.get(id=id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                context['form'] = form
                HttpResponseRedirect('/demo/list')
    return render(request, 'update.html' ,context)




def delete_book(request,**kwargs):
    if pk:=kwargs.get('pk'):
        books = Book.objects.get(pk=pk)
        books.delete()
    book = Book.objects.all()
    return render(request,'list.html', {'book': book})