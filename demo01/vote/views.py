from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'vote/index.html', context)


def detail(request, id):
    ques = Question.objects.get(pk=id)
    choices = ques.choice_set.all()
    context = {'questions': ques, 'choices': choices}
    return render(request, 'vote/detail.html', context)


def result(request):
    quesid = request.POST['qid']
    ques = Question.objects.get(pk=quesid)
    choice = request.POST['choice']
    choices = ques.choice_set.all()
    for i in choices:
        if choice == i.cname:
            ch = Choice.objects.get(pk=i.id)
            ch.ccount = ch.ccount + 1
            ch.save()
    choices1 = ques.choice_set.all()
    context = {'questions': ques, 'choices': choices1}
    return render(request, 'vote/display.html', context)
