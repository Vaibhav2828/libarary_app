from django.shortcuts import render, redirect
from .models import BookModel
from .forms import BookModelForms
from django.http import HttpResponse


def index(request):
    shelf = BookModel.objects.all()
    return render(request, 'library.html', {'shelf': shelf})


def upload(request):
    upload = BookModelForms()
    if request.method == 'POST':
        upload = BookModelForms(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = BookModel.objects.get(id=book_id)
    except BookModel.DoesNotExist:
        return redirect('index')
    book_form = BookModelForms(request.POST or None, instance=book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = BookModel.objects.get(id=book_id)
    except BookModel.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
