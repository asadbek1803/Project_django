from django.db import models

# Create your models here.
# Salom

class Manzil(models.Model):
    student_id = models.IntegerField(default=1)
    shahar = models.CharField(max_length=45)
    tuman = models.CharField(max_length=45)
    qishloq = models.CharField(max_length=45, null=True, blank=True)
    kocha = models.CharField(max_length=45)
    uy = models.CharField(max_length=45)

    def __str__(self):
        self.student_id

class Student(models.Model):
    genders = (
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other")
    )
    name = models.CharField(max_length=100)
    profile_image = models.FileField(blank=True,null=True, upload_to='Images')
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(max_length=1, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=genders, blank=True, null=True)




    def __str__(self):
        return self.name

    def salom(self):
        return 'salom'

class Author(models.Model):
    genders = (
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other")
    )
    name = models.CharField(max_length=100)
    is_alive = models.BooleanField(max_length=1)
    profile_image = models.FileField(null=True, upload_to='Images')
    gender = models.CharField(max_length=6,choices=genders)
    email = models.EmailField(null=True, blank=True)

    books = models.TextField()


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.SmallIntegerField(default=2023)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    page = models.PositiveSmallIntegerField(default=60)
    is_there = models.BooleanField(max_length=2)

    def __str__(self):
        return self.title



class BookRecord(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    when = models.DateTimeField()
    to_time = models.SmallIntegerField(default=2)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.student_name.name} book name: {self.book_name.title} time: {self.to_time}"


    def salom_ber(self):
        return "alik"