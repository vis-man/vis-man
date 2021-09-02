from django.shortcuts import render


def home(request):
    context = {
        'title': 'Visitor Management System'
    }
    return render(request, 'survey/home.html', context)

def gingin(request):
    context = {
        'title': 'Gingin Gravity Precinct'
    }
    return render(request, 'survey/form.html', context)
def iomrc(request):
    context = {
        'title': 'IOMRC Crawley'
    }
    return render(request, 'survey/form.html', context)
def watermans(request):
    context = {
        'title': 'Watermans Bay'
    }
    return render(request, 'survey/form.html', context)
def ridgefield(request):
    context = {
        'title': 'Ridgefield Farm'
    }
    return render(request, 'survey/form.html', context)
    