# CienciaDatos
PAPD - Ciencia de datos

## GIT

Git es una herramiento para llevar el control de proyectos.  **Colección** de Directorios y archivos

Incluye:

- Manejo de Versiones
- Facilita la colaboración
- Integra cambios  paralelos al mismo código
- Diferentes personas pueden trabajar en la misma parte del código
- Puedo saber quien, cuando y donde cambiaron alguna parte del código

No utiliza un modelo lineal, es algo mas complejo, pues puede crear ramas del mismo código para que 2 o mas personas lo trabajen
y posteriormente se pueda *integrar* en la versión difinitiva

Como exactamente se representa 

tipos de objetos:
 - blob (array(byte))
 - map <string, tree | blob>
 - commit = estructura
 
 Cada rama es un snapshot de los directorios y archivos, con metadata adicional que ayudan posteriormente a la unificación 
 del código.
 
 Al final lo que guarda son punteros en notación hexadecimal, con una referencia en lenguaje entendible.

![Conceptos principales](img/git.jpg)

### Comandos básicos

Comando | descripción
-- | --
init | Inicia un directorio para que trabaje con git
add | añade un archivo o directorio al repositorio
status | Despliega el status de nuestro repositorio
checkout | elimina los cambios realizados
commit | aplica los cambios realizados
push | Envía los cambios al repositorio general
pull | obtiene los cambios del repositorio general


### Pasos para iniciar un nuevo repositorio

1. git init
2. git add README.md
3. git commit -m "first commit"
4. git branch -M main
5. git remote add origin <URL/repositorio.git>
6. git push -u origin main

### Pasos para agregar un archivo

1. Crear el archivo
    - make filename
2. git add filename
    
### pasos para enviarlo a la nube

1. git commit -m "Se agrega el archivo animal.py"

    ![Conceptos principales](img/Img1.png)
    
2. git push 

    ![Conceptos principales](img/Img2.png)

### pasos para crear un branch

1. git checkout -b gato
2. git checkout -b perro

  ![Conceptos principales](img/img3.png)

3. Cambiar al branch que se necesita trabajar (gato)

   git checkout gato
   --> hacer cambios a gato
   git checkout perro
   --> hacer cambios a perro
   
## pasos para hacer merge de ambos cambios a master

1. git checkout main 
2. git merge gato 

  ![Conceptos principales](img/Img4.png)

   
   


