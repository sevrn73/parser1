from django.shortcuts import render

def main(request):
    print(request.FILES['myfile'])
    return render(request, 'main.html')
