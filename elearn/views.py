from django.shortcuts import render, redirect

# Shared Views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def login_form(request):
    return render(request, 'login.html')

def logoutView(request):
    return redirect('home')

def loginView(request):
    pass


# Admin Views

def dashboard(request):
    pass

def InstrucorSignUpView(request):
    pass

def AdminLearner(request):
    pass

def course(request):
    pass

def AdminCreatePost(request):
    pass

def AdminListTise(request):
    pass

def ListAllTise(request):
    pass

def ADeletePost(request):
    pass

def ListUserView(request):
    pass

def ADeleteUser(request):
    pass

def create_user_form(request):
    pass

def create_user(request):
    pass

def acreate_profile(request):
    pass

def auser_profile(request):
    pass


# Instructor View
def home_instructor(request):
    pass

def QuizCreateView(request):
    pass

def QuizeUpdateView(request):
    pass

def question_add(request):
    pass

def question_change(request):
    pass

def QuizListView(request):
    pass

def QuestionDeleteView(request):
    pass

def QuizResultsView(request):
    pass

def QuizDeleteView(request):
    pass

def question_add(request):
    pass

def QuizUpdateView(request):
    pass

def CteatePost(request):
    pass

def TiseList(request):
    pass

def user_profile(request):
    pass

def create_profile(request):
    pass

def tutorial(request):
    pass

def publish_tutorial(request):
    pass

def LNotesList(request):
    pass

def publish_notes(request):
    pass

def update_file(request):
    pass


# Learner Views

def home_learner(request):
    pass

def LearnerSignUpView(request):
    pass

def ltutorial(request):
    pass

def LLNotesList(request):
    pass

def ITiseList(request):
    pass

def luser_profile(request):
    pass

def LTutorialDetail(request):
    pass

def LearnerInterestsView(request):
    pass

def LQuizListView(request):
    pass

def TakenQuizListView(request):
    pass

def take_quiz(request):
    pass