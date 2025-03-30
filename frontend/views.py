from django.shortcuts import render, get_object_or_404
from .models import School, ExamResult
from django.shortcuts import render
from .models import School
from .forms import CompareForm

# zobrazeni uvodni stranky
def homepage(request):
    return render(request, 'homepage.html')

# zobrazeni seznamu skol
def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})

# detailni stranka skoly
def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    results = ExamResult.objects.filter(school=school)
    return render(request, 'school_detail.html', {'school': school, 'results': results})

# zpracovani porovnani vysledku
def compare_results(request):
    result = None
    if request.method == "POST":
        form = CompareForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            czech_score = form.cleaned_data["czech_score"]
            math_score = form.cleaned_data["math_score"]

            # ziskani skol podle ID
            first_school = School.objects.get(id=form.cleaned_data["first_choice"])
            second_school = School.objects.get(id=form.cleaned_data["second_choice"])
            third_choice_id = form.cleaned_data.get("third_choice")

            third_school = None
            if third_choice_id:
                third_school = School.objects.get(id=third_choice_id)

            # vytvoreni seznamu s vysledky porovnani
            results = []
            for school in [first_school, second_school, third_school]:
                if school:
                    avg_czech = school.avg_czech_score if school.avg_czech_score is not None else 0
                    avg_math = school.avg_math_score if school.avg_math_score is not None else 0

                    meets_czech = czech_score >= avg_czech
                    meets_math = math_score >= avg_math
                    accepted = meets_czech and meets_math

                    results.append({
                        "school": school.name,
                        "avg_czech": avg_czech,
                        "avg_math": avg_math,
                        "meets_czech": meets_czech,
                        "meets_math": meets_math,
                        "accepted": accepted
                    })

            return render(request, "compare_results.html", {"form": form, "results": results})
    else:
        form = CompareForm()

    return render(request, "compare_results.html", {"form": form, "results": None})