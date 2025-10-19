#!/usr/bin/env python
########################################################################
#
# text menu for set menu stuff
#
########################################################################
from src.core.setcore import bcolors, get_version, check_os, meta_path

# grab version of SET
define_version = get_version()

# check operating system
operating_system = check_os()

# grab metasploit path
msf_path = meta_path()

PORT_NOT_ZERO = "¡El puerto no puede ser cero!"
PORT_TOO_HIGH = "Mantengámonos con los puertos INFERIORES a 65,535..."

main_text = " Seleccione del menú:\n"

main_menu = ['Ataques de Ingeniería Social',
             'Pruebas de Penetración (Fast-Track)',
             'Módulos de Terceros',
             'Actualizar ingenieriasocial',
             'Actualizar configuración de ingenieriasocial',
             'Ayuda, Créditos y Acerca de']

main = ['Vectores de Ataque Spear-Phishing',
        'Vectores de Ataque Web',
        'Generador de Medios Infecciosos',
        'Crear un Payload y Listener',
        'Ataque de Correo Masivo',
        'Vector de Ataque Basado en Arduino',
        'Vector de Ataque de Punto de Acceso Inalámbrico',
        'Vector de Ataque Generador de Código QR',
        'Vectores de Ataque Powershell',
        'Módulos de Terceros']

spearphish_menu = ['Realizar un Ataque de Correo Masivo',
                   'Crear un Payload de Formato de Archivo',
                   'Crear una Plantilla de Ingeniería Social',
                   '0D']

spearphish_text = ("""
 El módulo de """ + bcolors.BOLD + """Spearphishing""" + bcolors.ENDC + """ le permite crear mensajes de correo especialmente diseñados y enviarlos
 a un gran (o pequeño) número de personas con payloads maliciosos adjuntos en formato de archivo.
 Si desea falsificar su dirección de correo, asegúrese de que "Sendmail" esté instalado
 (apt-get install sendmail) y cambie la bandera config/set_config SENDMAIL=OFF a SENDMAIL=ON.

 Hay dos opciones, una es empezar y dejar que SET haga todo por usted (opción 1),
 la segunda es crear su propio payload de formato de archivo y usarlo en su propio ataque.
 ¡De cualquier manera, buena suerte y disfrute!
""")

webattack_menu = ['Método de Ataque Java Applet',
                  'Método de Exploit de Navegador Metasploit',
                  'Método de Ataque Recolector de Credenciales',
                  'Método de Ataque Tabnabbing',
                  'Método de Ataque Web Jacking',
                  'Método de Multi-Ataque Web',
                  'Método de Ataque HTA',
                  '0D']

fasttrack_menu = ['Fuerza Bruta Microsoft SQL',
                  'Exploits Personalizados',
                  'Vector de Ataque SCCM',
                  'Verificador Predeterminado Dell DRAC/Chassis',
                  'RID_ENUM - Ataque de Enumeración de Usuarios',
                  'Inyección PSEXEC Powershell',
                  '0D']

fasttrack_text = ("""
Bienvenido a ingenieriasocial - """ + bcolors.BOLD + """Plataforma de Pruebas de Penetración Fast-Track""" + bcolors.ENDC + """. Estos vectores de ataque
tienen una serie de exploits y aspectos de automatización para asistir en el arte de las pruebas de penetración. SET
ahora incorpora los vectores de ataque aprovechados en Fast-Track. Todos estos vectores de ataque han sido
completamente reescritos y personalizados desde cero para mejorar la funcionalidad y capacidades.
""")

fasttrack_exploits_menu1 = ['MS08-067 (Win2000, Win2k3, WinXP)',
                            'Mozilla Firefox 3.6.16 Exploit Use After Free del Objeto mChannel (Win7)',
                            'Solarwinds Storage Manager 5.1.0 Exploit de Inyección SQL SYSTEM Remoto',
                            'RDP | Use after Free - Denegación de Servicio',
                            'Exploit de Bypass de Autenticación MySQL',
                            'Exploit de Bypass de Autenticación Root F5',
                            '0D']

