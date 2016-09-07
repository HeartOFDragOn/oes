from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.CharField(max_length = 20)
    question_name = models.CharField(max_length = 200)
    question_correct_answer = models.CharField(max_length = 5)
    question_answer_a = models.CharField(max_length = 100)
    question_answer_b = models.CharField(max_length = 100)
    question_answer_c = models.CharField(max_length = 100)
    question_answer_d = models.CharField(max_length = 100)

    question_created_time = models.DateTimeField()
    question_updated_time = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'question'
        db_table = 'question'
