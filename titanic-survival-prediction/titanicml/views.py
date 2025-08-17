from django.shortcuts import render
import pickle

def home(request):
    return render(request, "home.html")

def predict(pclass, sex, age, sibsp, parch, fare, C, Q, S):

    model = pickle.load(open("model/titanic_model.sav", "rb"))
    scaled = pickle.load(open("model/scaler.sav", "rb"))
    prediction = model.predict(
        scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]])
    )

    if prediction == 0:
        return "Not survived"
    elif prediction == 1:
        return "Survived"
    else:
        return "Error"

def result(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])
    embC = int(request.GET["embC"])
    embQ = int(request.GET["embQ"])
    embS = int(request.GET["embS"])

    result = predict(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, "home.html", {"result": result})
