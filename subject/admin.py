from django.contrib import admin
from .models import Category, SubjectTitle, Subject, SubjectType, UserSubject, Vacancy, Step, Exam, Club, UserClub, ClubMeeting, StepLesson, StepTest,TestQuestion,TestAnswer,UserTestResult,UserTotalTestResult

admin.site.register(Category)
admin.site.register(SubjectTitle)
admin.site.register(Subject)
admin.site.register(SubjectType)
admin.site.register(UserSubject)
admin.site.register(Vacancy)
admin.site.register(Step)
admin.site.register(Exam)
admin.site.register(Club)
admin.site.register(UserClub)
admin.site.register(ClubMeeting)
admin.site.register(StepLesson)
admin.site.register(StepTest)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(UserTestResult)
admin.site.register(UserTotalTestResult)




