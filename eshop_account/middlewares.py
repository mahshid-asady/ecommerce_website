from django.shortcuts import redirect
from django.contrib import messages

LOGIN = ['login', 'register', '/']

def login_register(get_response):

    def middleware(request):
        print('before')
        if not request.user.is_authenticated and request.path not in LOGIN:
            messages.error(request, 'you should login')
            return redirect('/')

        response= get_response(request)

        print('after')

        return response


    return middleware
