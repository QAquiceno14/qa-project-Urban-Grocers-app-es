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

Instalando Pytest

Existen dos métodos para instalar Pytest. Elige el que te resulte más conveniente.
Usando el comando "pip" en la terminal:
1.	Abre la terminal o consola.
2.	Ingresa el comando pip install pytest.

pip es el gestor de paquetes de Python. Te permite instalar y gestionar bibliotecas, así como herramientas adicionales.
 A través de la interfaz de PyCharm en "Python Packages":
1.	En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
2.	En el campo de búsqueda, introduce "Pytest".
3.	Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".Siguiente

Ejecución de pruebas

Tienes dos opciones para ejecutar tus pruebas: directamente desde la consola de PyCharm o utilizando su interfaz gráfica.
Desde la terminal de PyCharm
Dirígete a la pestaña "Terminal" en la parte inferior de PyCharm. Por defecto, esta terminal se ubica en el directorio de tu proyecto. 
Para ejecutar todas las pruebas de tu proyecto, simplemente escribe:
pytest
Luego ejecuta las pruebas desde el archivo calc_test.py:
pytest calc_test.py

Ejecuta todas las pruebas del proyecto:
1.	En el menú "Run", selecciona "Edit Configurations" (Editar configuraciones).
2.	Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración). Se abrirá una ventana nueva.
3.	Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
4.	Aparecerá una ventana nueva. Selecciona "Custom" (Personalizar) en la línea "Target" (Objetivo).
5.	Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
6.	Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados.

Ejecución de pruebas en un archivo determinado:

1.	En el menú "Run", selecciona "Edit Configurations" (Editar configuraciones).
2.	Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración) en una ventana nueva.
3.	Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
4.	Aparecerá una ventana nueva. El "Script path" está seleccionado en la línea "Target" de forma predeterminada. No cambies nada aquí.
5.	Selecciona el archivo con tus pruebas en el campo debajo de "Target". Puedes hacerlo haciendo clic en el ícono con forma de carpeta.
6.	Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
7.	Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados:

Después de instalar Pytest, verás una flecha verde junto a las pruebas que se utiliza para ejecutarlas (puedes verla en la línea 1 de tu archivo). Haz clic en ella y observa el resultado.

Instalación de Librerías en Python

Para trabajar con solicitudes HTTP en Python, necesitarás el paquet requests. Recuerda que cuentas con dos formas de instalarlo:
Usando "pip", el gestor de paquetes de Python
1.	Abre la terminal o consola.
2.	Ingresa el comando pip install requests.
Recuerda: pip significa administrador de paquetes. En otras palabras, este es un programa para instalar varios paquetes, ya está integrado en Python.
 Mediante la pestaña "Python Packages" (Paquetes de Python)
1.	En PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages” (Paquetes de Python).
2.	En la barra de búsqueda, escribe "requests" (solicitudes).
3.	Localiza y selecciona el paquete "requests" de la lista.
4.	Finalmente, haz clic en el botón "Install" (instalar).

De esta forma se descargará e instalará la última versión de la librería mencionada, Una vez que la librería ha sido instalada, puedes usarla en tu código importándola.

Vamos a explorar cómo hacer una solicitud a la página de documentación de la API de Urban Grocers utilizando la librería requests de Python.

1.	Archivo de configuración: Crea un archivo llamado configuration.py en tu proyecto. Aquí almacenarás la URL base de Urban Grocers y la ruta específica para la documentación:
URL_SERVICE = "copia la URL generada sin la barra inclinada al final"
DOC_PATH = "/docs/"
•	URL_SERVICE: Esta es una constante que almacena la URL base del servicio de Urban Grocers. La frase "copia la URL generada sin la barra inclinada al final" es un marcador de posición: reemplázala con la URL real del servidor que iniciaste.
•	DOC_PATH: Esta constante almacena la ruta específica para acceder a la documentación en la URL base.
2.	El archivo de solicitud. Crea otro archivo y nómbralo sender_stand_request.py. Importa a este el archivo configuration y el paquete requests utilizando la palabra clave import. Esta se indica arriba. Aquí está tu código:
	import configuration
	import requests
3.	Envío de a la solicitud. Puedes enviar una solicitud mediante la librería requests de Python. Solo necesitas llamar a la función get() y proporcionarle la URL completa a la que deseas acceder. También puedes incluir encabezados y parámetros si es necesario.
4.	A continuación, agrega el siguiente código a tu archivo sender_stand_request.py para realizar la solicitud y mostrar el código de estado de la respuesta:

•	import configuration
•	import requests



def get_docs():
return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)

Veamos los detalles de cada línea de código:

•	import configuration: esta línea importa el archivo configuration.py. Esto significa que ahora puedes acceder a las constantes definidas en configuration.py: URL_SERVICE y DOC_PATH.

•	import requests: importa la librería Requests.

•	def get_docs(): define una función llamada get_docs. Cuando se llama a esta función, realiza una solicitud GET a la combinación de URL_SERVICE y DOC_PATH (es decir, la URL completa de la documentación).

•	response = get_docs(): esta línea llama a la función get_docs() y almacena la respuesta en la variable de respuesta.

•	print(response.status_code): muestra el código de estado de la respuesta HTTP. Por ejemplo, si todo va bien, debe mostrarse 200, que es el código de estado de "OK".


La librería de solicitudes de Python: solicitudes POST

1.	Configuración de la ruta: añade el siguiente código al archivo configuration.py. Esta ruta es la que crea un usuario
CREATE_USER_PATH = "/api/v1/users/"
2.	Datos de la solicitud: crea un archivo llamado data.py. Este archivo almacenará la información que se enviará en la solicitud, como el cuerpo y los encabezados:

headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
3.	Importación de datos: en el archivo sender_stand_request.py, asegúrate de importar el archivo data para acceder a la información que acabas de crear:

import configuration

import requests

import data
4.	Envío de la solicitud POST: para enviar la solicitud, utiliza la función post() de la librería Requests de Python. Esta función necesita la URL completa, el cuerpo de la solicitud y los encabezados:

def post_new_user(body):

return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
   
json=body,  # inserta el cuerpo de solicitud

headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)

print(response.status_code)

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

