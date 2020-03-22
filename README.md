# CORE UTILS CERT

## Descripción

Ester proyecto expone una serie de utilidades para la gestión de certificados

Para ejecutar cualquier modulo, es necesario activar el entorno virtual ...

```sh
source /Users/borja.sanchez/Code/python/virtualenv/vmigration/bin/activate;
```

## Generación de jks

Para generar un nuevo keystore, ejecutaremos el siguiente comando

```sh
binaries_migration_utils generate_jks -pfx /Users/borja.sanchez/Code/certs/seiri-play/etherId.p12 -pwd Mc6xVLLf -a seiri-client -ca /Users/borja.sanchez/Code/certs/CA/work/globalrootca.crt /Users/borja.sanchez/Code/certs/CA/work/globalissuingcainfrastructure.crt
```

Para ver todas las opciones disponobles de la generación de un keystore, ejecutamos el comando

```sh
python3 binaries_migration_utils.py generate_jks -h
```

# Estra

## Instalación del modulo de utilidades

Una vez descargado el modulo de utilidades, es necesario generar un entorno virtual

```sh
# Ruta que contiene los entornos virtuales
cd /Users/borja.sanchez/Code/python/virtualenv

export VENV=vmigration # Nombre del entorno virtual

# Instalar virtual env en macOS con Homebrew
pip install virtualenv

# Creación de un nuevo entorno virtual
virtualenv $VENV --python=python3

# Activación del entorno virtual
source ./$VENV/bin/activate;

# Descarga de las dependencias desde el path del proyecto
pip install -r requirements.txt
```

# Referencias

Transformación pfx (p12) a [pem](https://gist.github.com/erikbern/756b1d8df2d1487497d29b90e81f8068)
Instalación mediante [pip](http://blog.vero4ka.info/blog/2018/07/25/como-hacer-un-repositorio-de-python-instalable/)
