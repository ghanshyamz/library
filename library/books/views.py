from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Books
from .form import BookForm

def addBook(request):
    if request.method == 'POST':
        bookForm = BookForm(request.POST)
        if bookForm.is_valid(): 
            bookForm.save()
            return redirect('home')
        else:
            messages.success(request, 'Error in creating your book record, invalid data!')
            return render(request, 'add_book.html', {'bookForm':bookForm})
    else:
        bookForm = BookForm()
        return render(request, 'add_book.html', {'bookForm':bookForm})

def updateBook(request, id):
    if request.method == 'POST':
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            name = bookForm.cleaned_data['name']
            author = bookForm.cleaned_data['author']
            book = Books(
                id = id,
                name = name,
                author = author,
            )
            book.save()
            return redirect('home')
        else:
            messages.success(request, 'Error in updating your book record, invalid data!')
            return render(request, 'update_book.html', {'bookForm':bookForm, 'id':id})
    else:
        book = Books.objects.filter(id=id).first()
        bookForm = BookForm(instance=book)
        return render(request, 'update_book.html', {'bookForm':bookForm, 'id':id})

def deleteBook(request, id):
    book = Books.objects.filter(id = id).delete()

    return redirect('home')