from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import AddMemberForm
from .models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    return render(request, "all_members.html", {"mymembers": mymembers})


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    return render(request, "details.html", {"mymember": mymember})


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    members = Member.objects.all().order_by("first_name", "-id").values()
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
        "greeting": 1,
        "members": members,
    }
    return HttpResponse(template.render(context, request))


# def add_member(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         phone_num = request.POST.get("phone_num")
#         slug = f"{first_name}-{last_name}"
#         new_member = Member(
#             first_name=first_name, last_name=last_name, phone=phone_num, slug=slug
#         )
#         new_member.save()
#         return redirect("/members")
#     return render(request, "add_member.html", {"data": 1})


def add_new_member(request):
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/members")
    else:
        # This is a GET request, so create an empty form
        form = AddMemberForm()

    context = {"form": form}
    return render(request, "add_member_sample.html", context)


def update_member_details(request, id):
    obj = get_object_or_404(Member, id=id)
    if request.POST:
      form = AddMemberForm(request.POST, instance=obj)
      if form.is_valid():
          form.save()
          return redirect("/members")
    else:
        form = AddMemberForm(instance=obj)
    return render(request, "add_member_sample.html",{'form':form})


def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect("/members")
