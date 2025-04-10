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
    img_s= models.ImageField(upload_to='imge',blank=True, max_length=255)

    def __str__(self):
        return self.name_s
    
