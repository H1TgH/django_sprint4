from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Post, Category


def index(request):
    posts = (
        Post.objects.select_related('category', 'author', 'location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        .order_by('-pub_date')[:5]
    )
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'author', 'location'),
        id=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    posts = (
        Post.objects.select_related('author', 'location')
        .filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now()
        )
        .order_by('-pub_date')
    )
    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'post_list': posts
        }
    )


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('blog:index')
