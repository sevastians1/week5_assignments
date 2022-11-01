from django.http import HttpResponse
from django.shortcuts import render
latest_question_list = [
    {
        'id' : 1,
        'question_text': 'whats up',
        'pub_date':'2022-01-04',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
    {
        'id' : 2,
        'question_text': 'whats new',
        'pub_date':'2022-02-09',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
]



def index(request):
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

