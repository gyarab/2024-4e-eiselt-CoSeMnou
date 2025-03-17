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
    result = None
    if request.method == "POST":
        form = CompareForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            czech_score = form.cleaned_data["czech_score"]
            math_score = form.cleaned_data["math_score"]

            # Získání objektů škol podle ID
            first_school = School.objects.get(id=form.cleaned_data["first_choice"])
            second_school = School.objects.get(id=form.cleaned_data["second_choice"])
            third_choice_id = form.cleaned_data.get("third_choice")

            third_school = None
            if third_choice_id:  # Pokud uživatel vybral třetí školu
                third_school = School.objects.get(id=third_choice_id)

            results = []
            for school in [first_school, second_school, third_school]:
                if school:
                    meets_czech = czech_score >= school.min_czech_score
                    meets_math = math_score >= school.min_math_score
                    accepted = meets_czech and meets_math

                    results.append({
                        "school": school.name,
                        "required_czech": school.min_czech_score,
                        "required_math": school.min_math_score,
                        "meets_czech": meets_czech,
                        "meets_math": meets_math,
                        "accepted": accepted
                    })

            return render(request, "compare_results.html", {"form": form, "results": results})

    else:
        form = CompareForm()

    return render(request, "compare_results.html", {"form": form, "results": None})

