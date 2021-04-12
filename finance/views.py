from django.shortcuts import render

# Create your views here.
def feeCollection(request):
    return render(request,'finance/feeColletion.html')

def feeDue(request):
    return render(request,'finance/feeDue.html')

def feeReport(request):
    return render(request,'finance/feeReport.html')
