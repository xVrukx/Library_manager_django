from django.db import models
from django.core.exceptions import ValidationError

class Member(models.Model):
    name = models.CharField(max_length=100, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.title

class borrow(models.Model):
    Name = models.ForeignKey(Member, on_delete=models.CASCADE)
    Books = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_data = models.DateField(auto_now_add=True)

    def borrow(self,*value, **keyvalue):
        if not self.pk:
            if self.Book.quantity <=0:
                raise ValidationError (f'warning:no copies of{ self.Books.title} is available')
            
            self.Books.quantity -=1
            self.Books.save()

        super().save(*value,**keyvalue)

    def return_(self, *value, **keyvalue):
        self.Books.quantity +=1
        self.Books.save()

        super().save(*value,**keyvalue)