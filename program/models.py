from django.db import models
from user.models import User
# Create your models here.


class Program(models.Model):
    Program_name = models.CharField(max_length=100, primary_key=True)
    Program_giturl = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')


class Test(models.Model):
    Test_id = models.AutoField(primary_key=True)
    Test_file_addr = models.CharField(max_length=100)

    test_types_choices = (
        (0, "Checkstyle"),
        (1, "FindBugs"),
        (2, "submit")
    )

    Test_type = models.SmallIntegerField(verbose_name="type", choices=test_types_choices)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    Test_text = models.TextField(verbose_name="text",default = "default")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='Program')
    result_file_loc = models.CharField(max_length=100)





