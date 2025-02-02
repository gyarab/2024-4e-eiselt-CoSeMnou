# frontend/views.py
from django.shortcuts import render, get_object_or_404
from .models import School, ExamResult

def homepage(request):
    return render(request, 'homepage.html')

def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})


def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    results = ExamResult.objects.filter(school=school)
    return render(request, 'school_detail.html', {'school': school, 'results': results})

from django.shortcuts import render
from .forms import StudentForm
from .models import School

def compare_results(request):
    result = None
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.total = student.total_score()
            student.save()
            # Získání bodů škol
            first_school = student.first_choice
            second_school = student.second_choice
            first_result = student.total_score() >= first_school.minimum_points
            second_result = student.total_score() >= second_school.minimum_points
            result = {
                'first_school': first_school,
                'second_school': second_school,
                'first_result': first_result,
                'second_result': second_result,
            }
    else:
        form = StudentForm()
    return render(request, 'compare_results.html', {'form': form, 'result': result})

