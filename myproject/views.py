from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from joblib import load
from ml_model.model import predict_cancer
from ml_model.train_model import train_and_save_model
from ml_model.graphs import generate_histograms, generate_correlation_heatmap, generate_summary_statistics, generate_top10_weights


# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def signup_view(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('password2')

        if(password != confirmpassword):
            messages.info(request, 'Passwords donot match')
            return render(request, 'signup.html')
        if(User.objects.filter(email=email).exists()):
            messages.info(request, 'Email already used')
            return render(request, 'signup.html')
        if(User.objects.filter(username=username).exists()):
            messages.info(request, 'Username already used')
            return render(request, 'signup.html')
            
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Invalid Credentials!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def stats_view(request):
    model_path = 'ml_model/logistic_regression_model.joblib'
    model = load(model_path)
    model_accuracy = train_and_save_model()

    img_base64_histograms = generate_histograms()
    img_base64_heatmap = generate_correlation_heatmap()
    img_base64_statistics = generate_summary_statistics()
    img_base64_top10_weights = generate_top10_weights()

    context = {
        'img_base64_histograms': img_base64_histograms,
        'img_base64_heatmap': img_base64_heatmap,
        'img_base64_statistics': img_base64_statistics,
        'img_base64_top10_weights': img_base64_top10_weights,
        'accuracy': model_accuracy * 100
    }

    return render(request, 'stats.html', context)

def main_view(request):
    return render(request, 'main.html')

def logout_view(request):
    auth.logout(request)
    return redirect('index')

def result_view(request):
    if(request.method == 'POST'):
        input_data = {
            "area_mean": request.POST.get('area_mean'),
            "concave points_mean": request.POST.get('concave_points_mean'),
            "concave points_worst": request.POST.get('concave_points_worst'),
            "concavity_worst": request.POST.get('concavity_worst'),
            "perimeter_mean": request.POST.get('perimeter_mean'),
            "perimeter_worst": request.POST.get('perimeter_worst'),
            "radius_mean": request.POST.get('radius_mean'),
            "radius_worst": request.POST.get('radius_worst'),
            "texture_mean": request.POST.get('texture_mean'),
            "texture_worst": request.POST.get('texture_worst')
        }

        model_path = 'ml_model/logistic_regression_model.joblib'
        model = load(model_path)

        prediction, probability = predict_cancer(input_data)

        model_accuracy = train_and_save_model()

        result = "Malignant" if prediction == 1 else "Benign"

        return render(request, 'result.html', {
            'result': result,
            'probability': probability,
            'accuracy': model_accuracy * 100
        })
    return render(request, 'result.html')
