bueno la verdad esto es una verga asi q lo que voy a hacer es anotarme aca los pasos para que esta poronga funcione

0.creamos la red a la que se conectaran nuestros containers con las siguientes variables: "docker network create mired"

1. creamos una carpeta para la base de datos y uno para el backend, cada una con sus respetctivos archivos y Dockerfiles

2. en la carpeta de la db creamos la img para la base de datos con el comando: "docker build -t mypsqldb:v56 ./" 
    y levantamos su respectivo conteiner con: docker run -d --name mypsqlcont --network mired -p 5432:5432 mypsqldb:v56

3. hacemos lo mismo en la la carpeta del backend con el comando: "docker build -t myserverimg:v0 ./"
    y con: "docker run -d --name myservercont --network mired -p 8000:8000  myserverimg:v0"

4. y listo la concha de tu puta madre
checkeamos el server con 

5. nos conectamos al server desde: http://localhost:8000/

6. nos conectamos a la base de datos con: psql -h localhost -U nathan -p 5432 -W mudanza
    vemos las tablas con \dt;
    vemos una tabla en particular con select * from tabla;


COMMITEAR
anoto los pasos xq siempre me los olvido

git status 
git add .
git commit -m "coment"
git push -u origin master