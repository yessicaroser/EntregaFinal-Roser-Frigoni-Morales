Entrega final para proyecto final del curso Python (orientado al desarrollor web) de Coderhouse

Participantes: Yessica Roser/ Gino Frigoni/ Constanza Morales/
<br/>

<h1>Primera entrega del Proyecto Final</h1>

<li> Video: </li>

<br/>

<h3>Indice: </h3>
<b><strong>Templates</strong></b>:

<li> Home </li>
<li> About </li>
<li> Blog </li>
<li> Registro </li>
<li> Login </li>
<li> Editar Perfil </li>
<li> Post Form </li>
<li> Post Detail </li>
<li> Post Draft List </li>
<li> Comment form </li>


<br>

<b>Modelos</b>:
<li> Modelo de Publicacion (blog) - App </li>
<li> Modelo para Registro/logueo/editar perfil (AppRegistro) - App</li>

<br>
<b>Formularios</b>:
<li> Formulario de blog (app) </li>
<li> Formulario de AppRegistro (app)  </li>

<br>
<b>Funcionalidades</b>:
<li> Registo de usuarios </li>
<li> Logueo de usuarios </li>
<li> Crear posteos </li>
<li> Editar posteos </li>
<li> Eliminar posteos </li>
<li> Ver posteos </li>
<li> Ver borradores </li>
<li> Modificar perfil </li>
<li> Agregar comentarios a posteos </li>

<br>
<b>Usuarios con permisos de Admin</b>:
<li> frigoni </li>
<li> Yessica  </li>
<br>
<br>
<b>Instalación</b>:
<li>Pasos para utilizar el archivo</li>
<br><br>
<h2>Templates</h2>
<br>
1. Templates / Home:

