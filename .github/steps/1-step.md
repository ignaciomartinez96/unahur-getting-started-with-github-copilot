## Paso 1: Hola Copilot

¡Bienvenido a tu ejercicio **"Introducción a GitHub Copilot"**! :robot:

En este ejercicio, utilizarás diferentes características de GitHub Copilot para trabajar en un sitio web que permite que los estudiantes de la Escuela Secundaria Mergington se registren para actividades extracurriculares. 🎻 ⚽️ ♟️

<img width="600" alt="screenshot of Mergington High School WebApp" src="../images/mergington-high-school-webapp.png" />

### 📖 Teoría: Conocer GitHub Copilot

<img width="150" align="right" alt="copilot logo" src="../images/copilot-logo.png" />

GitHub Copilot es un asistente de codificación con IA que te ayuda a escribir código más rápido y con menos esfuerzo, permitiéndote enfocarte más energía en la resolución de problemas y la colaboración.

GitHub Copilot ha demostrado aumentar la productividad del desarrollador y acelerar el ritmo del desarrollo de software. Para más información, consulta [Research: quantifying GitHub Copilot's impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

Mientras trabajas en tu IDE, interactuarás con GitHub Copilot la mayoría de las veces de las siguientes maneras:

| Modo de Interacción       | 📝 Descripción                                                                                                                 | 🎯 Mejor para                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ Sugerencias Inline** | Sugerencias de código impulsadas por IA que aparecen mientras escribes, ofreciendo completaciones conscientes del contexto desde líneas individuales hasta funciones completas. | Completación de la línea actual, a veces un bloque de código completamente nuevo                                |
| **💭 Chat Inline**        | Chat interactivo limitado a tu archivo actual o selección. Haz preguntas sobre bloques de código específicos.                 | Explicaciones de código, depuración de funciones específicas, mejoras específicas                                |
| **💬 Modo Ask**           | Optimizado para responder preguntas sobre tu base de código, codificación y conceptos de tecnología general.                   | Comprender cómo funciona el código, generar ideas, hacer preguntas                                              |
| **🤖 Agent Mode**         | Modo predeterminado recomendado para la mayoría de tareas de codificación: ediciones autónomas, uso de herramientas y continuidad hasta que se complete la tarea. | Tareas de codificación diarias, desde correcciones específicas hasta trabajo de implementación de múltiples archivos |
| **🧭 Plan Agent**         | Optimizado para redactar un plan y hacer preguntas aclaratorias antes de realizar cambios de código.                           | Cuando quieres un plan revisado primero, luego transferir a la implementación                                   |

A medida que trabajes, encontrarás que GitHub Copilot puede ayudarte en varios lugares del sitio web `github.com` y en tus entornos de codificación favoritos como VS Code, Jet Brains y Xcode.

Para la codificación de hoy, practicaremos con VS Code en un entorno de desarrollo preconfigurado conocido como [GitHub Codespace](https://github.com/features/codespaces).

> [!TIP]
> Puedes aprender más sobre características actuales y futuras en la documentación [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features).

### :keyboard: Actividad: Obtén una introducción del proyecto desde Copilot Chat

Empecemos nuestro entorno de desarrollo, usa copilot para aprender un poco sobre el proyecto, y luego hazle una prueba.

1. Usa el botón inferior para abrir la página **Create Codespace** en una nueva pestaña. Usa la configuración predeterminada.

   [![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirma que el campo **Repository** es tu copia del ejercicio, no el original, y luego haz clic en el botón verde **Create Codespace**.
   - ✅ Tu copia: `/{{full_repo_name}}`
   - ❌ Original: `/skills/getting-started-with-github-copilot`

1. Espera un momento a que Visual Studio Code se cargue en tu navegador.

1. En la barra lateral izquierda, haz clic en la pestaña de extensiones y verifica que las extensiones `GitHub Copilot` y `Python` estén instaladas y habilitadas.

   <img width="350" alt="copilot extension for VS Code" src="../images/copilot-extension-vscode.png" />

   <img width="350" alt="python extension for VS Code" src="../images/python-extension-vscode.png" />

1. En la parte superior de VS Code, localiza y haz clic en el **icono Toggle Chat** para abrir un panel lateral de Copilot Chat.

   <img width="150" alt="image" src="../images/toggle-chat-icon.png" />

   > 🪧 **Nota:** Si es la primera vez que usas GitHub Copilot, tendrás que aceptar los términos de uso para continuar.

1. Asegúrate de estar en **Ask Mode** para nuestra primera interacción

   <img width="350" alt="screenshot showing Ask Mode selection in Copilot Chat" src="../images/ask-mode-selection.png" />

1. Ingresa el siguiente prompt para pedirle a Copilot que te introduzca al proyecto.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > @workspace Por favor, explica brevemente la estructura de este proyecto.
   > ¿Qué debo hacer para ejecutarlo?
   > ```

   > 🪧 **Nota:** No es necesario seguir las instrucciones recomendadas de Copilot. Ya hemos preparado el entorno para ti.

   <details>
   <summary>¿Qué es @workspace?</summary>

   ¡Gran pregunta! Este es un [chat participant](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants) especializado que explorará el repositorio del proyecto e intentará incluir contexto adicional relevante.

   </details>

1. Ahora que sabemos un poco más sobre el proyecto, ¡intentemos ejecutarlo! En la barra lateral izquierda, selecciona la pestaña `Run and Debug` y luego presiona el icono **Start Debugging**.

   <img width="300" alt="image" src="../images/run-and-debug-tab.png" />

1. Queremos ver nuestra página web ejecutándose en un navegador, así que busquemos la URL y el puerto. Si no es visible, expande el panel inferior y selecciona la pestaña **Ports**.

1. En la lista, encuentra el puerto `8000` y el enlace relacionado. Pasa el cursor sobre el enlace y selecciona el icono **Open in browser**.

   ![image](../images/open-in-browser-icon.png)

### :keyboard: Actividad: Usa Copilot para recordar un comando de terminal 🙋

¡Buen trabajo! Ahora que estamos familiarizados con la aplicación y sabemos que funciona, pidámosle a copilot ayuda para comenzar una rama para que podamos personalizar.

1. En el panel inferior de VS Code, selecciona la pestaña **Terminal** y en el lado derecho haz clic en el signo más `+` para crear una nueva ventana de terminal.

   > 🪧 **Nota:** Esto evitará detener la sesión de depuración existente que está alojando nuestro servicio de aplicación web.

1. En la nueva ventana de terminal, usa el atajo de teclado `Ctrl + I` (Windows) o `Cmd + I` (Mac) para abrir **Copilot's Terminal Inline Chat**.

1. Pidámosle a Copilot que nos ayude a recordar un comando que hemos olvidado: crear una rama y publicarla.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hola copilot, ¿cómo puedo crear y publicar una nueva rama Git llamada "accelerate-with-copilot"?
   > ```

   > 💡 **Consejo:** Si Copilot no te da exactamente lo que quieres, siempre puedes seguir explicando lo que necesitas. Copilot recordará el historial de conversación para respuestas de seguimiento.

1. Presiona el botón `Run` para permitir que Copilot inserte el comando de terminal para nosotros. ¡No necesitas copiar y pegar!

1. Después de un momento, mira en la barra de estado inferior de VS Code, en el lado izquierdo, para ver la rama activa. Ahora debería decir `accelerate-with-copilot`. ¡Si es así, ya terminaste con este paso!

1. Ahora que tu rama está publicada en GitHub, Mona ya debería estar ocupada verificando tu trabajo. Dale un momento y mantén la vista en los comentarios. Verás que responde con información de progreso y la siguiente lección.

<details>
<summary>¿Tienes problemas? 🤷</summary><br/>

Si no recibes comentarios, aquí hay algunas cosas que debes verificar:

- Asegúrate de haber creado la rama con el nombre exacto `accelerate-with-copilot`. Sin prefijos o sufijos.
- Asegúrate de que la rama fue publicada en tu repositorio.

</details>
