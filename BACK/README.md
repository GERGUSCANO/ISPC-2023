--PIP y Python3 
    https://docs.python.org/es/3.9/library/ensurepip.html#:~:text=De%20forma%20predeterminada%2C%20pip%20se,hay%20ning%C3%BAn%20entorno%20virtual%20activo

-- MYSQL y MYSQL worbrench
    https://dev.mysql.com/downloads/workbench/


--Instructivo de instalación MySQL y Workbench
    https://docs.google.com/presentation/d/1iAmBc6G8qI0bBvi3wcjOxLRK6a4al1Nt/edit?usp=sharing&ouid=106638896470969516678&rtpof=true&sd=true


--Crear un entorno virtual dentro de su proyecto de back para tener instalados lo necesario del proyecto y que no se instale en el entorno global de python.Como primer paso instalamos VirtualEnv con el siguiente comando:
        pip install virtualenv
    --Creamos el entorno
        WIN :   venv mientornovirtual
        linux: python3 -m venv mientornovirtual
    --Luego, activamos el entorno virtual
        Windows:
            source mientornovirtual/Scripts/activate
        Linux: 
            source mientornovirtual/bin/activate
--Django
    pip3 install djangorestframework

--Luego instalaremos el paquete CORS, este paquete nos servirá para poder
comunicarnos con Angular cuando lleguemos a ese punto.
    pip install django-cors-headers



