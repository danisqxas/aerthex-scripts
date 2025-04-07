# PayloadInject.c

Este es un script en C diseñado para inyectar una DLL en un proceso de Windows usando diferentes métodos. Actualmente incluye la opción de inyección por `CreateRemoteThread` y `NtCreateThreadEx`.

## Características

- Permite inyectar DLLs en procesos especificados por PID.
- Utiliza funciones nativas de Windows (`CreateRemoteThread`, `NtCreateThreadEx`).
- Código comentado y estructurado para su fácil comprensión y modificación.
- Modo de uso sencillo desde la línea de comandos.

## Requisitos

- Sistema operativo Windows.
- Tener instalado GCC (puede compilarse con MinGW).
- Ejecutar con permisos de administrador (en algunos casos necesarios para ciertos procesos).

## Compilación

Abrí una terminal y ejecutá:

```bash
gcc PayloadInject.c -o injector.exe
Uso
Una vez compilado, podés ejecutar el binario con los siguientes parámetros:
bash
injector.exe <PID> <ruta_completa_de_la_DLL> <método>
Ejemplo:
bash
injector.exe 1234 "C:\\Users\\Usuario\\Desktop\\mi_payload.dll" 1
Donde:

1234 es el PID del proceso objetivo.

"C:\\Users\\Usuario\\Desktop\\mi_payload.dll" es la DLL que será inyectada.

1 es el método de inyección (1 para CreateRemoteThread, 2 para NtCreateThreadEx).

Métodos de Inyección Soportados
ID	Método
1	CreateRemoteThread
2	NtCreateThreadEx
Advertencias
Esta herramienta fue creada con fines educativos.

El uso inadecuado puede violar términos legales o políticas de seguridad de terceros.

Usala con responsabilidad, solo en entornos controlados o con consentimiento.

Ejemplo visual
A continuación se muestra una captura del uso exitoso del script:



Contacto
Podés encontrarme en Twitter (X) para consultas, ideas o colaboraciones.

⚠️ Disclaimer: El autor no se hace responsable por el uso indebido de este código.
Este proyecto fue hecho únicamente con fines educativos y de investigación.
