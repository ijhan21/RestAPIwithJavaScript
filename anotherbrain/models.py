from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20) # ADP, ADsP, ....

class SubCategory(models.Model)    :
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_subcategory')
    name = models.CharField(max_length=50) # chap1, 2, 3 ....

# site/question/<subcategory>/ => return question+answer set
class Dataset(models.Model): 
    # 분류
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, related_name='subcategory_dataset')    
    question = models.TextField()
    answers = models.JSONField(default ='{}')
    accuracy_rate = models.FloatField(default=0.0)    
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "dataset"