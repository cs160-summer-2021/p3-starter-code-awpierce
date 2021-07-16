from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def account(request):
    return render(request, 'coloring/account.html')

def setting(request):
    return render(request, 'coloring/setting.html')

def reference(request):
    return render(request, 'coloring/reference.html')

def sketch(request):
    return render(request, 'coloring/sketch.html')

def sketch_with_reference(request):
    return render(request, 'coloring/sketch_with_reference.html')