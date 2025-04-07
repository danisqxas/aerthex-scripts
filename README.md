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

