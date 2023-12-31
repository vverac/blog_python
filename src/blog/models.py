from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  TZ={
      ('EU', 'EUROPE'),
      ('AS', 'ASIA'),
      ('US', 'UNITED STATES'),
    }

  title = models.CharField( verbose_name='Titulo del posteo' , max_length=100)
  content = models.TextField(verbose_name='Texto del posteo',null=True, blank= True, default='texto de prueba')
  # User es una tabla cuando estamos usando ForeingKey
  autor=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor del posteo')
  created_at= models.DateTimeField(auto_now=True, verbose_name='Horario del posteo' )
  tzone=models.CharField(choices=TZ, verbose_name='Zona horaria')

  def __str__(self):
    # __str__ metodo para hacer una representacion de cadena
    return self.title

class Comment(models.Model):
  post=models.ForeignKey('Post', on_delete=models.CASCADE)
  author=models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  created_at= models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Comentario de {self.author.username} en {self.post.title}"




  