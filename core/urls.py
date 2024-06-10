from django.contrib import admin
from django.urls import path
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login_Professor, name='Login_Professor'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('Cadastro/', views.Cadastro, name='Cadastro'),
    path('CadastrarTurma/<int:id>/', views.Cadastro_Turma, name='Cadastro_Turma'),
    path('CadastrarAtividade/<int:id_professor>/<int:id_turma>/', views.Cadastro_Atividades, name='Cadastrar_Atividade'),
    path('area_professor/<int:id>/', views.area_professor, name='area_professor'),
    path('area_turma/<int:id>', views.area_turma, name='area_turma'),
    path('delete/<int:id_turma>/', views.Excluir_Turma, name='Excluir_Turma' ),
    path('confirm/<int:id_turma>/', views.confirm, name='Confirm')
]