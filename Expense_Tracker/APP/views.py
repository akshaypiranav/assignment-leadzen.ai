from django.shortcuts import render,redirect
from .models import Expense
 # Create your views here.
def index(request):
    if request.method=="POST":
        expense=request.POST["expense"]
        amount=request.POST["amount"]
        category=request.POST["category"]
        print(expense,amount,category)
        try:
            expense=Expense.objects.create(expense=expense,amount=amount,category=category)
            expense.save()
        except:
            pass
        
    try:
        expenseValue=Expense.objects.all()
        
    except:
        pass
        
    return render(request,"index.htm",{"data":expenseValue})


def update(request,id):
    if request.method=="POST":
        if (Expense.objects.filter(id=id).exists()):
            try:
                expenseDB=Expense.objects.get(id=id)
                expenseDB.expense=request.POST["expense"]
                expenseDB.amount=request.POST["amount"]
                expenseDB.category=request.POST["category"]
                expenseDB.save()
            except:
                pass
            return redirect('/')
        return redirect("/")

def delete(request,id):
    if (Expense.objects.filter(id=id).exists()):
        expenseDB=Expense.objects.get(id=id)
        expenseDB.delete()
        return redirect("/")

    return redirect("/")