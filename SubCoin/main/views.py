from django.shortcuts import render , redirect
from .models import Price , Comment
from .get_data import set_data
from .forms import CommentForm


def index(request):
    set_data()
    prices = Price.objects.all().order_by("-price")
    return render(request, "main/index.html", {'price': prices})


def search_results(request):
    q = request.GET.get('quiz')

    res = Price.objects.filter(name__icontains=q)

    return render(request, 'main/result.html', {'res': res})


def discussion(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("discussion")
    form = CommentForm()
    comments = Comment.objects.order_by("-date")
    return render(request, "main/discussion.html" , {'comments' : comments , "form": form})
