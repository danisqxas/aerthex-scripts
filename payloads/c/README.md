# PayloadInject.c

PayloadInject.c es un programa escrito en C que implementa funcionalidades comunes utilizadas en agentes de post-explotación. Entre sus capacidades se incluyen la ejecución remota de comandos mediante reverse shell, captura de pantalla, registro de teclas (keylogger), y exfiltración de datos a través de un canal de comando y control (C2).

> Advertencia: Este proyecto es únicamente con fines educativos y de investigación. No debe ser utilizado en sistemas sin autorización explícita.

---

## Funcionalidades principales

- Reverse shell a una dirección IP y puerto configurables  
- Keylogger básico  
- Captura de pantalla  
- Exploración del sistema de archivos  
- Beaconing periódico con información del sistema (hostname y usuario)  
- Cifrado de comunicaciones utilizando XOR y codificación Base64  
- Capacidad para inyectar y ejecutar payloads remotos  

---

## Requisitos

- Sistema operativo Linux o entorno WSL  
- Compilador gcc  
- Permisos adecuados de ejecución  
- (Opcional) Entorno controlado o sandbox para pruebas  

---

## Compilación

```bash
gcc -o payload PayloadInject.c -lpthread
```
