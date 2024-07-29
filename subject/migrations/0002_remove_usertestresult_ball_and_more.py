# Generated by Django 5.0.7 on 2024-07-29 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertestresult',
            name='ball',
        ),
        migrations.RemoveField(
            model_name='usertestresult',
            name='correct_ans',
        ),
        migrations.RemoveField(
            model_name='usertestresult',
            name='steptest',
        ),
        migrations.AddField(
            model_name='usertestresult',
            name='testanswer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.testanswer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertestresult',
            name='testquestion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.testquestion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertestresult',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserTotalTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.FloatField()),
                ('correct_ans', models.IntegerField()),
                ('steptest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.steptest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]