from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AddBookForm,AddStudentForm
from .models import addbook,addstudent
from django.contrib import messages
# Create your views here.
def index(request):
    book=addbook.objects.all()
    return render(request, 'index.html',{'book':book})

def addbookfun(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Added successfully")
            return redirect("/")
        else:
            b = AddBookForm()
            #messages.success(request, "Something Wrong happened Please try again")
            return render(request, 'addbook.html',{'b':b})
    else:
        b=AddBookForm()
        return render(request, 'addbook.html',{'b':b})

def addstudentfun(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added successfully")
            return redirect("/")
        else:
            s=AddStudentForm()
            return render(request, 'addstudent.html',{'s':s})
    else:
        s=AddStudentForm()
        return render(request, 'addstudent.html',{'s':s})

def borrow(request,myid):
    obj = get_object_or_404(addbook, id=myid)
    form = AddBookForm(request.POST or None ,request.FILES or None ,instance=obj)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully Borrowed the Book")
        return redirect('/')
    else:
        # messages.success(request, "Something went wrong please try again")
        return render(request,'borrow.html' , {'info':form})

def updatebook(request,myid):
    obj = get_object_or_404(addbook, id=myid)
    form = AddBookForm(request.POST or None ,request.FILES or None ,instance=obj)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully Updated the Book Details")
        j="/learnmore/"+str(myid)
        return redirect(j)
    else:
        # messages.success(request, "Something went wrong please try again")
        return render(request,'updatebook.html' , {'info':form})
    
def learnmore(request,myid):
    b=addbook.objects.filter(id=myid)
    return render(request, "bookinfo.html", {'b':b[0]})
        #return render(request, 'info.html',{'shop':sp})   

def showstudent(request):
    s=addstudent.objects.all()
    return render(request, 'showstudent.html', {'s':s})

def studentupdate(request, myid):
    obj = get_object_or_404(addstudent, id=myid)
    form = AddStudentForm(request.POST or None ,request.FILES or None ,instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully updated the Details")
        context = {'form': form}
        return redirect('/showstudent')
    else:
        return render(request,'updatestudent.html' , {'info':form})
    
def studentdelete(request,myid):
    myid=int(myid)
    t=addstudent()
    b=addbook.objects.filter(student_id=myid)
    #b.student=None
    for i in b:
        print(i)
        i.student=None
        i.save()
    t.id=myid
    #b.save()
    t.delete()
    messages.success(request, "You successfully Deleted the Student")
    return redirect('/showstudent')

def bookdelete(request,myid):
    myid=int(myid)
    t=addbook()
    t.id=myid
    t.delete()
    messages.success(request, "You successfully Deleted the Book")
    return redirect('/')