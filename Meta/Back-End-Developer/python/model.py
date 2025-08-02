from django.db import models

class College(models.Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 
    
    
class Principal(models.Model): 
    # This model represents a Principal of a College
    # one-to-one relationship with College
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
    
    
"**************************************************************************"    
class Subject(models.Model):  # type: ignore
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField()
    
class Teacher(models.Model):  # type: ignore
    TeacherID = models.IntegerField(primary_key=True)
    subjectcode = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
    
    
"***************************************************************************"

class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
    
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField() 
    teacher = models.ManyToManyField(Teacher) 
    
"***************************************************************************"

class Student(CommonInfo): 
    # ... 
    class Meta(CommonInfo.Meta): 
        db_table = 'student_info'
        # This will create a table named 'student_info' in the database
        # we override the default table name to be more descriptive 