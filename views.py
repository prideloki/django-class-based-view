from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View,ListView,DetailView

from django.contrib.auth.decorators import login_required

from .forms import EmployeeForm
from .models import Publisher,Book,Author
from django.utils import timezone
# def index(request):
#   return HttpResponse("Hi")

class MyView(View):
    greeting = "Hi"
    name = "Top"
    age = 23
    def get(self,request):
        return HttpResponse(self.greeting+' '+self.name+' '+str(self.age))


class MyView2(MyView):
    # pass
    age = 37


class EmployeeRegister(View):
    def write_form(self,request,form):
        return render(request,'myapp/register.html',{'form':form})
    def get(self,request,*args,**kwargs):
        form = EmployeeForm()
        return self.write_form(request,form)

    def post(self,request,*args,**kwargs):
        form = EmployeeForm(request)
        if form.is_valid():
            # form.cleaned_data[]
            pass
        return self.write_form(request,form)

class Publisher(ListView):
    model = Publisher
    context_object_name = 'publishers'

# if i changed to Publisher, it's not working
class BookDetail(DetailView):
    #return both a book ints and author list
    model = Book
    
    template_name = "myapp/book_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(BookDetail,self).get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        return context

class AuthorBookList(ListView):
    template_name = 'myapp/books_by_author.html'
    context_object_name = "books"
    def get_queryset(self):

        self.authors = Author.objects.filter(name=self.args[0])
        return Book.objects.filter(authors=self.authors)

    def get_context_data(self, **kwargs):
        context = super(AuthorBookList,self).get_context_data(**kwargs)
        context['authors'] = self.authors
        return context

class AuthorDetailView(DetailView):
    context_object_name = 'author'
    queryset = Author.objects.all()

    def get_object(self):
        #update obj every time, we access to this
        author = super(AuthorDetailView,self).get_object()
        author.last_accessed = timezone.now()
        author.save()
        return author