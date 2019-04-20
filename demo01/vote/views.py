from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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


def addquestion(request):
    return render(request, 'vote/addquestions.html')


def addquestionhandler(request):
    btitle = request.POST['btitle']
    b1 = Question()
    b1.qtitle = btitle
    b1.save()
    questions = Question.objects.all()
    context = {"questions": questions}
    return HttpResponseRedirect('/vote/', context)


def addchoice(request,id):
    question = Question.objects.get(pk=id)
    context = {'question':question}
    return render(request, 'vote/addchoice.html', context)


def addchoicehandler(request):
    quesid = request.POST['quesid']
    question = Question.objects.get(pk=quesid)
    cname = request.POST['cname']
    choice = Choice()
    choice.cname = cname
    choice.ccount = 0
    choice.cques = question
    print(quesid, cname)
    choice.save()
    choices = question.choice_set.all()
    context = {'questions': question, 'choices': choices}
    return HttpResponseRedirect('/vote/detail/'+str(quesid)+"/", context)


def modifyquestion(request,id):
    ques = Question.objects.get(pk=id)
    context = {'question': ques}
    return render(request, 'vote/modifyquestion.html', context)


def modifyquestionhandler(reqeust):
    id = reqeust.POST['quesid']
    title = reqeust.POST['qtitle']
    question = Question.objects.get(pk=id)
    question.qtitle = title
    question.save()
    questions = Question.objects.all()
    context = {"questions": questions}
    return HttpResponseRedirect('/vote/', context)


def modifychoice(request,id):
    choice = Choice.objects.get(pk=id)
    context = {'choice': choice}
    return render(request, 'vote/modifychoice.html', context)


def modifychoicehandler(request):
    id= request.POST['cid']
    cname = request.POST['cname']
    ccount = request.POST['ccount']
    choice = Choice.objects.get(pk=id)
    choice.cname = cname
    choice.ccount = ccount
    choice.save()
    question = choice.cques
    choices = question.choice_set.all()
    context = {'questions': question, 'choices': choices}
    return HttpResponseRedirect('/vote/detail/' + str(question.id) + '/', context)


def deletequestion(request,id):
    Question.objects.get(pk=id).delete()
    questions = Question.objects.all()
    context = {"questions": questions}
    return HttpResponseRedirect('/vote/', context)


def deletechoice(request,id):
    choice = Choice.objects.get(pk=id)
    question = choice.cques
    choice.delete()
    choices = question.choice_set.all()
    context = {'questions': question, 'choices': choices}
    return HttpResponseRedirect('/vote/detail/'+str(question.id)+'/', context)


