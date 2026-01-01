from django.contrib.postgres.search import TrigramSimilarity
from taggit.models import Tag # type: ignore
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post
from .forms import CommentForm, EmailPostForm, SearchForm
from django.core.mail import send_mail

def post_list(request, tag_slug=None):
    posts_page = Post.published.all().order_by('publish')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_page = posts_page.filter(tags__in=[tag])
    
    return render(request,
                  'blog_app/post/list.html',
                  {'posts': posts_page,
                   'tag': tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request,
                  'blog_app/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    return render(request,
                  'blog_app/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog_app/post/share.html', {'post': post,
                                                        'form': form,
                                                        'sent': sent})
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']  
            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
            

    return render(request,
                  'blog_app/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})