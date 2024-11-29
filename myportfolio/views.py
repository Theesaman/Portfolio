from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from .bot import send_message
from .models import *
from .form import *
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =CommentForm
    success_url = "/"

    def form_valid(self,form):
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('text')
      text = f"Name : {name}\nEmail : {email}\nMessage : {content}"
      send_message(text)
      form.save()
      return super().form_valid(form)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

def index_view(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request=request,template_name='index.html', context=context)

def about_view(request):
    return render(request=request, template_name='about.html')

def project_view(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'projects.html', context)

def contact_view(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = CommentForm()
    return render(request, 'contact.html', {'form': form})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('detailsblog-page', pk=blog.pk)
    else:
        form = BlogCommentForm()

    return render(request, 'single-blog.html', {'blog': blog, 'form': form})



def detailsproject_view(request):
    return render(request=request, template_name='single-project.html')