fasttrack_exploits_text1 = ("""
Bienvenido a ingenieriasocial - Pruebas de Penetración Fast-Track """ + bcolors.BOLD + """Sección de Exploits""" + bcolors.ENDC + """. Este
menú tiene exploits oscuros y aquellos que son principalmente impulsados por python. Esto continuará creciendo con el tiempo.
""")

fasttrack_mssql_menu1 = ['Escanear y Atacar MSSQL',
                         'Conectar directamente a MSSQL',
                         '0D']

fasttrack_mssql_text1 = ("""
Bienvenido a ingenieriasocial - Pruebas de Penetración Fast-Track """ + bcolors.BOLD + """Fuerza Bruta Microsoft SQL""" + bcolors.ENDC + """. Este
vector de ataque intentará identificar servidores MSSQL activos y forzar por fuerza bruta las contraseñas débiles de cuentas que
puedan encontrarse. Si eso ocurre, SET comprometerá el sistema afectado desplegando un vector de ataque binario a
hexadecimal que tomará un binario crudo, lo convertirá a hexadecimal y usará un enfoque por etapas
en el despliegue de la forma hexadecimal del binario en el sistema subyacente. En este punto, ocurrirá un disparador
para convertir el payload de vuelta a un binario para nosotros.
""")

webattack_text = ("""
El módulo de Ataque Web es una forma única de utilizar múltiples ataques basados en web para comprometer a la víctima objetivo.

El método de """ + bcolors.BOLD + """Ataque Java Applet""" + bcolors.ENDC + """ falsificará un Certificado Java y entregará un payload basado en Metasploit. Usa un applet java personalizado creado por Thomas Werth para entregar el payload.

El método de """ + bcolors.BOLD + """Exploit de Navegador Metasploit""" + bcolors.ENDC + """ utilizará exploits selectos de navegador Metasploit a través de un iframe y entregará un payload Metasploit.

El método de """ + bcolors.BOLD + """Recolector de Credenciales""" + bcolors.ENDC + """ utilizará clonación web de un sitio web que tenga un campo de nombre de usuario y contraseña y recolectará toda la información publicada en el sitio web.

El método de """ + bcolors.BOLD + """TabNabbing""" + bcolors.ENDC + """ esperará a que un usuario se mueva a una pestaña diferente, luego actualizará la página a algo diferente.

El método de """ + bcolors.BOLD + """Ataque Web-Jacking""" + bcolors.ENDC + """ fue introducido por white_sheep, emgent. Este método utiliza reemplazos de iframe para hacer que el enlace URL resaltado parezca legítimo, sin embargo, cuando se hace clic, aparece una ventana que luego es reemplazada con el enlace malicioso. Puede editar la configuración de reemplazo de enlaces en set_config si es demasiado lento/rápido.

El método de """ + bcolors.BOLD + """Multi-Ataque""" + bcolors.ENDC + """ agregará una combinación de ataques a través del menú de ataque web. Por ejemplo, puede utilizar el Java Applet, Navegador Metasploit, Recolector de Credenciales/Tabnabbing todo a la vez para ver cuál tiene éxito.

El método de """ + bcolors.BOLD + """Ataque HTA""" + bcolors.ENDC + """ le permitirá clonar un sitio y realizar inyección PowerShell a través de archivos HTA que pueden usarse para explotación PowerShell basada en Windows a través del navegador.
""")

webattack_vectors_menu = ['Plantillas Web',
                          'Clonador de Sitios',
                          'Importación Personalizada\n',
                          ]

webattack_vectors_text = ("""
 El primer método permitirá a SET importar una lista de aplicaciones web
 predefinidas que puede utilizar dentro del ataque.

 El segundo método clonará completamente un sitio web de su elección
 y le permitirá utilizar los vectores de ataque dentro de la misma
 aplicación web que estaba intentando clonar.

 El tercer método le permite importar su propio sitio web, tenga en cuenta que
 solo debe tener un index.html al usar la funcionalidad de importar sitio web.
   """)

