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

def compare_results(request):
    if request.method == 'POST':
        selected_school_id = request.POST.get('school_id')
        user_math_score = int(request.POST.get('math_score'))
        user_czech_score = int(request.POST.get('czech_score'))
        
        # Načtení vybrané školy a minimálních požadavků
        school = School.objects.get(id=selected_school_id)
        min_scores = ExamResult.objects.filter(school=school).order_by('-year')[:5]  # posledních 5 let
        
        # Vyhodnocení, zda žák splňuje požadavky
        is_eligible = False
        for result in min_scores:
            if user_math_score >= result.min_score_math and user_czech_score >= result.min_score_czech:
                is_eligible = True
                break
        
        # Výstupní zpráva podle výsledků
        if is_eligible:
            message = f"Gratulujeme! S danými body byste se na školu '{school.name}' dostali."
        else:
            min_needed_math = min(min_scores, key=lambda x: x.min_score_math).min_score_math
            min_needed_czech = min(min_scores, key=lambda x: x.min_score_czech).min_score_czech
            message = f"Bohužel, potřebujete alespoň {min_needed_math} bodů z matematiky a {min_needed_czech} bodů z češtiny."
        
        return render(request, 'result_page.html', {'message': message, 'school': school})

    return render(request, 'compare_form.html', {'schools': School.objects.all()})
