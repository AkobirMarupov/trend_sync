from django.db import models
from django.contrib.auth import get_user_model

class BusinessPlan(models.Model):

    BUSINESS_TYPE_CHOICES = [
        ('dukon', 'Dukon'),
        ('uquv_markaz', 'Uquv markaz'),
        ('kompaniya', 'Kompaniya'),
        ('maktab', 'Maktab'),
        ('sartaroshxona', 'Sartaroshxona'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  
    budget = models.DecimalField(max_digits=12, decimal_places=2) 
    business_type = models.CharField(
        max_length=100, 
        choices=BUSINESS_TYPE_CHOICES,  
        blank=True,  
        null=True, 
    )
    custom_business_type = models.CharField(max_length=100, null=True, blank=True) 
    country = models.CharField(max_length=100) 
    expenses_breakdown = models.JSONField() 
    taxes = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Business Plan {self.id} for {self.user.username}"

    class Meta:
        verbose_name = 'Business Plan'
        verbose_name_plural = 'Business Plans'
