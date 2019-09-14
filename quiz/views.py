from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Quiz,Question,Answer,Player
from .forms import User_form
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from datetime import datetime

# Create your views here.
#Index Pageclass index(View):

class index(View):
    #@method_decorator(login_required(login_url='quiz1:login'))

    def get(self,request):
        quiz = Quiz.objects.filter(user=request.user)
        return render(request, 'quiz/index.html', {'all_quiz': quiz})





#Registeration Page
class Register(View):
    form_name=User_form
    def get(self,request):
        form=self.form_name(None)
        return render(request,'quiz/register.html',{'form':form})
    def post(self,request):
        form=self.form_name(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user.set_password(password)
            user.save()
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('quiz1:index')
        return render(request,'quiz/register.html',{'form':form})
#Login Page
class Login(View):
    def get(self,request):
        return render(request,'quiz/login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['name']=request.POST['username']
            return redirect('quiz1:index')

        return render(request,'quiz/login.html',{'error':'Username or password is incorrect'})
#Logout Page
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('quiz1:login')
#Quiz creating

class Quizcreate(View):


    def get(self,request):
        return render(request,'quiz/quiz_form.html')
    def post(self,request):
        quiz_name=request.POST['quiz_name']
        genre=request.POST['genre']
        no_q=request.POST['no_q']
        quiz=Quiz(user=request.user,quiz_name=quiz_name,no_q=no_q,genre=genre)
        quiz.save()
        return redirect('quiz1:quizcontent')
class Quizcontent(View):

    def get(self,request):
        quiz = Quiz.objects.order_by('-pk')[0]
        return render(request,'quiz/quizcontent.html',{'num':'1','quiz':quiz})
    def post(self,request):


        quiz=Quiz.objects.order_by('-pk')[0]
        question=request.POST['question']
        answer = request.POST['answer']
        numb=quiz.no_q
        quiz.count=quiz.count+1
        quiz.save()
        q=Question(quiz=quiz,question=question)
        q.save()
        a=Answer(quiz=quiz,answer=answer)
        a.save()
        if quiz.count <= numb:
            return render(request,'quiz/quizcontent.html',{'num':quiz.count})
        else:
            return redirect('quiz1:index')
class Play(View):
    def get(self,request,*args,**kwargs):
        name=request.user.username
        quiz=Quiz.objects.get(pk=self.kwargs['yo'])
        quiz.count = 1
        quiz.array = 0
        quiz.save()
        x = Player(quiz=quiz, name=name)
        x.save()
        que = Question.objects.filter(quiz=quiz).order_by('pk')[quiz.array]


        return render(request,'quiz/play.html',{'que':que,'quiz':quiz,'no':quiz.count})


    def post(self,request,*args,**kwargs):

        name = request.user.username
        quiz = Quiz.objects.get(pk=self.kwargs['yo'])
        ans=Answer.objects.filter(quiz=quiz).order_by('pk')[quiz.array]
        answer=request.POST['answer']
        que = Question.objects.filter(quiz=quiz).order_by('pk')[quiz.array]
        x=Player.objects.order_by('-pk')[0]
        if answer!=ans.answer:
            error='Sorry! Answer is not correct!'
            return render(request, 'quiz/play.html', {'que': que, 'quiz': quiz, 'no': quiz.count,'error':error})
        else:
            x.score=x.score+1
            x.save()
            quiz.array=quiz.array+1
            quiz.count=quiz.count+1
            quiz.save()
            if quiz.count<=quiz.no_q:
                que = Question.objects.filter(quiz=quiz).order_by('pk')[quiz.array]
                return render(request, 'quiz/play.html', {'que': que, 'quiz': quiz, 'no': quiz.count})
            else:
                quiz.array=0
                quiz.count=1
                quiz.save()
                return redirect('quiz1:index')
class Quizrank(View):
    def get(self,request,*args,**kwargs):
        quiz=Quiz.objects.get(pk=self.kwargs['yo'])
        player=Player.objects.filter(quiz=quiz).order_by('-score')
        return render(request,'quiz/quizscore.html',{'player':player,'quiz':quiz})







