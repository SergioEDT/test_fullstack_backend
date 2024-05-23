Repositorio para el proyecto Backend

Requisitos previos
- Python 3.9 o superior instalado en tu sistema.

Instalación
1. Clona este repositorio en tu máquina local:
    git clone <URL_del_repositorio>

2. Ve al directorio del proyecto:
    cd nombre_del_proyecto

3. Crea un entorno virtual (opcional, pero se recomienda):
    python -m venv venv

4. Activa el entorno virtual:
    En Windows:
        venv\Scripts\activate
    En macOS y Linux:
        source venv/bin/activate

5. Instala las dependencias del proyecto:
    pip install -r requirements.txt

Configuración
1. Crea un archivo .env en el directorio raíz del proyecto y agrega las siguientes variables de entorno:
    DATABASE_URL=url_proporcionada_por_coreo
Reemplaza url_proporcionada_por_coreo con la URL que se le hizo llegar por correo.

Ejecución
1. Con el entorno virtual activado y las dependencias instaladas, ejecuta el siguiente comando para iniciar el servidor de desarrollo:
    uvicorn main:app --reload

2. La consola indicará el url donde estará disponible el API.

Detener la ejecución
1. Para detener la ejecución del servidor, simplemente presiona Ctrl + C en la terminal donde se está ejecutando.
