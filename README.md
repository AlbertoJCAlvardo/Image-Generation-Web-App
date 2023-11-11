# Aplicacion Para Generación de Imagenes
Un ejemplo de como realizar una aplicación web
sencilla utilizando python flask y openai api

## Creación de un entorno virtual
Para el correcto uso y segmentación de las librerías 
es preciso crear un entorno virtual para el proyecto
### Windows
```
  py -m pip install --user virtualenv
  py -m venv env
  env\Scripts\activate.bat
```

### Linux / macOS
```
   pip install virtualenv
   python3 -m venv env
   source env/bin/activate
```


## Instalación

Utiliza el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) 
para instalar las librerias utilizadas
```
    pip install -r requirements.txt
```

##Definicion de variables de entorno

### Linux/macOS:
```
export FLASK_APP="image.py"
```
### Windows: 
```
set "FLASK_APP=image.py"
```

## Uso
Para encender la aplicación:
```
  flask run
```

## Para utilizar la aplicacion solo es necesario escrbir en el navegador
### Windows
```
  127.0.0.1:5000
```

### Linux
```
  127.0.0.0:5000
```
