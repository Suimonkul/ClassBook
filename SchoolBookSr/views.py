# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from SchoolBookSr.models import Support


@csrf_exempt
def support(request):
    try:
        name = request.POST.get('name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        grade = request.POST.get('grade')

        support_request = Support.objects.create(
            name=name, title=title, description=description,
            phone=phone, grade=grade
        )
        support_request.save()
        return JsonResponse(dict(request='OK'))
    except:
        return JsonResponse(dict(request='ERROR'))
