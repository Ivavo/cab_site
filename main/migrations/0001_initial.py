# Generated by Django 3.2.7 on 2021-09-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('title_name', models.CharField(max_length=128, verbose_name='Назва')),
                ('text', models.TextField(verbose_name='Текст')),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=128, verbose_name='Назва')),
                ('description', models.TextField(null=True, verbose_name='Опис')),
                ('price', models.IntegerField(verbose_name='Ціна')),
                ('procedure_time', models.IntegerField(verbose_name='Час виконання (хв)')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=128, verbose_name='Ім`я')),
                ('phone_number', models.CharField(max_length=128, verbose_name='Номер телефону')),
                ('price', models.IntegerField()),
                ('procedure', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.procedures')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='День')),
                ('hour', models.TimeField(verbose_name='Час')),
                ('record', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.record')),
            ],
        ),
    ]