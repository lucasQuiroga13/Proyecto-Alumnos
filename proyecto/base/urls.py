from django.urls import path
from .views import ListaAlumnos, DetalleAlumno, CrearAlumno, EditarAlumno, EliminarAlumno, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("", ListaAlumnos.as_view(), name="alumnos"),
               path('login/', Logueo.as_view(), name="login"),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
               path("alumno/<int:pk>", DetalleAlumno.as_view(), name="alumno"),
               path("crear-alumno/", CrearAlumno.as_view(), name="crear-alumno"),
               path("editar-alumno/<int:pk>", EditarAlumno.as_view(), name="editar-alumno"),
               path("eliminar-alumno/<int:pk>", EliminarAlumno.as_view(), name="eliminar-alumno")]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
