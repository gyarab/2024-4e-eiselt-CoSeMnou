from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    min_czech_score_1 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z češtiny 1")
    min_czech_score_2 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z češtiny 2")
    min_czech_score_3 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z češtiny 3")
    min_math_score_1 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z matematiky 1")
    min_math_score_2 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z matematiky 2")
    min_math_score_3 = models.IntegerField(blank=True, null=True, verbose_name="Minimální skóre z matematiky 3")

    def __str__(self):
        return self.name

    # vypocet prumeru z minimalnich skore
    @property
    def avg_czech_score(self):
        scores = [self.min_czech_score_1, self.min_czech_score_2, self.min_czech_score_3]
        valid = [s for s in scores if s is not None]
        if valid:
            return sum(valid) / len(valid)
        return None

    # vypocet prumeru z minimalnich skore
    @property
    def avg_math_score(self):
        scores = [self.min_math_score_1, self.min_math_score_2, self.min_math_score_3]
        valid = [s for s in scores if s is not None]
        if valid:
            return sum(valid) / len(valid)
        return None


    

class Student(models.Model):
    name = models.CharField(max_length=100)
    czech_score = models.IntegerField()
    math_score = models.IntegerField()

    first_choice = models.ForeignKey(
        'School', related_name='first_choice_students', on_delete=models.CASCADE
    )
    second_choice = models.ForeignKey(
        'School', related_name='second_choice_students', on_delete=models.CASCADE
    )
    third_choice = models.ForeignKey(
        'School', related_name='third_choice_students', on_delete=models.CASCADE,
        null=True, blank=True 
    )

    def total_score(self):
        return self.czech_score + self.math_score

    def __str__(self):
        return self.name



class ExamResult(models.Model):
    student_name = models.CharField(max_length=100)
    czech_score = models.IntegerField()
    math_score = models.IntegerField()

    def total_score(self):
        return self.czech_score + self.math_score

    def __str__(self):
        return f"{self.student_name} - {self.total_score()}"
