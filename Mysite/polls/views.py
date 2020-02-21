from django.shortcuts import render

from django.http import HttpResponse

from . import models

def index(request):
    latest_question_list = models.Question.objects.order_by('pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse('''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>
        <a href = 'https://www.soft98.ir'>page1</a>
        </li>
        <li>
        <a href = 'https://www.soft98.ir'>page1</a>
        </li>
    </ul>
</body>
</html>''')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)