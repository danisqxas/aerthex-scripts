# 🧠 Aerthex Scripts — Herramientas de Ciberseguridad Ofensiva y Automatización Técnica

Bienvenido al repositorio oficial de *Aerthex Scripts, un conjunto de herramientas desarrolladas con precisión, ética y enfoque técnico, diseñadas para pruebas ofensivas, automatización de análisis y entornos de auditoría controlados. Este espacio es una extensión viva del aprendizaje, la curiosidad y la práctica constante en el mundo de la **ciberseguridad moderna*.

Cada línea de código, cada utilidad aquí presente, nace de la necesidad real de crear soluciones funcionales, livianas y adaptables, tanto para ejercicios en laboratorios como para entornos de simulación ofensiva profesional.

---

![status](https://img.shields.io/badge/estado-activo-brightgreen)
![platform](https://img.shields.io/badge/plataforma-multiplataforma-purple)
![focus](https://img.shields.io/badge/enfoque-ciberseguridad%20ofensiva-red)
![license](https://img.shields.io/badge/licencia-MIT-blue)

---

## 🧬 Filosofía del Repositorio

Este proyecto no es una simple colección de scripts. Es una apuesta por herramientas bien estructuradas, comentadas, entendibles y pensadas para escalar o integrarse fácilmente en otras soluciones. Apunta a:

- *Aprender haciendo*: código claro, técnico y funcional.
- *Compartir conocimiento*: scripts con propósitos definidos y bien explicados.
- *Actuar con ética*: cada utilidad debe ser empleada exclusivamente en contextos autorizados.

---

## 📁 Estructura del Proyecto


aerthex-scripts/
├── scanners/           # Scripts de detección y análisis de red
│   ├── scan_hosts.py
│   └── LeakScan-Script.py
├── helpers/            # Scripts auxiliares para análisis local
│   └── User_Activity_V1.1.py


Cada carpeta está pensada como un módulo temático. Los nombres de los archivos reflejan directamente su propósito y están diseñados para poder integrarse en flujos más complejos o ejecutarse como herramientas independientes.

---

## ⚙ Requisitos Técnicos

Para utilizar estas herramientas correctamente, es necesario tener instalado:

- Python 3.6 o superior
- Entorno Linux, macOS o Windows (según el script)
- Las siguientes dependencias:

bash
pip install -r requirements.txt


Nota: Algunos scripts pueden requerir permisos elevados para acceder a ciertas rutas o ejecutar operaciones de análisis local.

---

## 🔍 Descripción de Herramientas Incluidas

### 1. scan_hosts.py  
Un escáner de red liviano y rápido. Permite detectar hosts activos dentro de un rango específico, útil para tareas de reconocimiento básico.

*Ejemplo de uso:*
bash
python3 scan_hosts.py --target 192.168.1.0/24


*Lo que hace:*
- Envía solicitudes para verificar hosts vivos.
- Muestra direcciones IP activas encontradas.

*Ventajas:*
- Sin dependencias pesadas.
- Ideal para entornos controlados y pruebas rápidas.

---

### 2. LeakScan-Script.py  
Verifica si un correo electrónico ha sido expuesto en filtraciones públicas de datos. Excelente para analizar riesgos personales o institucionales de seguridad de la información.

*Ejemplo de uso:*
bash
python3 LeakScan-Script.py -e ejemplo@dominio.com


*Salida esperada:*

[+] El correo aparece en 3 bases de datos filtradas.


*Importante:*  
- Puede conectarse a APIs públicas opcionales para mejorar los resultados.
- Pensado para profesionales de ciberseguridad, educadores y auditores.

---

### 3. User_Activity_V1.1.py  
Herramienta forense liviana que recolecta evidencia de actividad del usuario en sistemas locales: historial de comandos, archivos abiertos recientemente, y más.

*Ejemplo de uso:*
bash
python3 User_Activity_V1.1.py


*Funciones:*
- Analiza historial de comandos (según SO).
- Lista accesos recientes a archivos críticos.
- Ofrece visión rápida del comportamiento del usuario.

*Ideal para:*
- Entornos forenses.
- Simulaciones de intrusión.
- Prácticas de análisis de actividad post-explotación.

---

## 🌐 Compatibilidad

| Script                | Linux | Windows | macOS |
|----------------------|:-----:|:-------:|:-----:|
| scan_hosts.py      |   ✅   |    ❌    |  ✅   |
| LeakScan-Script.py |   ✅   |   ✅     |  ✅   |
| User_Activity.py   |   ✅   |   ✅     |  ⚠   (limitado)

Nota: Todos los scripts están diseñados para ser modificables y adaptables según el entorno y la necesidad.

---

## ✍ Buenas Prácticas y Advertencia Ética

Este repositorio *no está diseñado para actividades ilegales o malintencionadas*. Todas las herramientas aquí presentes deben ser utilizadas en:

- Laboratorios personales
- Simulaciones con fines educativos
- Pruebas autorizadas en entornos de pentesting

No nos hacemos responsables por el uso indebido de este contenido.

---

## 📜 Licencia

Este proyecto se encuentra bajo la licencia MIT. Sentite libre de modificar, compartir y mejorar el código siempre que respetes los términos de la licencia.  
[Ver archivo LICENSE](LICENSE)

---

## 🙌 Autor y Contacto

Desarrollado por [@danisqxas**](https://github.com/danisqxas), entusiasta de la tecnología, autodidacta y apasionado por la seguridad ofensiva.

Podés seguir el desarrollo de herramientas, tips y contenido técnico en:

- GitHub: [@danisqxas](https://github.com/danisqxas)
- X / Twitter: [@daniiwnet](https://x.com/daniiwnet?s=21)

---

<div align="center">
  <strong>Creado con ética, precisión y mucha pasión por la ciberseguridad.</strong><br>
  <em>“Automatizá lo repetitivo. Analizá lo esencial. Dominá el conocimiento.”</em>
</div>
