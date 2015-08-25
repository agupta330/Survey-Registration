from django.shortcuts import render
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import models
from .models import UserProfile
from django.contrib.auth.models import User


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'Survey/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

@login_required
def update(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    user = request.user
    #myuser=User.objects.get(username='amangupta12345')
    profile=user.userprofile

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.

        user_form = UserForm(data=request.POST,instance=user)
        profile_form = UserProfileForm(data=request.POST,instance=profile)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    # Render the template depending on the context.
    return render(request,
            'Survey/update_profile.html',
            {'user_form': user_form,'profile_form': profile_form,'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                #return HttpResponseRedirect('/Survey/index.html')

                return render(request, 'Survey/index.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict = {'boldmessage': "Invalid Login details "}
            return render(request, 'Survey/login.html', context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...

        context_dict = {'boldmessage': "Login"}
        return render(request, 'Survey/login.html', context_dict)
@login_required
def some_view(request):

        return HttpResponse("You are logged in.")

@login_required
def restricted(request):
    return render(request, 'Survey/survey.html', {})
    #return HttpResponse("Since you're logged in, you can see this text!")
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Survey/')

@login_required
def index(request):

    # Render the response and send it back!
    context_dict = {'boldmessage': "Login"}
    return render(request, 'Survey/login.html',context_dict)
    #return render(request, 'Survey/index.html')
@login_required
def survey1(request):


    # Render the response and send it back!
    return render(request, 'Survey/survey1.html')


#@login_required
#def update_profile(request):
#    args = {}

#    if request.method == 'POST':
#        form = UserForm(request.POST,instance=request.user)
#        form.username = request.user.username
#        form.email=request.user.email

 #       if form.is_valid():
 #           form.save()
 #           args['user_form'] = form
 #           return render(request, 'Survey/register.html', args)


@login_required
def update_profile(request):
    return render(request, 'Survey/update.html')

@login_required
def edit_profile(request):
    user = request.user
    #profile = request.user.userprofile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST)#,instance=profile)
        if all([user_form.is_valid()]):#, profile_form.is_valid()]):
            user_form.save()
            #profile_form.save()
            #return redirect('.')
            return render(request, 'Survey/update.html')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm()#instance=profile)
    return render(request, 'Survey/update.html',
                       {'user_form': user_form})#, 'profile_form': profile_form})