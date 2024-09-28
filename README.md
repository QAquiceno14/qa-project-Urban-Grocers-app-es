Adriana Quiceno, grupo 14 Avo, Sprint 

Proyecto Urban Grocers
Este proyecto consiste en realizar pruebas para la creación de un kit de usuario en la aplicación Urban Grocers mediante el uso de su API. El objetivo principal es asegurar que la funcionalidad de creación de kits cumple con las restricciones y requerimientos de validación.

Para ello, sigue estos pasos:

1) Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
2) Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.
3) Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

lista de comprobación 

def test_create_kit_body_1_letter_in_first_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_create_kit_body_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_create_kit_body_0_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_3)

def test_create_kit_body_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.kit_body_4)

def test_create_kit_body_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_5)

def test_create_kit_body_has_space_in_name_get_successful_response():
    positive_assert(data.kit_body_6)

def test_create_kit_body_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_7)

def test_create_kit_body_no_name_get_error_response():
    negative_assert_symbol(data.Kit_body_8)

def test_create_kit_body_number_type_name_get_error_response():
    negative_assert_symbol(data.Kit_body_9)

Archivos del proyecto 
configuration.py, data.py sender_stand_request.py, create_kit_name_kit_test.py, README.md, y .gitignore.

Paquetes usados en el Proyecto: 
Request, Pytest

Lista de instrucciones 
1.	enlazar tu cuenta de GitHub a TripleTen
2.	Clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de esta página.
3.	Confirmes que deseas enlazar tu cuenta de GitHub
4.	Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña
5.	Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub.
6.	Clona el repositorio en tu computadora
7.	Para ellos debes haber vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Grocers-app-es.
Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

1.1	Abre la línea de comandos en tu computadora.

1.2	Si aún no lo has hecho, crea un directorio para almacenar         todos tus proyectos. Por ejemplo:
•	cd ~               # asegúrate de estar en tu directorio de inicio

•	mkdir projects     # crea una carpeta llamada projects

•	cd projects        # cambia el directorio a la nueva carpeta de proyectos


1.3	 Y por último Clona el repositorio con SSH, para después trabajar en el proyecto de forma local

1.4	Cuando puedas comenzar a trabajar, presiona el botón "Iniciar el servidor" para obtener la URL de tu servidor.

