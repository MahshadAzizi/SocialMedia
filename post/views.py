from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import NewPostForm, NewCommentForm
from .models import Post, Comments
from django.views.generic import ListView, DetailView


class NewPost(View):
    """Create a new post"""

    def get(self, request):
        form = NewPostForm()
        return render(request, 'post/new_post.html', {"form": form})

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post/all")
        else:
            return HttpResponse("not saved")


class Posts(ListView):
    """Return list of posts"""
    model = Post
    ordering = ['-date_posted']


class PostDetail(DetailView):
    """Return detail of post"""
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = NewCommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.post_comment.all().order_by('-comment_date')

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context


class LastPostWeek(View):
    """Return last week posts"""
    def get(self, request):
        posts = Post.objects.get_query_set()
        return render(request, 'post/last_post.html', {'posts': posts})


# class NewComment(View):
#     def get(self, request, *args, **kwargs):
#         form = NewCommentForm()
#         return render(request, 'post/new_comment.html', {'form': form})
#     # def get(self, request, post_id: int):
#     #     form = NewCommentForm()
#     #     post = self.get_object()
#     #     return render(request, 'post/new_comment.html', {"form": form})
#
#     def post(self, request, post_id: int):
#         form = NewCommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f"/post/postdetail/{post_id}")
#         else:
#             return HttpResponse("not saved")


def new_comment(request, post_id: int):
    """Create a new comment on special post"""
    if request.method == "GET":
        form = NewCommentForm()
        return render(request, 'post/new_comment.html', {"form": form})
    elif request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                username=form.cleaned_data["username"],
                comment=form.cleaned_data["comment"],
                post=Post.objects.get(id=post_id)
            )
            comment.save()
            return HttpResponseRedirect(f"/post/postdetail/{post_id}")
        else:
            return HttpResponse("Not saved")