teensy_menu = ['Payload PowerShell HTTP GET MSF',
               'Payload WSCRIPT HTTP GET MSF',
               'Payload Reverse Shell basado en PowerShell',
               'Payload Internet Explorer/FireFox Beef Jack',
               'Ir a sitio java malicioso y aceptar payload applet',
               'Payload Descarga Gnome wget',
               'Ataque Binary 2 Teensy (Desplegar payloads MSF)',
               'Ataque SDCard 2 Teensy (Desplegar Cualquier EXE)',
               'Ataque SDCard 2 Teensy (Desplegar en OSX)',
               'X10 Arduino Sniffer PDE y Bibliotecas',
               'X10 Arduino Jammer PDE y Bibliotecas',
               'Ataque Teensy ShellCode Directo PowerShell',
               'Ataque Multi Peensy Dip Switch + Ataque SDCard',
	       'Ataque Shellcode HID Msbuild compilar en memoria',
               '0D']

teensy_text = ("""
 El Vector de """ + bcolors.BOLD + """Ataque Basado en Arduino""" + bcolors.ENDC + """ utiliza el dispositivo basado en Arduino para
 programar el dispositivo. Puede aprovechar los Teensy, que tienen almacenamiento
 integrado y pueden permitir la ejecución remota de código en el sistema
 físico. Dado que los dispositivos están registrados como Teclados USB,
 evitarán cualquier autorun deshabilitado o protección de endpoint en el
 sistema.

 Necesitará comprar el dispositivo USB Teensy, cuesta aproximadamente
 $22 dólares. Este vector de ataque generará automáticamente el código
 necesario para desplegar el payload en el sistema por usted.

 Este vector de ataque creará los archivos .pde necesarios para importar
 en Arduino (el IDE usado para programar el Teensy). Los vectores de ataque
 van desde descargadores basados en PowerShell, ataques wscript,
 y otros métodos.

 Para más información sobre especificaciones y buenos tutoriales visite:

 http://www.irongeek.com/i.php?page=security/programmable-hid-usb-keystroke-dongle

 Para comprar un Teensy, visite: http://www.pjrc.com/store/teensy.html
 Agradecimientos especiales a: IronGeek, WinFang, y Garland

 Este vector de ataque también ataca controladores basados en X10, asegúrese de estar aprovechando
 dispositivos de comunicación basados en X10 para que esto funcione.

 Seleccione un payload para crear el archivo pde para importar en Arduino:
""")

wireless_attack_menu = ['Iniciar el Punto de Acceso del Vector de Ataque Inalámbrico SET',
                        'Detener el Punto de Acceso del Vector de Ataque Inalámbrico SET',
                        '0D']


wireless_attack_text = """
 El módulo de """ + bcolors.BOLD + """Ataque Inalámbrico""" + bcolors.ENDC + """ creará un punto de acceso aprovechando su
 tarjeta inalámbrica y redirigirá todas las consultas DNS hacia usted. El concepto es bastante
 simple, SET creará un punto de acceso inalámbrico, servidor DHCP, y falsificará
 DNS para redirigir el tráfico a la máquina del atacante. Luego saldrá
 de ese menú con todo ejecutándose como un proceso hijo.

 Luego puede lanzar cualquier vector de ataque SET que desee, por ejemplo el ataque
 Java Applet y cuando una víctima se una a su punto de acceso e intente ir a
 un sitio web, será redirigida a su máquina atacante.

 Este vector de ataque requiere AirBase-NG, AirMon-NG, DNSSpoof, y dhcpd3.

"""

infectious_menu = ['Exploits de Formato de Archivo',
                   'Ejecutable Estándar Metasploit',
                   '0D']


infectious_text = """
 El módulo """ + bcolors.BOLD + bcolors.GREEN + """Infeccioso """ + bcolors.ENDC + """USB/CD/DVD creará un archivo autorun.inf y un
 payload Metasploit. Cuando se inserte el DVD/USB/CD, se ejecutará automáticamente
 si autorun está habilitado.""" + bcolors.ENDC + """

 Elija el vector de ataque que desea usar: bugs de formato de archivo o un ejecutable directo.
"""

