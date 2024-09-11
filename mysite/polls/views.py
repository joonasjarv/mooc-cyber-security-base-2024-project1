import sqlite3
import re

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Question


def index(request):
    list = Question.objects.all()
    context = {"list": list, "user": request.user}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        selected_choice = request.POST.get('choice')

        if selected_choice == 'yes':
            question.votes_yes = F("votes_yes") + 1
            question.save()
        elif selected_choice == 'no':
            question.votes_no = F("votes_no") + 1
            question.save()
        else:
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# CSRF flaw, fix by removing @csrf_exempt
@csrf_exempt
# A5:2017-Broken Access Control, fix by adding @login_required
# @login_required
def add(request):
    # A5:2017-Broken Access Control https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html
    # Only admins should be able to add polls, fix:
    # if not request.user.is_superuser:
    #    return HttpResponseRedirect("/polls")

    if request.method == 'POST':
        # A1:2017-Injection https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html
        # Example malicious question_text: '); DROP TABLE polls_question; --
        question_text = request.POST.get('question_text')
        
        # For partial defense server-side validation
        # pattern = r'^[A-Za-zA-Z0-9, ]*[?]$'
        # if not re.match(pattern, question_text):
        #     context = {"user": request.user, "error_message": "Only alphanumeric input with question mark allowed."}
        #     return render(request, "polls/add.html", context)

        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = f"INSERT INTO polls_question (votes_yes, votes_no, question_text) VALUES (0, 0, '{question_text}');"
        cursor.executescript(query)
        connection.commit()
        connection.close()
        # Fix:
        # Question.objects.create(question_text=question_text)

        return HttpResponseRedirect("/polls")
    
    context = {"user": request.user}
    return render(request, "polls/add.html", context)
