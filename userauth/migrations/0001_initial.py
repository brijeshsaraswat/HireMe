# Generated by Django 3.0.4 on 2020-03-18 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=15)),
                ('is_candidate', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='job_posted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('apply_by', models.DateTimeField()),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.employer')),
            ],
        ),
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=15)),
                ('is_candidate', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='applied_for',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.candidate')),
                ('job_applied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.job_posted')),
            ],
        ),
    ]
