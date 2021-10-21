from django.shortcuts import render, redirect


def view404(request, *args, **kwargs):
  return render(request, "includes/page_404.html", status=404)

def view500(request, *args, **kwargs):
  return render(request, "includes/page_500.html", status=500)

def viewAbout(request, *args, **kwargs):
  return render(request, "contents/about.html", {})

def viewLogout(request, *args, **kwargs):
  return render(request, "contents/about.html", {})

def viewSignup(request, *args, **kwargs):
  return render(request, "contents/about.html", {})

def viewSignin(request, *args, **kwargs):
  return render(request, "contents/about.html", {})
