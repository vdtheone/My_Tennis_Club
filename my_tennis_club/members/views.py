from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from .forms import AddMemberForm, ContactUsForm
from .models import Member


# Create your views here.
@login_required(login_url="/")
def members(request):
    mymembers = Member.objects.all().values()
    paginator = Paginator(mymembers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "all_members.html", {"mymembers": page_obj})


@login_required(login_url="/")
def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    return render(request, "details.html", {"mymember": mymember})


def main(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContactUsForm()
    context = {"form": form}
    return render(request, "main.html", context)


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


@login_required(login_url="/")
def add_new_member(request):
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            slug = f"{first_name}-{last_name}"
            contact = form.save(commit=False)
            contact.slug = slug
            contact.save()
            return redirect("/members")
    else:
        # This is a GET request, so create an empty form
        form = AddMemberForm()

    context = {"form": form}
    return render(request, "add_member_sample.html", context)


@login_required(login_url="/")
def update_member_details(request, id):
    obj = get_object_or_404(Member, id=id)
    if request.POST:
        form = AddMemberForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/members")
    else:
        form = AddMemberForm(instance=obj)
    return render(request, "add_member_sample.html", {"form": form})


@login_required(login_url="/")
def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect("/members")


def logout_user(request):
    logout(request)
    return redirect("/")
