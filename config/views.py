# from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, "main.html")

#p.48
def burger_list(request):
    return render(request, "burger_list.html")