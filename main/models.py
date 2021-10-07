from django.db import models


class Procedures(models.Model):

    name = models.CharField('Назва', max_length=128, null=False)
    description = models.TextField('Опис', null=True)
    price = models.IntegerField('Ціна', null=False)
    procedure_time = models.IntegerField('Час виконання (хв)', null=False)

    def __str__(self):
        return self.name


class Record(models.Model):

    name = models.CharField('Ім`я', null=False, max_length=128)
    phone_number = models.CharField('Номер телефону', null=False, max_length=128)
    procedure = models.ManyToManyField(Procedures)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Records(models.Model):
    day = models.DateField('День')
    hour = models.TimeField('Час')
    record = models.ForeignKey(Record, default=None, on_delete=models.CASCADE)

    def __str__(self):
          return str(self.record)


class Blog(models.Model):

    title_name = models.CharField('Назва', max_length=128, null=False)
    short_text = models.CharField('Опис', max_length=256, null=True)
    text = models.TextField('Текст')
    posted_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_name

