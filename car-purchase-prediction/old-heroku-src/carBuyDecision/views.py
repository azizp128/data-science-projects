from django.shortcuts import render
from joblib import load
from django.http import HttpResponse

model = load('./assets/model/model.joblib')

def index(request):
    return render(request, 'index.html')

def predict(request):
    gender = request.GET.get("Gender", 0)
    age = int(request.GET.get("Age", 0))
    annualSalary = int(request.GET.get("AnnualSalary", 0))
    prediction = model.predict([[gender, age, annualSalary]])

    if prediction[0] == 0:
        return render(request, 'result_0.html')
    elif prediction[0] == 1:
        return render(request, "result_1.html")
    else:
        return HttpResponse("Error")