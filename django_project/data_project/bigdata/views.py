from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home1(request):
    print(request.method,"+++++")
    if request.method == 'POST':
        form = request.POST
        source1 = form.get('my_source1')
        source2 = form.get('my_source2')
        if source1=='db' and source2 =='db':

            return render(request,'screen.html')
        else:
            return HttpResponse('Value is not DB')


    else:

        return render(request,'home1.html')

def screen(request):
    print(request.method,"+++++")
    if request.method == 'POST':
        form = request.POST
        conid = form.get('conid')
        conpassword = form.get('conpassword')
        host = form.get('host')
        port = form.get('port')
        service_name = form.get('service_name')
        sql_query = form.get('sql_query')
        print(form)


        return HttpResponse(conid)

    else:

        return render(request,'screen.html')