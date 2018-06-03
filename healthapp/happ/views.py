from django.shortcuts import render, redirect
# from .forms import Register, ProfileInfo
from django.contrib.auth import authenticate, login
from .models import userModel

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
'''
from .models import Benefactor
from book_listing.models import Book_List
from forum.models import Post
'''
import nltk
import math
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer



def game(request):
    age = userModel.objects.get(user=request.user).age
    return render(request, 'game.html', {'age': age})


def chatbot(request):
    return render(request, 'chatbot.html')


def myadmin(request):
    return render(request, 'index.html')


def charts(request):
    return render(request, 'charts.html')


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def bot_response(request):
    data = {"success": False}

    if request.method == "POST":
        l1,l2=[],[]
        with open("data/Questions.txt") as f:
            for line in f.readlines():
                l1.append(line.strip())
        with open("data/Answers.txt") as f:
            for line in f.readlines():
                l2.append(line.strip())
        set(stopwords.words('english'))
        ps = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        def clean(input):
            inpfin=[]
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(input)
            word_tokens = [word for word in word_tokens if word.isalpha()]
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    inpfin.append(lemmatizer.lemmatize(ps.stem(w.lower())))
            return inpfin
        fin=[]
        for i in l1:
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(i)
            word_tokens = [word for word in word_tokens if word.isalpha()]
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(lemmatizer.lemmatize(ps.stem(w.lower())))
            fin.append(filtered_sentence)
        def query(inpfin):
            infin=[]
            infin=clean(inpfin)
            #print(infin)
            max=0
            ans=0
            for i in range(len(fin)):  
                count=0
                for k in infin:
                    for j in fin[i]:
                        if j==k:
                            count=count+1
                            break
                #print(count)
                if count>max:
                    max=count
                    ans=i
            #print(max)
            return ans  
        x=query(request.POST["query"])

        data['success'] = True
        data['response'] = l2[x]

    return JsonResponse(data) 

# def menu(request):
#     return render(request, 'registration/menu.html')


# def donorPage(request):
#     return render(request, 'registration/donorPage.html')


# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = Register(request.POST)
#         profile_form = ProfileInfo(request.POST, request.FILES)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()

#             username = user_form.cleaned_data.get('username')
#             raw_password = user_form.cleaned_data.get('password')

#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.profile_pic = request.FILES['profile_pic']
#             profile.save()

#             login(request, authenticate(username=username, password=raw_password))
#             registered = True
#     else:
#         user_form = Register(request.POST)
#         profile_form = ProfileInfo(request.POST, request.FILES)
#     if registered:
#         return redirect('/booklisting/search/')
#     else:
#         return render(request, 'sign_in/register.html', {'user_form': user_form, 'profile_form': profile_form})


# '''
# def profile(request):
#     user = Profile.objects.get(user=request.user)
#     books = Book_List.objects.filter(user=request.user)
#     post = Post.objects.filter(user=request.user)
#     return render(request, 'sign_in/profile.html', {'user': user, 'books': books, 'forum': post})
# '''
