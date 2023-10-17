from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.core.paginator import Paginator


from .forms import AddMemberForm, ContactUsForm
from .models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    paginator = Paginator(mymembers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "all_members.html", {'mymembers':page_obj})


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    return render(request, "details.html", {"mymember": mymember})


def main(request):
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContactUsForm()
    context = {"form": form}
    return render(request, 'main.html',context)


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


def create_random_member():
    names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Isaac", "Jack",
         "Katie", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Samuel", "Taylor",
         "Ursula", "Victor", "Wendy", "Xander", "Yvonne", "Zachary"]
    
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Wilson", "Davis", "Miller", "Jones", "Garcia", "Rodriguez",
              "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Williams", "Lee", "Chen", "Kim", "Nguyen",
              "Singh", "Patel", "Ali", "Muller", "Schmidt", "Meyer", "Schneider", "Fischer", "Weber", "Schulz",
              "Schwarz", "Wong", "Chang", "Wang", "Li", "Chen", "Wu", "Liu", "Huang", "Li", "Kumar", "Rao", "Sharma",
              "Das", "Sen", "Choudhury", "Jha", "Banerjee"]

    print(len(names))
    print(len(last_names))
    for i in range(25):
        slug = f"{names[i]}-{last_names[i]}"
        new_member = Member(
            first_name=names[i], last_name=last_names[i], phone=7854127854, slug=slug
        )
        new_member.save()


