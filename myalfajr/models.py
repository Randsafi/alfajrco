from django.db import models

# Create your models here.
x={
    'winter':'شتوي' ,
    'summer':'صيفي' ,
    'm':'موسمي' ,
    'kilo':'كلوات' ,
    'flower':'زهور' ,
}
class seeds(models.Model):
    name_s=models.CharField(max_length=225)
    catgory=models.CharField(choices=x ,default='m')
    img_url = models.URLField(max_length=500, blank=True)  # هون بدلنا بـ URLField
    classification = models.CharField(blank=True ,default="")
    descript = models.TextField(blank=True ,default="")
    def get_related_by_classification(self):
        """ ترجع بذور من نفس التصنيف """
        return seeds.objects.filter(
            classification=self.classification
        ).exclude(id=self.id)
 
    def __str__(self):
        return self.name_s
    
