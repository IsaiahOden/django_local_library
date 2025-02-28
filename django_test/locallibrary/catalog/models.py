from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get url for specified
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

# Create your models here.
class Genre(models.Model):
    # Model Representing a book genre.
    name = models.CharField(
        max_length = 200,
        unique = True, #only one record for each genre
        help_text = "Enter a book genre(e.g. Science Fiction, French Poetry etc.)"
    )
    
    def __str__(self):
        # String for representing the Model Object
        return self.name
    
    def get_absolute_url(self):
        #Returns the url to access a particular genre instance
        return reverse('genre-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name = 'genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            )
        ]
    