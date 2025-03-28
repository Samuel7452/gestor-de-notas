# gestor-de-notas
esta es una aplicacion construida sobre el framework de django para la gestion de notas personales, con edicion de contenidos, categorias ETC.

# uso con Docker
dependiendo del sistema operativo que se desee usar se debe instalar docker desktop (Windows) o docker-compose por medio de consola (Linux) 

tener en cuenta que si se desea ejecutar por medio de python sin Docker habra que cambiar el punto env y se deberia ver asi:
//////////////////////////////
NAME=notes
USER=admin
PASSWORD=e4ZXe621HZEthj9f
HOST=localhost
PORT=5432
//////////////////////////////
pero al momento de querer ejecutarse con Docker es muy importante que el HOST este como en el siguiente ejemplo
//////////////////////////////
NAME=notes
USER=admin
PASSWORD=e4ZXe621HZEthj9f
HOST=notes_postgres_db
PORT=5432
//////////////////////////////

- situarse en la carpeta origen del proyecto en donde se encuentra el archivo manage.py y ejecutar en la consola el siguiente comando
docker-compose up -d --build

despues se creara el contenedor y la base de datos en Postgresql para el almacenamiento de la informacion de la aplicacion y podra abrir la aplicacion web en la ruta:
http://localhost:8000/api/v1/notes/list/