# used in create_payloads.py
if operating_system != "windows":
    if msf_path != False:
        payload_menu_1 = [
            'Inyección de Memoria Meterpreter (PREDETERMINADO)  Esto soltará un payload Meterpreter a través de inyección powershell',
            'Inyección Multi-Memoria Meterpreter      Esto soltará múltiples payloads Metasploit vía inyección powershell',
            'Shell Interactivo SE Toolkit            Shell inverso interactivo personalizado diseñado para SET',
            'Shell Inverso HTTP SE Toolkit           Shell HTTP puramente nativo con soporte de cifrado AES',
            'Payload Túnel HTTP RATTE                Payload de bypass de seguridad que tunelizará todas las comunicaciones sobre HTTP',
            'ShellCode Alfanumérico ShellCodeExec    Esto soltará un payload meterpreter a través de shellcodeexec',
            'Importar su propio ejecutable           Especifique una ruta para su propio ejecutable',
            'Importar su propio commands.txt         Especifique payloads a enviar vía línea de comandos\n']

if operating_system == "windows" or msf_path == False:
    payload_menu_1 = [
        'Shell Interactivo SE Toolkit    Shell inverso interactivo personalizado diseñado para SET',
        'Shell Inverso HTTP SE Toolkit   Shell HTTP puramente nativo con soporte de cifrado AES',
        'Payload Túnel HTTP RATTE        Payload de bypass de seguridad que tunelizará todas las comunicaciones sobre HTTP\n']

payload_menu_1_text = """
¿Qué payload le gustaría generar:

  Nombre:                                     Descripción:
"""

# used in gen_payload.py
payload_menu_2 = [
    'Windows Shell Reverse_TCP               Generar un shell de comandos en la víctima y enviar de vuelta al atacante',
    'Windows Reverse_TCP Meterpreter         Generar un shell meterpreter en la víctima y enviar de vuelta al atacante',
    'Windows Reverse_TCP VNC DLL             Generar un servidor VNC en la víctima y enviar de vuelta al atacante',
    'Windows Shell Reverse_TCP X64           Shell de Comandos Windows X64, Reverse TCP Inline',
    'Windows Meterpreter Reverse_TCP X64     Conectar de vuelta al atacante (Windows x64), Meterpreter',
    'Windows Meterpreter Egress Buster       Generar un shell Meterpreter y encontrar un puerto de salida vía múltiples puertos',
    'Windows Meterpreter Reverse HTTPS       Tunelizar comunicación sobre HTTP usando SSL y usar Meterpreter',
    'Windows Meterpreter Reverse DNS         Usar un nombre de host en lugar de una dirección IP y usar Reverse Meterpreter',
    'Descargar/Ejecutar su Propio Ejecutable Descarga un ejecutable y lo ejecuta\n'
]


payload_menu_2_text = """\n"""

payload_menu_3_text = ""
payload_menu_3 = [
    'Windows Reverse TCP Shell              Generar un shell de comandos en la víctima y enviar de vuelta al atacante',
    'Windows Meterpreter Reverse_TCP        Generar un shell Meterpreter en la víctima y enviar de vuelta al atacante',
    'Windows Reverse VNC DLL                Generar un servidor VNC en la víctima y enviar de vuelta al atacante',
    'Windows Reverse TCP Shell (x64)        Shell de Comandos Windows X64, Reverse TCP Inline',
    'Windows Meterpreter Reverse_TCP (X64)  Conecta de vuelta al atacante (Windows x64), Meterpreter',
    'Windows Shell Bind_TCP (X64)           Ejecutar payload y crear un puerto de aceptación en el sistema remoto',
    'Windows Meterpreter Reverse HTTPS      Tunelizar comunicación sobre HTTP usando SSL y usar Meterpreter\n']

