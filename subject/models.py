from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubjectTitle(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    subjecttitle = models.ForeignKey(SubjectTitle, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

class SubjectType(models.Model):
   
    name = models.CharField(max_length=255)
    subtopic = models.ForeignKey(Subject, on_delete=models.CASCADE)
    SUBJECT_TYPE_CHOICES = (
        ('local', 'Local'),
        ('global', 'Global'),
    )

    def __str__(self):
        return self.name

class UserSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    total_test_ball = models.FloatField()

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Step(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.title

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Club(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserClub(models.Model):
    user = models.CharField(max_length=100)
    club = models.CharField(max_length=255)




class ClubMeeting(models.Model):
    name = models.CharField(max_length=100)
    ##################################### validator
    location = models.URLField()
    date = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StepLesson(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class StepTest(models.Model):
    step = models.ForeignKey(Step, models.CASCADE)
    ball_for_each_test = models.FloatField()
    question_count = models.IntegerField()
    question_type = models.CharField(max_length=100, choices=[
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer')
    ])
    type = models.CharField(max_length=100, choices=[
        ('practice', 'Practice'),
        ('assessment', 'Assessment')
    ])
    time_for_question = models.IntegerField()


#########################################################################################   MODE

class TestQuestion(models.Model):
    steptest = models.ForeignKey(StepTest, models.CASCADE)
    text = models.TextField()

class TestAnswer(models.Model):
    testquestion = models.ForeignKey(TestQuestion, models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

#########################################################################################   QUESTIONTYPE




class UserTestResult(models.Model):
    testquestion = models.ForeignKey(TestQuestion, models.CASCADE)
    testanswer = models.ForeignKey(TestAnswer, models.CASCADE)

#########################################################################################   USER

class UserTestResult(models.Model):
    steptest = models.ForeignKey(StepTest, models.CASCADE)
    ball = models.FloatField()
    correct_ans = models.IntegerField()
    # testanswer = models.ForeignKey(TestAnswer, models.CASCADE) USER
