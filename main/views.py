from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'project_1_images': [f'assets/img/portfolio/project-1/{i}.jpeg' for i in range(1, 19)],
        'project_2_images': [f'assets/img/portfolio/project-2/{i}.jpeg' for i in range(1, 46)],
        'project_3_images': [f'assets/img/portfolio/project-3/{i}.jpeg' for i in range(1, 164)],
        'project_4_images': [f'assets/img/portfolio/project-4/{i}.jpeg' for i in range(1, 111)],
        'job_1_images': [f'assets/img/portfolio/job-1/{i}.jpeg' for i in range(1, 6)],
        'job_2_images': [f'assets/img/portfolio/job-2/{i}.jpeg' for i in range(1, 25)],
    }    
    return render(request, 'main/index.html', context)