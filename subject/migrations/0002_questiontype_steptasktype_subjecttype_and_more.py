# Generated by Django 5.0.7 on 2024-07-26 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MULTIPLE', 'Multiple'), ('SINGLE', 'Single')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='StepTaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LOCAL', 'Local'), ('GLOBAL', 'Global')], max_length=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='student',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='subtopic',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject',
        ),
        migrations.AddField(
            model_name='category',
            name='clicked_count',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ClubMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('date', models.DateField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.club')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('description', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StepTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball_for_each', models.FloatField()),
                ('title', models.CharField(max_length=255)),
                ('time_for_quest', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.steptasktype')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.stop')),
            ],
        ),
        migrations.CreateModel(
            name='StopLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.stop')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.category')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.subjecttitle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.subjecttype'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('step_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.steptask')),
            ],
        ),
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.testquestion')),
            ],
        ),
        migrations.CreateModel(
            name='UserClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_test_ball', models.FloatField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.testanswer')),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.testquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTotalTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.FloatField()),
                ('correct_ans', models.JSONField()),
                ('step_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.steptask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='Subtopic',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
