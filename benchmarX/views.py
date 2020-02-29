from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(response):
    return render(response, "benchmarX/home.html", {})

@login_required
#Tips : passer des paramètres aux templates : https://www.youtube.com/watch?v=b0CgA_Ap_Mc&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=4&t=720
def redtools(response):
    return render(response, "benchmarX/red-tools.html", {})


@login_required
def bluetools(response):
    return render(response, "benchmarX/blue-tools.html", {"name": "This is the offensive tools page !"})
