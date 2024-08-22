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
    

class aeye_database_patient_models (models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    profileImage = models.URLField(max_length=255)
    numberOfVisits = models.IntegerField()
    recentVisitDate = models.DateField()
    severityPercentage = models.CharField(max_length=10)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class aeye_database_checkup_models (models.Model):
    patientId = models.ForeignKey(aeye_database_patient_models, related_name='checkups', on_delete=models.CASCADE)
    date = models.DateField()
    symptom = models.TextField()
    status = models.CharField(max_length=20)
    ultrasound_image = models.JSONField()
    ai_diagnosis = models.CharField(max_length=255)
    ai_probability = models.CharField(max_length=10)
    doctor_diagnosis = models.TextField()

    def __str__(self):
        return self.name