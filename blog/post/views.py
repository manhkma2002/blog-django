from django.shortcuts import render, get_object_or_404
from .models import Post, Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q


def get_category_count():
    queryset = Post.objects.values('category__title').annotate(Count('category__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST['email']
        newSignup = Signup()
        newSignup.email = email
        newSignup.save()

    content = {
        'object_list': featured,
        'latests': latest,
    }
    return render(request, 'index.html', content)


def blog(request):
    category_count = get_category_count()

    most_recent = Post.objects.order_by('-timestamp')[0:3]

    post_list = Post.objects.all()

    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    content = {
        'most_recent': most_recent,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', content)


def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'post.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(over_view__icontains=query)
        ).distinct()
    context = {'queryset': queryset}
    return render(request, 'search.html', context)