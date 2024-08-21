from django.db import models

class aeye_inference_models (models.Model):
    whoami    = models.CharField(max_length=40)
    message   = models.CharField(max_length=40)
    image     = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class aeye_database_read_models (models.Model):
    whoami = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    request_data = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class aeye_database_write_models (models.Model):
    whoami = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    request_data = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class aeye_database_list_models (models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    profileImage = models.URLField(max_length=255)
    numberOfVisits = models.IntegerField()
    recentVisitDate = models.DateField()
    severityPercentage = models.CharField(max_length=10)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class aeye_Checkup_models (models.Model) :
    patient = models.ForeignKey(aeye_database_list_models, related_name='checkups', on_delete=models.CASCADE)
    date = models.DateField()
    symptom = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class aeye_UltrasoundImage_models (models.Model):
    checkup = models.ForeignKey(aeye_Checkup_models, related_name='ultrasoundImages', on_delete=models.CASCADE)
    imageUrl = models.URLField(max_length=255)
     
    def __str__(self):
        return self.imageUrl


class aeye_Report_models (models.Model):
    checkup = models.OneToOneField(aeye_Checkup_models, related_name='report', on_delete=models.CASCADE)
    ai_diagnosis = models.CharField(max_length=255)
    ai_probability = models.CharField(max_length=10)
    doctor_diagnosis = models.TextField()