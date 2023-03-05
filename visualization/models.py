from django.db import models


# Create your models here.
class AnnualData(models.Model):
    year = models.CharField(max_length=100)
    students = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Annual year placement report'

    def __str__(self):
        return f'{self.year}-{self.students}'

class DepartmentData(models.Model):
    Department = models.CharField(max_length=100)
    students2 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Departmentwise placement report'

    def __str__(self):
        return f'{self.Department}-{self.students2}'

class CategaryData(models.Model):
    categary = models.CharField(max_length=100)
    students3 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Categarywise placement report'

    def __str__(self):
        return f'{self.categary}-{self.students3}'

class companyData(models.Model):
    company = models.CharField(max_length=100)
    students4 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Companywise placement report'

    def __str__(self):
        return f'{self.company}-{self.students4}'

class GenderData(models.Model):
    gender = models.CharField(max_length=100)
    students5 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Genderwise placement report'

    def __str__(self):
        return f'{self.gender}-{self.students5}'

class PlacedData(models.Model):
    placed = models.CharField(max_length=100)
    students6 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'placed & unplaced placement report'

    def __str__(self):
        return f'{self.placed}-{self.students6}'
