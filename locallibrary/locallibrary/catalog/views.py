from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for homepage of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    
    return render(request, 'catalog/book_detail.html', context={'book':book})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # context_object_name = 'my_book_list' # listname as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title "war"
    # template_name = 'books/my_arbitrary_template_name_list.html' # Specify template name/location

    # def get_context_data(self, **kwargs):
    #     # call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author