# 🧠 Blog Agent Framework

**Crea articulos de blogs inteligentes y de alta calidad en forma automática.**

**Blog Agent Framework** es una libreria en Python que te permite generar ariculos de blog usando un equipo de agentes de inteligencia artificial. Basada en [Autogen de Microsoft](https://microsoft.github.io/autogen), esta herramienta simula el proceso de escritura profesional: un redactor, un crítico y varios revisores trabajan en conjunto para crear contenido claro, optimizado para SEO, y atractivo para el lector.  Además, aplica las mejores prácticas del marketing digital para mejorar el alcance, la estructura y el impacto de cada publicación.

Ideal para creadores de contenido, emprendedores, educadores o desarrolladores que quieren generar textos de calidad sin complicaciones.

---

## 🔧 Características

- **🧩 Arquitectura modular de agentes**  
  Incluye agentes especializados para:
  - **Redacción** – Crea publicaciones con lenguaje sencillo y estilo narrativo  
  - **Revisión de Marketing de Contenidos** – Mejora la estructura, claridad y atractivo del texto  
  - **Revisión de Claridad y Ética** – Verifica que el contenido sea comprensible y libre de lenguaje confuso o inapropiado  
  - **Revisión SEO** – Optimiza el contenido para mejorar su visibilidad en Google y otros motores de búsqueda

- **💬 Colaboración inteligente entre agentes**  
  Cada agente cumple una función específica dentro de un flujo de revisión automatizado. El crítico recoge las opiniones de los revisores y produce un texto final refinado.

- **📦 Úsalo como biblioteca o base para una API**  
  - Puedes usar la librería directamente en tus proyectos de Python  
  - O crear tu propia API para generar blogs automáticamente desde una web o aplicación

- **✅ Contenido optimizado para buscadores y personas**  
  El contenido está diseñado para ser fácil de leer, especialmente para lectores con nivel general o básico, y a la vez eficaz en términos de posicionamiento SEO.

---

## 🚀 Instalación


[![PyPI version](https://badge.fury.io/py/blog-agent-framework.svg)](https://badge.fury.io/py/blog-agent-framework)


Instalar desde PyPI:

```bash
pip install blog-agent-framework
```
<sub>Requiere Python 3.11+</sub>

Instala la biblioteca directamente desde GitHub usando `pip`:

```bash
pip install git+https://github.com/edilma/AI-Agent-Orchestrator.git
````

---

## ✍️ Uso básico

Aquí te mostramos cómo ejecutar el ejemplo incluido.

### ▶️ Ejecutar el ejemplo

1. **Entra a la carpeta de ejemplos:**

```bash
cd examples
```

2. **Copia el archivo de entorno desde la plantilla:**

```bash
# En Windows
copy .env.example .env

# En macOS o Linux
cp .env.example .env
```

3. **Agrega tus credenciales de OpenAI al archivo `.env`:**

```env
OPENAI_API_KEY=tu_clave_de_openai
OPENAI_PROJECT_ID=tu_id_de_proyecto
```

4. **Ejecuta el script:**

```bash
python run_example.py
```

Esto activará el sistema de agentes, generará un blog y mostrará cómo se realiza el ciclo completo de redacción y revisión.

---

## 🧠 ¿Cómo funciona?

Blog Agent Framework simula un proceso de redacción colaborativo con un conjunto de agentes especializados en IA. Cada agente tiene una tarea específica:

1. **Agente Redactor**
   Genera un borrador del blog a partir de un tema. Usa lenguaje sencillo y un estilo narrativo para enganchar al lector.

2. **Agente Crítico**
   Revisa el borrador, analiza la estructura, claridad, tono y narrativa, e incorpora las sugerencias de los demás agentes para entregar una versión mejorada.

3. **Agente SEO**
   Evalúa la presencia de palabras clave, encabezados y elementos esenciales para mejorar el posicionamiento en buscadores.

4. **Agente de Marketing de Contenidos**
   Verifica que el blog tenga buena estructura, lógica y sea fácil de seguir.

5. **Agente de Claridad y Ética**
   Asegura que el texto sea comprensible para cualquier lector, sin lenguaje confuso o inadecuado.

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
Puedes usarlo, modificarlo y distribuirlo libremente, con atribución.

---

## ✨ Autor

Creado con 💻 por **Edilma Riano**
Ayudando a empresas y creadores a usar IA para trabajar de forma más inteligente y escalar más rápido.

🔗 [Visita mi perfil en GitHub](https://github.com/edilma)

```

---

