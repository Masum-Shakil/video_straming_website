from django.shortcuts import render, redirect
from .models import Videos, Comments
from .forms import CommentCreateForm
from django.contrib import messages

# Create your views here.
def index(request):
    videos = Videos.objects.all()
    video_list = []    
    
    for item in videos:
        temp_list = []
        temp_list.append(item)
        comments = Comments.objects.filter(video = item)
        number_of_comments = len(comments)
        temp_list.append(number_of_comments)
        video_list.append(temp_list)

    context = {
        'video_list' : video_list,
        'videos' : videos
    }

    return render(request, 'index.html', context)

def details(request, id):
    video = Videos.objects.get(id = id)
    comments = Comments.objects.filter(video = video)
    form = CommentCreateForm()

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.video = video
            form.save()
            messages.success(request, "Thanks for your comment!!!")
            return redirect('details', id)

    context = {
        'video' : video,
        'form' : form,
        'comments' : comments
    }

    return render(request, 'details.html', context)

def ajax_search(request):
    search_input= request.GET.get('search_input')
    videos = Videos.objects.filter(video_title__icontains=search_input)|Videos.objects.filter(video_description__icontains=search_input)
    video_list = []    
    
    for item in videos:
        temp_list = []
        temp_list.append(item)
        comments = Comments.objects.filter(video = item)
        number_of_comments = len(comments)
        temp_list.append(number_of_comments)
        video_list.append(temp_list)

    context = {
        'video_list' : video_list,
        'videos' : videos
    }

    return render(request, 'search.html', context)