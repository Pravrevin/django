from MLMAPP.serializers import RegistrationSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

#class RegistrationList(APIView):

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'success':200}
            return JsonResponse(message,safe=False)
        return JsonResponse(serializer.errors, status=400)