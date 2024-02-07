from django.shortcuts import render
from .forms import MyForm
from django.http import JsonResponse
from django.views import View

class TemplView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'landing/index.html', context={"form": form})

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь
        form = MyForm(received_data)
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data = form.cleaned_data
            data['ip'] = ip
            data['user_agent'] = user_agent



            return JsonResponse(data, json_dumps_params={"indent": 4, 'ensure_ascii': False})
        return render(request, 'landing/templates/index.html', context={"form": form})

