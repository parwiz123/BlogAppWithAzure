from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegistration, ArticleAddForm, ArticleUpdateForm
from django.contrib.auth import logout
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def article_list(request):
    article_list = Article.objects.all().order_by('-published')

    # Create a Paginator object with 3 articles per page
    paginator = Paginator(article_list, 3)

    # Get the current page number from the request ( ?page=2)
    page = request.GET.get('page')

    try:
        # Try to get the articles for the requested page
        articles = paginator.page(page)

    except PageNotAnInteger:
        # If the page is not an integer, show the first page
        articles = paginator.page(1)

    except EmptyPage:
        # If the page number is out of range, show the last page
        articles = paginator.page(paginator.num_pages)



    return render(request, 'articles.html', {'article_list':articles, 'page':page})


def register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()

            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistration()

    return render(request, 'registration/register.html', {'user_form':user_form})



@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleAddForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)

            article.author = request.user

            article.save()

            return redirect('article_list')
    else:
        form = ArticleAddForm()


    return render(request, 'add_article.html', {'form':form})


@login_required
def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')

    return render(request, 'update.html', {'form':form})



@login_required
def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})



@login_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('article_list')


def logout_view(request):
    logout(request)
    return redirect('login')
