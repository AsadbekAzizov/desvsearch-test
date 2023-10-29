from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_main import models
from app_users.models import Message
from . import forms
from .utils.filter_profiles import filter_profiles
from app_main.utils.pagination import pagination


def profiles(request):
    profiles = filter_profiles(request=request)
    search_query = request.GET.get('profile', "")  # "ul"

    profiles, custom_range = pagination(request=request, queryset=profiles)

    context = {
        'page_range': custom_range,
        'profiles': profiles,
        'search_query': search_query,
    }
    return render(request, "app_users/profiles.html", context)


# class ProfileListView(ListView):
#     template_name = 'app_users/profiles.html'
#     queryset = models.Profile.objects.all().order_by('id')  # A-Z 0-9
#     context_object_name = 'profiles'
#     paginate_by = 6
#     paginator_class = Paginator
#     page_kwarg = 'page'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProfileListView, self).get_context_data(**kwargs)
#         context['search_query'] = self.request.GET.get('profile', '')
#         # context['profiles'] = filter_profiles(request=self.request)
#         return context


def profile_detail(request, pk):
    profile = models.Profile.objects.get(id=pk)
    projects = profile.project_set.all()  # modelname_set.all()
    dev_skills = profile.skill_set.exclude(
        description="")  # skills with description. Skills with description field set to empty value are being excluded
    other_skills = profile.skill_set.filter(
        description="")  # skills without description. Skills with description field set to empty value are being filtered

    context = {
        'profile': profile,
        'projects': projects,
        'dev_skills': dev_skills,
        'other_skills': other_skills,
    }
    return render(request, "app_users/profile_detail.html", context)


@login_required(login_url='signin')
def account(request):
    profile = request.user.profile

    context = {
        'profile': profile,
    }
    return render(request, 'app_users/account.html', context)


@login_required(login_url='signin')
def profile_edit(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # success message
            return redirect('account')
        else:
            # error message
            return redirect('profile_edit')

    form = forms.ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'form-template.html', context)


@login_required(login_url='signin')
def create_skill(request):
    if request.method == 'POST':
        form = forms.SkillForm(request.POST)
        owner = request.user.profile

        if form.is_valid():
            skill = form.save(commit=False)  # Create an object but don't save it into the database
            skill.owner = owner
            skill.save()
            # success message
            return redirect('account')
        else:
            # error message
            return redirect('create_skill')

    form = forms.SkillForm()
    context = {
        'form': form,
    }
    return render(request, 'form-template.html', context)


@login_required(login_url='signin')
def edit_skill(request, pk):  # pk => primary key => id
    skill = models.Skill.objects.get(id=pk)

    if request.method == 'POST':
        form = forms.SkillForm(request.POST, instance=skill)

        if form.is_valid():
            form.save()
            # success message
            return redirect('account')
        else:
            # error message
            return redirect('edit_skill', pk=pk)

    form = forms.SkillForm(instance=skill)
    context = {
        'form': form,
    }
    return render(request, 'form-template.html', context)


@login_required(login_url='signin')
def delete_skill(request, pk):
    skill = models.Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        # success message
        return redirect('account')

    context = {
        'object': skill.title,
        'object_type': 'skill',
    }
    return render(request, 'delete.html', context)


@login_required(login_url='signin')
def inbox(request):
    profile = request.user.profile
    # unread_messages = Message.objects.filter(receiver=profile).filter(is_read=False).count()
    unread_messages = profile.received_messages.filter(is_read=False).count()

    # received_messages = Message.objects.filter(receiver=profile)
    received_messages = profile.received_messages.all().order_by('is_read', '-created')

    context = {
        'unread_messages': unread_messages,
        'received_messages': received_messages,
    }
    return render(request, 'app_users/inbox.html', context)


def send_message(request, pk):
    form = forms.MessageForm()

    if request.user.is_authenticated:
        sender = request.user.profile
        form.fields.pop('email')
        form.fields.pop('fullname')
    else:
        sender = None

    receiver = models.Profile.objects.get(id=pk)

    if request.method == 'POST':
        form = forms.MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)

            if sender:  # if sender is not None
                message.sender = sender
                message.fullname = sender.fullname
                message.email = sender.user.email  # User
                message.receiver = receiver
                message.save()
                return redirect('profile_detail', pk=pk)

            else:
                message = form.save(commit=False)
                message.receiver = receiver
                message.save()
                return redirect('profile_detail', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'form-template.html', context)


@login_required(login_url='signin')
def message_detail(request, pk):
    message = Message.objects.get(id=pk)

    if not message.receiver == request.user.profile:
        # error message: "You can not read other dude's messages"
        return redirect('inbox')

    message.is_read = True
    message.save()

    context = {
        'message': message
    }
    return render(request, 'app_users/message_detail.html', context)


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            # error message: passwords are not similar
            return redirect('signup')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password1)
        user.save()

        # success message: Successfully signed up ...
        return redirect('signin')

    return render(request, 'app_users/signup.html')


def signin(request):
    if request.user.is_authenticated:
        # warning message: "Logout first to log in again"
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # returned value from authenticate() would be either a real user object or None
        # if user with credentials provided does not exist in the database

        if user:  # user is not None
            login(request, user)
            # takes the request and the user and puts the sessionid key into the user's browser's cookies
            return redirect('profiles')
        else:
            return redirect('signin')

    return render(request, 'app_users/signin.html')


def signout(request):
    logout(request)
    return redirect('signin')
