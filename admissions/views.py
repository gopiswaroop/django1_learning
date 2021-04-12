from django.shortcuts import render
from admissions.models import student
from admissions.forms import StudentModelForm
from admissions.forms import vendorform
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html')


def logoutuser(request):
    return render(request, 'logout.html')


@login_required
def addadmin(request):
    form = StudentModelForm
    studentform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request, 'admissions/addadmin.html', studentform)


@login_required
def adminreport(request):
    # get all records from student table
    result = student.objects.all();  # select * from students
    # store it in dictionary
    students = {'allstudents': result}
    return render(request, 'admissions/adminreport.html', students)


@login_required
def addvendor(request):
    form = vendorform
    vform = {'form': form}

    if request.method == 'POST':
        form = vendorform(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['address']
            c = form.cleaned_data['contact']
            i = form.cleaned_data['item']
            response = render(request,'index.html')
            # response.set_cookie("name",n)
            # response.set_cookie("address",a)
            # response.set_cookie("contact",c)
            # response.set_cookie("item",i)
            request.session['name'] = n
            request.session['address'] = a
            request.session['contact'] = c
            request.session['item'] = i

        return response
    return render(request, 'admissions/addvendor.html', vform)


@login_required
@permission_required('admissions.delete_student')
def deletestudent(request, id):
    s = student.objects.get(id=id)
    s.delete()
    return adminreport(request)


@login_required
@permission_required('admissions.change_student')
def updatestudent(request, id):
    s = student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form': form}
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return adminreport(request)
    return render(request, 'admissions/update-admission.html', dict)


class FirstClassView(View):
    def get(self, request):
        return HttpResponse("<h1>hello ...this is my first class</h1>")


class TeacherRead(ListView):
    model = Teacher


class getTeacher(DetailView):
    model = Teacher


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name', 'exp', 'subject', 'contact')


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name', 'contact')


class RemoveTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')
