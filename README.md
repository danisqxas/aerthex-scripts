# 🧠 Aerthex Scripts

> Repositorio de herramientas y scripts de propósito ofensivo y analítico desarrollados por **Aerthex**. Enfocado en ciberseguridad, automatización y pruebas de concepto técnicas.

![status](https://img.shields.io/badge/status-maintained-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)
![platform](https://img.shields.io/badge/platform-Windows%20%7C%20Unix-lightgrey)
![focus](https://img.shields.io/badge/focus-OffSec%20%7C%20Forensics-critical)

---

## 📁 Estructura del repositorio

```bash
aerthex-scripts/
├── payloads/           # Inyección de código y exploits
│   └── PayloadInject.c
├── scanners/           # Reconocimiento y análisis de red
│   ├── scan_hosts.py
│   └── LeakScan-Script.py
├── helpers/            # Scripts complementarios
│   └── User_Activity_V1.1.py


---

## 📦 Uso por script

### 🔹 PayloadInject.c (C)
Herramienta de inyección de DLLs en procesos Windows:

```bash
x86_64-w64-mingw32-gcc PayloadInject.c -o injector.exe
injector.exe <PID> C:\\ruta\\a\\la\\dll.dll