# called from create_payload.py associated dictionary = ms_attacks
create_payloads_menu = [
    'SET Custom Written DLL Hijacking Attack Vector (RAR, ZIP)',
    'SET Custom Written Document UNC LM SMB Capture Attack',
    'MS15-100 Microsoft Windows Media Center MCL Vulnerability',
    'MS14-017 Microsoft Word RTF Object Confusion (2014-04-01)',
    'Microsoft Windows CreateSizedDIBSECTION Stack Buffer Overflow',
    'Microsoft Word RTF pFragments Stack Buffer Overflow (MS10-087)',
    'Adobe Flash Player "Button" Remote Code Execution',
    'Adobe CoolType SING Table "uniqueName" Overflow',
    'Adobe Flash Player "newfunction" Invalid Pointer Use',
    'Adobe Collab.collectEmailInfo Buffer Overflow',
    'Adobe Collab.getIcon Buffer Overflow',
    'Adobe JBIG2Decode Memory Corruption Exploit',
    'Adobe PDF Embedded EXE Social Engineering',
    'Adobe util.printf() Buffer Overflow',
    'Custom EXE to VBA (sent via RAR) (RAR required)',
    'Adobe U3D CLODProgressiveMeshDeclaration Array Overrun',
    'Adobe PDF Embedded EXE Social Engineering (NOJS)',
    'Foxit PDF Reader v4.1.1 Title Stack Buffer Overflow',
    'Apple QuickTime PICT PnSize Buffer Overflow',
    'Nuance PDF Reader v6.0 Launch Stack Buffer Overflow',
    'Adobe Reader u3D Memory Corruption Vulnerability',
    'MSCOMCTL ActiveX Buffer Overflow (ms12-027)\n']

create_payloads_text = """
 Seleccione el exploit de formato de archivo que desea.
 El predeterminado es el PDF con EXE embebido.\n
           ********** PAYLOADS **********\n"""

browser_exploits_menu = [
    'Adobe Flash Player ByteArray Use After Free (2015-07-06)',
    'Adobe Flash Player Nellymoser Audio Decoding Buffer Overflow (2015-06-23)',
    'Adobe Flash Player Drawing Fill Shader Memory Corruption (2015-05-12)',
    'MS14-012 Microsoft Internet Explorer TextRange Use-After-Free (2014-03-11)',
    'MS14-012 Microsoft Internet Explorer CMarkup Use-After-Free (2014-02-13)',
    'Internet Explorer CDisplayPointer Use-After-Free (10/13/2013)',
    'Micorosft Internet Explorer SetMouseCapture Use-After-Free (09/17/2013)',
    'Java Applet JMX Remote Code Execution (UPDATED 2013-01-19)',
    'Java Applet JMX Remote Code Execution (2013-01-10)',
    'MS13-009 Microsoft Internet Explorer SLayoutRun Use-AFter-Free (2013-02-13)',
    'Microsoft Internet Explorer CDwnBindInfo Object Use-After-Free (2012-12-27)',
    'Java 7 Applet Remote Code Execution (2012-08-26)',
    'Microsoft Internet Explorer execCommand Use-After-Free Vulnerability (2012-09-14)',
    'Java AtomicReferenceArray Type Violation Vulnerability (2012-02-14)',
    'Java Applet Field Bytecode Verifier Cache Remote Code Execution (2012-06-06)',
    'MS12-037 Internet Explorer Same ID Property Deleted Object Handling Memory Corruption (2012-06-12)',
    'Microsoft XML Core Services MSXML Uninitialized Memory Corruption (2012-06-12)',
    'Adobe Flash Player Object Type Confusion  (2012-05-04)',
    'Adobe Flash Player MP4 "cprt" Overflow (2012-02-15)',
    'MS12-004 midiOutPlayNextPolyEvent Heap Overflow (2012-01-10)',
    'Java Applet Rhino Script Engine Remote Code Execution (2011-10-18)',
    'MS11-050 IE mshtml!CObjectElement Use After Free  (2011-06-16)',
    'Adobe Flash Player 10.2.153.1 SWF Memory Corruption Vulnerability (2011-04-11)',
    'Cisco AnyConnect VPN Client ActiveX URL Property Download and Execute (2011-06-01)',
    'Internet Explorer CSS Import Use After Free (2010-11-29)',
    'Microsoft WMI Administration Tools ActiveX Buffer Overflow (2010-12-21)',
    'Internet Explorer CSS Tags Memory Corruption (2010-11-03)',
    'Sun Java Applet2ClassLoader Remote Code Execution (2011-02-15)',
    'Sun Java Runtime New Plugin docbase Buffer Overflow (2010-10-12)',
    'Microsoft Windows WebDAV Application DLL Hijacker (2010-08-18)',
    'Adobe Flash Player AVM Bytecode Verification Vulnerability (2011-03-15)',
    'Adobe Shockwave rcsL Memory Corruption Exploit (2010-10-21)',
    'Adobe CoolType SING Table "uniqueName" Stack Buffer Overflow (2010-09-07)',
    'Apple QuickTime 7.6.7 Marshaled_pUnk Code Execution (2010-08-30)',
    'Microsoft Help Center XSS and Command Execution (2010-06-09)',
    'Microsoft Internet Explorer iepeers.dll Use After Free (2010-03-09)',
    'Microsoft Internet Explorer "Aurora" Memory Corruption (2010-01-14)',
    'Microsoft Internet Explorer Tabular Data Control Exploit (2010-03-0)',
    'Microsoft Internet Explorer 7 Uninitialized Memory Corruption (2009-02-10)',
    'Microsoft Internet Explorer Style getElementsbyTagName Corruption (2009-11-20)',
    'Microsoft Internet Explorer isComponentInstalled Overflow (2006-02-24)',
    'Microsoft Internet Explorer Data Binding Corruption (2008-12-07)',
    'Microsoft Internet Explorer Unsafe Scripting Misconfiguration (2010-09-20)',
    'FireFox 3.5 escape Return Value Memory Corruption (2009-07-13)',
    'FireFox 3.6.16 mChannel use after free vulnerability (2011-05-10)',
    'Metasploit Browser Autopwn (USE AT OWN RISK!)\n']

