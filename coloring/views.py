from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def account(request):
    return render(request, 'coloring/account.html')

def setting(request):
    return render(request, 'coloring/setting.html')

def mandela(request):
    return render(request, 'coloring/mandela.html')

def reference(request):
    return render(request, 'coloring/reference.html')

def asreference(request):
    return render(request, 'coloring/asreference.html')

def sketch(request):
    return render(request, 'coloring/sketch.html')

def sketch_as_reference(request):
    return render(request, 'coloring/sketch_as_reference.html')

def sketch_with_reference(request):
    return render(request, 'coloring/sketch_with_reference.html')