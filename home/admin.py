from django.contrib import admin

from .models import Student, Book, BookRecord, Author, Manzil

# Register your models here.

admin.site.register(Manzil)
admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookRecord)