![home](https://user-images.githubusercontent.com/110737647/204418672-dadaeb5f-1d15-49f7-bf65-3650b5d6d589.jpg)
El Navbar cuenta con links que redirigen a la navegación por el blog(home/about/blog), el acceso de nuevos usuarios por medio de un registro y el logueo de usuarios ya establecidos.<br>
El header ofrece información sobre la temática del blog.
<br><br><br><br>

2. Templates / About:
![about](https://user-images.githubusercontent.com/110737647/204419203-c33ce090-7cec-4832-8ca5-82739a890693.jpg)
El header indica el nombre de la página y finalidad.<br>
Se menciona a cada participante del proyecto y una breve descripción que los caracteriza.
<br><br><br><br>

3. Templates / Blog:
![blog](https://user-images.githubusercontent.com/110737647/204420064-cd0b21e6-b3f0-45f8-8179-cb56d2497291.jpg)
En el template Blog se visualiza los artículos publicados, destacando su titulo y la fecha de publicación como información inicial. El usuarip puede acceder a su contenido clikeando sobre el titulo elegido.
<br><br><br><br>

4. Templates / Registro:
![registro](https://user-images.githubusercontent.com/110737647/204420234-89ad2f1d-d8fd-4161-915e-09f9d2f9d7f7.jpg)
El template de registro ofrece una formulario con una vista limpia, sin distracciones visuales.<br>
Como mejora se podría considerar agregar el logo que identifica al blog o el nombre del mismo y utilizar la misma paleta cromática que poseen los botones y otros elementos de interacción para generar una identidad visual homogénea. <br>
<br><br><br><br>

5. Templates / Login:
![login](https://user-images.githubusercontent.com/110737647/204420338-4797ab2b-99a5-4d71-94f5-4b236105bb32.jpg)
Presenta las misma estructura que el registro. Para el acceso se solicita el username y la contraseña generada.<br>
Ofrece la opción de registro para aquellos que aún no tienen una cuenta e ingresaron a esta opción por equivocación.
<br><br><br><br>

6. Templates / Editar Perfil:
![panel_profile](https://user-images.githubusercontent.com/110737647/204420517-5a1de2ec-3e40-4b25-8eb1-d8af3ff5d362.jpg)
Una vez que el usuario se loguea puede acceder desde la barra de navegación a la opción de "Editar perfil" que lo redirigirá al panel de control del blog. Podrá:
<br>
Editar perfil: Modificar sus datos personales, cargar o modificar la imagen de perfil y agregar/editar un breve texto a su biografía.<br>
Desde ese panel también podrá crear nuevos artículos, ver artículos ya publicados y sus borradores. Actualmente estas opciones redirigen a formularios y templates del blog. Como mejora se podría crear vistas dentro del dashboard para generar estas acciones dentro de este entorno visual.<br>
<br><br><br><br>

7. Templates / Artículo nuevo (Post Form):
![articulo_nuevo](https://user-images.githubusercontent.com/110737647/204420897-61995d58-4633-483b-bea0-f0a6c5e119d6.png)
El formulario de edición/creación de nuevos artículos cuenta con un editor visual de texto enriquecido que ofrece múltiples funcionalidades para crear bloques personalizados e incorporar imágenes.<br>
Como mejora se debería identificar al usuario logueado y la publicación creada se vincule automáticamente a su perfil de usuario. 
<br><br><br><br>

8. Templates / Artículos (Post Detail):
![articulos](https://user-images.githubusercontent.com/110737647/204421060-95713e39-245b-4f33-a191-5bfef04929f7.jpg)
La estructura implementada se corresponde a los blogs tradicionales: titulo, imagen de portada, autor, fecha de creación, y cuerpo con texto y/o imagenes.<br>
Al pie del artículo se puede visualizar el avatar de perfil del autor con su username y el texto de biografía ingresado desde el panel de edición de perfil.
<br><br><br><br>

9. Templates / Borradores (Post Fraft List):
![borradores](https://user-images.githubusercontent.com/110737647/204421668-61eba303-38e0-4420-8cd4-54a25c2d30d9.jpg)
En este espacio se visualizan los artículos que el usuario no publicó. Aparecerán en forma de lista ordenada por fecha de creación. 
<br><br><br><br> 

10. Templates / Comentarios (Comment Form):
![form_comentario](https://user-images.githubusercontent.com/110737647/204421839-0e7673cf-569d-4ea2-8e17-7ec7e5cca22c.jpg)
Debajo de la descripción del autor de la publicación figuran los comentarios en orden por fecha de creación. Para agregar un nuevo comentario se requiere que el usuario se encuentre logueado previamente.
<br><br><br><br>

<h2>Modelos</h2>
1. Modelo de Publicacion/ (blog) - App
<br>

class Post(models.Model):
 
    titulo = models.CharField(max_length=100)
    imagen_portada = models.ImageField(default='default.jpg', upload_to='images/', null=True, blank=True)
    contenido = RichTextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars/', null=True)
   
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comentario.filter(comentario_aprobado=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.titulo
        
class Comment(models.Model):
 
    post = models.ForeignKey('blog.Post', related_name='comment', on_delete=models.CASCADE)
    autor = models.CharField(max_length=200)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def approve(self):
        self.comentario_aprobado = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.comment


<br>
<br>
2. Modelo para Registro/logueo/editar perfil (AppRegistro) - App
<br><br>
class Users(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
<br>
<br>
<h2>Formularios</h2>
<h3>Formulario de blog (app)</h3>
 
class PostForm(forms.ModelForm):
 
    class Meta:
 
        model = Post
        fields = ('autor', 'titulo', 'contenido', 'imagen_portada')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.TextInput(attrs={'class': 'form-control'}),
            'Autor' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder','type': 'hidden'}),
            
        }




class CommentForm(forms.ModelForm):
 
    class Meta:
 
        model = Comment
        fields = ('autor', 'comentario',)

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'textinputclass'}),
            'comentario': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
 
<br>
<h3>Formulario de AppRegistro (app)</h3>
 
class UserCreateForm(UserCreationForm):
 
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())

    class Meta:
 
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        model = get_user_model()

 
class EditProfileForm(UserChangeForm):
 
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter you last name...'  , 'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es superusuario...'  , 'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es staff...'  , 'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es activo...'  , 'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Fecha de registro...'  , 'class': 'form-control'}))

    class Meta:
 
        fields = ("username", "first_name", "last_name", "email", "password" )
        model = get_user_model()

 
class PasswordChangingForm(PasswordChangeForm):
 
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        fields = ("old_password", "new_password1", "new_password2")
        model = get_user_model()
<br>

 
<h3>Pasos de instalación:</h3>

Antes que nada recomendamos trabajar en un ambiente controlado como virtualenv o pipenv para evitar conflictos de versiones.
Ejecute el comando: 
<strong>virtualenv venv</strong>

Esto creará una carpeta con el nombre "venv". Ingrese a la ruta venv/Scripts y ejecute el activate.
Tambien puede correr el siguiente comando:
<strong>.\Scripts\activate</strong>

Una vez llevado a cabo, debera ver el nombre de su enterno virtual como promt entre parentesis.

(venv)

Ejecute el siguiente comando 
<strong>pip install -r requirements.txt</strong>


