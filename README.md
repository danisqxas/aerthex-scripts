# 🧠 Aerthex Scripts — Herramientas Profesionales para Ciberseguridad Ofensiva y Automatización Técnica

Bienvenido a *Aerthex Scripts, una colección curada de herramientas enfocadas en **pruebas de intrusión, análisis forense y automatización técnica. Este repositorio es resultado del estudio continuo, la práctica ética y la pasión por la **seguridad ofensiva aplicada*.

Cada script ha sido desarrollado con objetivos claros: funcionalidad inmediata, bajo consumo de recursos y facilidad de integración en entornos de auditoría reales o laboratorios de aprendizaje.

---

![status](https://img.shields.io/badge/estado-activo-brightgreen)
![platform](https://img.shields.io/badge/plataforma-multiplataforma-purple)
![focus](https://img.shields.io/badge/enfoque-pentesting%20%7C%20automatización-red)
![license](https://img.shields.io/badge/licencia-MIT-blue)

---

## 🧬 Filosofía del Proyecto

*Aerthex Scripts* no es solo un conjunto de utilidades técnicas. Es una declaración de principios:

- *Aprender haciendo*: scripts funcionales y documentados.
- *Desarrollar con intención*: código legible, reutilizable y adaptable.
- *Operar con ética*: uso exclusivo en entornos legales, simulados o con autorización expresa.

Este repositorio está diseñado tanto para analistas junior que se están formando como para profesionales que requieren soluciones simples y efectivas en sus flujos diarios.

---

## 📁 Estructura del Proyecto


aerthex-scripts/
├── scanners/              # Detección de hosts y análisis de red
│   ├── scan_hosts.py
│   └── LeakScan-Script.py
├── helpers/               # Recolección forense y análisis local
│   └── User_Activity_V1.1.py


Cada carpeta responde a una categoría funcional: descubrimiento, análisis pasivo, recolección de evidencia o automatización de tareas.

---

## ⚙ Requisitos Técnicos

Para ejecutar los scripts, se recomienda:

- *Python 3.6+*
- *Sistema operativo:* Linux, macOS o Windows (según el script)
- *Dependencias:*

bash
pip install -r requirements.txt


> Nota: Algunos scripts pueden requerir permisos elevados (sudo) o privilegios de administrador, especialmente en funciones de auditoría local o escaneo de red.

---

## 🔍 Herramientas Incluidas

### 1. scan_hosts.py  
*Escaneo de red liviano.* Detecta hosts activos en un rango de IP.

bash
python3 scan_hosts.py --target 192.168.1.0/24


*Funciones clave:*
- Descubrimiento rápido de dispositivos conectados.
- Mínimo uso de recursos.
- Ideal para reconocimiento inicial.

---

### 2. LeakScan-Script.py  
*Verificación de filtraciones de datos.* Comprueba si un correo ha sido expuesto en brechas públicas.

bash
python3 LeakScan-Script.py -e correo@dominio.com


*Características:*
- Compatible con APIs de búsqueda de leaks.
- Informa número y fuente de exposiciones.
- Apto para auditorías de higiene digital.

---

### 3. User_Activity_V1.1.py  
*Recolección forense.* Extrae historial de comandos, accesos recientes y trazas de actividad del usuario.

bash
python3 User_Activity_V1.1.py


*Incluye:*
- Historial de bash o PowerShell.
- Últimos archivos abiertos.
- Información útil para análisis post-compromiso.

---

## 🌐 Compatibilidad por Sistema Operativo

| Script                | Linux | Windows | macOS |
|----------------------|:-----:|:-------:|:-----:|
| scan_hosts.py      |   ✅   |    ❌    |  ✅   |
| LeakScan-Script.py |   ✅   |   ✅     |  ✅   |
| User_Activity.py   |   ✅   |   ✅     |  ⚠ (parcial)

> Los scripts son modificables para ampliar su compatibilidad o integrarse en pipelines personalizados.

---

## ⚠ Consideraciones Éticas y Legales

El contenido de este repositorio está estrictamente orientado a:

- Formación profesional.
- Evaluaciones técnicas en entornos controlados.
- Pruebas de seguridad *autorizadas*.

*No debe utilizarse en sistemas de terceros sin consentimiento.* El autor no se responsabiliza por usos indebidos o ilegales de estas herramientas.

---

## 📜 Licencia

Distribuido bajo licencia *MIT*. Podés modificar, distribuir o reutilizar el código con libertad, siempre respetando los términos legales.

[Ver archivo LICENSE](LICENSE)

---

## ✍ Autor

Desarrollado por [@danisqxas**](https://github.com/danisqxas), autodidacta, apasionado por el hacking ético, scripting técnico y la mejora continua de herramientas ofensivas.

*Contacto y redes:*
- GitHub: [@danisqxas](https://github.com/danisqxas)
- Twitter/X: [@daniiwnet](https://x.com/daniiwnet?s=21)

---

<div align="center">
  <strong>Hecho con ética, propósito y obsesión por la ciberseguridad ofensiva.</strong><br>
  <em>“Automatizá lo repetitivo. Analizá lo esencial. Dominá el conocimiento.”</em>
</div>
