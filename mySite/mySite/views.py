from django.shortcuts import render, HttpResponse

# Create your views here.
def service(request):
    
    # return HttpResponse("chatbot")
    return render(request, "service.html")

def community(request):
    
    # return HttpResponse("chatbot")
    return render(request, "community.html")

