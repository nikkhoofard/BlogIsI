from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from blog.models import Form
from blog.forms import SubjectForm,FormForm
# Create your views here.


def home_view(request):
    if request.method == "POST":
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_view")

    else:
        form = FormForm()
    return render(request, 'home.html', {'form': form})


'''
def home_view(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm()
        if form.is_valid():
            form = form(
                firs_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                field=form.cleaned_data["field"],
                degree=form.cleaned_data["degree"],
                subject=form.cleaned_data["subject"],
                phone_number=form.cleaned_data["phone_number"],
                summery=form.cleaned_data["summery"],
            )
            print("save")
            form.save()
            return HttpResponseRedirect(request.path_info)

    context={"form" : SubjectForm() }


    return render(request, "home.html", context)
'''