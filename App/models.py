from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Prime(models.Model):
    employer = models.ForeignKey('auth.User',related_name='primes',on_delete=models.CASCADE)
    article = models.ForeignKey('Article',related_name='primes_article',on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    justif = models.ImageField(blank=True, null=True)

    ENATTENT = 'En attent'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    
    STATE_CHOICES = [
        (ENATTENT, 'En attent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        
    ]
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=ENATTENT,
    )


    def __str__(self):
        return (self.employer.username + " " +self.article.name)
    
    def get_absolute_url(self):
        return reverse("prime_list")
       # return reverse("prime_list",kwargs={'pk':self.pk})


class Article(models.Model):
    name = models.CharField(max_length=200)
    montant = models.IntegerField()

    def __str__(self):
        return self.name


