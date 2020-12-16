from django.db import models

# Create your models here.
class Type(models.Model):

    name = models.CharField(max_length=200, help_text='Enter a food type (e.g. Asian)')
    
    def __str__(self):

        return self.name

from django.urls import reverse 

class Food(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    name = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the food")
    Cost = models.CharField('Cost',max_length=13, unique=True, help_text='Enter a cost of the food')
    Type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def _str_(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('food-detail', args=[str(self.id)])
import uuid # Required for unique book instances
from datetime import date 

from django.contrib.auth.models  import User


class Drink(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    name = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the drink")
    Cost = models.CharField('Cost',max_length=13, unique=True, help_text='Enter a cost of the drink')
    Type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def _str_(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('drink-detail', args=[str(self.id)])
import uuid # Required for unique book instances
from datetime import date 

from django.contrib.auth.models  import User



class Table(models.Model):

    number = models.CharField(max_length=200)
    
    def __str__(self):

        return self.number
    
    def get_absolute_url(self):

        return reverse('table-detail', args=[str(self.id)])

import uuid 

class TableInstance(models.Model):

    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Table availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set table as returned"),)   
        

    def _str_(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.table.number)
