# AUTOMADB



## Requisitos del Setup

Estos son los requisitos para poder ejecutar el proyecto:

  * Python 2.7
  * Pip package installer
  * Android Debug Bridge (ADB)
  * Android SDK Tools
  * Java Development Kit 8
  * Para poder ejecutar la framework con STF, es necesario tener instalado OpenSTF. (https://github.com/openstf/stf).

### Preparacion

Para instalar todas las dependencias, abrir una consola o terminal en el ***root***
del proyecto, y insertar este comando:

`pip install -r requirements.txt`

### Preparacion OpenSTF

Para correr su instancia en STF, segun la documentacion de OpenSTF, si se tienen todos los prerequisitos correspondientes de su parte, ejecutar:

`stf local`

O si se desea correr sobre la red local:

`stf local --public-ip <ip_address>`

Despues, dirigirse a la consola de STF en http://<ip_address>:7100/ e ingresar con las credenciales de su instalacion STF.

Para obtener una token, dirigirse a Settings y Keys, para generar un access Token para la API.

![Alt text](docs/STF-1.png?raw=true "STFToken")

En la misma pagina, debe seguir las instrucciones para añadir las ADB keys de su maquina a STF, para poder asi controlar a los
dispositivos remotamente.

![Alt text](docs/STF-2.png?raw=true "STFKeys")

Finalmente, integrar STF a la framework, se debe modificar el archivo ***stf_config.json***. Ahi se especifica el Access Token y la URL donde esta corriendo nuestro STF.


### Ultimos detalles

Para comprobar que ADB esta instalado correctamente, conectar el telefono en modo debug,  abrir una terminal donde
 se desee y ejecutar el comando: `adb devices`.

Si el setup fue correcto, se mostrara una lista con los dispositivos moviles
conectados al equipo.

Para poder conectarse a los dispositivos de STF desde su equipo, es necesario desde el Cliente UI de STF en la seccion de 
*ADB Keys* la direccion de su computadora. Sin esto, STF no le dara el acceso a los dispositivos.

### Compatibilidad del dispositivo

Para que el framework funcione con su dispositivo, debe asegurarse que su version este implementada.

Para verificar esto:
 
 1. Ejecutar en una terminal ``adb devices``
 2. Copiar el serial perteneciente a su dispositivo.
 3. Ir a la carpeta src/devices. En el archivo device_compatibility.json, agregar su serial especificando el nombre de
    la version a la que pertenece su telefono. Si no existe ninguna, la framework no es compatible.
 
 El serial tambien debe estar registrado para los dispositivos remotos de STF.
 
 
 Versiones compatibles actualmente: android9, huaweiY9



# Ejecucion de los scripts

Despues de haber cumplido todos los requisitos del setup, abrir una consola o terminal en el ***root*** del proyecto:

### Seleccionar las test suites a ejecutar

Para seleccionar que test suites ejecutar, se debe modificar el archivo **main.py**, para definir las test suites que se desean ejecutar.

```
def run_framework():
    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite()
    # Dialer Suite
    DialerSuite.run_suite()
    # Calculator Suite
    CalculatorSuite.run_suite()

```


### Ejecutar los scripts de la framework

Desde la ***root*** del proyecto ejecutar el comando;

`python main.py -local`

Esto ejecutara todas las suites que se hayan declarado previamente, con los dispositivos que se encuentren localmente conectados
al servidor local de adb.

Para poder ejecutar la framework con los dispositivos remotos de STF, ejecutar:

`python main.py -stf`

Esto correra las suites uno por uno en cada dispositivo remoto.


### Ejecutar test suites particulares manualmente

Si se desea, se pueden ejecutar test suites manualmente. Desde la root, ejecutar:

`cd src/suites`

Una vez en el directorio de las suites, se definen los scripts a correr y se definen los inputs. Por ejemplo, para correr la suite de Calculadora:

`python calculatorapp.py`

En este caso, se deben definir los inputs de la calculadora en el archivo *inputs/calculatorapp.txt*

Este metodo solo funciona corriendo la framework con la bandera de '-local'

### Documentacion

|   File	|   Location	|
|---	|---	|
|  [Business Case](docs/BusinessCase.docx) 	|   docs/BusinessCase	|
|   [Test Plan](qa/Test-Plan-and-Strategy.docx)	|   qa/Test-Plan-and-Strategy	|
|   [Test Strategy]()	|   qa/Test-Plan-and-Strategy	|
|   [Test Cases](qa/Test-Plan-and-Strategy.docx)	|   qa/TestCases-Matrix-v2	|
|   [Traceability Matrix](qa/TestCases-Matrix-v2.xlsx)	|   qa/TestCases-Matrix-v2 |
|   [Execution reports](qa/reports)	|   qa/reports	|
|   [Release Notes](docs/releaseNotesv2.docx)	|   docs/releaseNotesv2	|
|   [Bug Reports](docs/releaseNotesv2.docx)	|   docs/releaseNotesv2	|
|   [Core documentation](docs/core.docx)	|   docs/core	|
