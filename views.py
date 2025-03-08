# frontend/views.py
from django.shortcuts import render, get_object_or_404
from .models import School, ExamResult
from django.shortcuts import render
from .models import School
from .forms import CompareForm

def homepage(request):
    return render(request, 'homepage.html')

def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})


def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    results = ExamResult.objects.filter(school=school)
    return render(request, 'school_detail.html', {'school': school, 'results': results})



def compare_results(request):
    form = CompareForm()
    results = None

    if request.method == "POST":
        form = CompareForm(request.POST)
        if form.is_valid():
            czech_score = form.cleaned_data['czech_score']
            math_score = form.cleaned_data['math_score']
            first_choice = form.cleaned_data['first_choice']
            second_choice = form.cleaned_data['second_choice']

            results = []
            for school in [first_choice, second_choice]:
                min_czech_score = school.min_czech_score
                min_math_score = school.min_math_score
                accepted = (czech_score >= min_czech_score and math_score >= min_math_score)

                results.append({
                    "school": school.name,
                    "required_czech": min_czech_score,
                    "required_math": min_math_score,
                    "accepted": accepted
                })

    return render(request, "compare_results.html", {"form": form, "results": results})