browser_exploits_text = """
 Ingrese el exploit de navegador que le gustaría usar [8]:
"""

# this is for the powershell attack vectors
powershell_menu = ['Inyector de Shellcode Alfanumérico Powershell',
                   'Shell Inverso Powershell',
                   'Shell Bind Powershell',
                   'Volcado de Base de Datos SAM Powershell',
                   '0D']

powershell_text = ("""
El módulo de """ + bcolors.BOLD + """Vector de Ataque Powershell""" + bcolors.ENDC + """ le permite crear ataques específicos de PowerShell. Estos ataques le permitirán usar PowerShell que está disponible por defecto en todos los sistemas operativos Windows Vista y superiores. PowerShell proporciona un paisaje fructífero para desplegar payloads y realizar funciones que no son detectadas por tecnologías preventivas.\n""")


encoder_menu = ['shikata_ga_nai',
                'Sin Codificación',
                'Multi-Codificador',
                'Ejecutable con Puerta Trasera\n']

encoder_text = """
Seleccione una de las siguientes, 'ejecutable con puerta trasera' es típicamente la mejor. Sin embargo,
la mayoría aún son detectados por AV. Puede necesitar hacer empaquetado/cifrado adicional
para evadir la detección básica de AV.
"""

dll_hijacker_text = """
 La vulnerabilidad DLL Hijacker permitirá que extensiones de archivo normales
 llamen a archivos .dll locales (o remotos) que luego pueden llamar a su payload o
 ejecutable. En este escenario compactará el ataque en un archivo zip
 y cuando el usuario abra la extensión del archivo, activará la dll y luego
 finalmente nuestro payload. Durante el momento de este lanzamiento, todas estas
 extensiones de archivo fueron probadas y parecen funcionar y no están parcheadas. Esto
 se actualizará continuamente con el tiempo.
"""

fakeap_dhcp_menu = ['10.0.0.100-254',
                    '192.168.10.100-254\n']

fakeap_dhcp_text = "Por favor elija la configuración DHCP que le gustaría usar: "
