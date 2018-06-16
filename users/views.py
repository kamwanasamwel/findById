from django.shortcuts import render

# Create your views here.
def register_user(request):
    if request.method == 'POST':
            register = RegisterForm(request.POST, prefix='register')
            usrprofile = ProfileForm(request.POST, prefix='profile')
            if register.is_valid() * usrprofile.is_valid():
                user = register.save()
                usrprof = usrprofile.save(commit=False)
                usrprof.user = user
                usrprof.save()
                return HttpResponse('congrats')
            else:
                return HttpResponse('errors')
    else:
        userform = RegisterForm(prefix='register')
        userprofileform = ProfileForm(prefix='profile')
        return render(request, 'test/register.html', {'userform': userform, 'userprofileform': userprofileform})