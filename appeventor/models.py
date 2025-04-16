from django.db import models
# from django.contrib.auth.models import User 
# Create your models here.
class datadesire(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    
class user_query(models.Model):
    # user=models.ForeignKey(userclient,on_delete=models.CASCADE)
    Q_email=models.EmailField()
    query=models.CharField(max_length=200)

class adminuser(models.Model):
    name=models.CharField(max_length=20)
    is_read = models.BooleanField(default=False)
    username=models.EmailField()
    password=models.CharField(max_length=16)
    suggestion=models.TextField(null=True)
    
    def __str__(self):
        return self.username


class FakePayment(models.Model):
    user = models.ForeignKey(datadesire, on_delete=models.CASCADE, related_name="payments",null=True) 
    name = models.CharField(max_length=100)
    event=models.CharField(max_length=200,null=True)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')], default='Success')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.transaction_id}"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=12)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserDocument(models.Model):
    DOCUMENT_TYPES = [
        ('Pan card', 'Pan card'),
        ('National ID', 'National ID'),
    ]
    user = models.ForeignKey(datadesire, on_delete=models.CASCADE, related_name="documents")  
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)  
    document_file = models.FileField(upload_to="documents/")  
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.email} - {self.document_type}"
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.CharField(max_length=12)
    company=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    typeofevent=models.CharField(max_length=100)
    dateprimary=models.DateField()
    datesecondary=models.DateField()
    abouttheevent=models.TextField()

    def __str__(self):
        return self.name

class inquiry(models.Model):
   
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

