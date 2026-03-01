## Paso 2: Realizando trabajo con Copilot

En el paso anterior, GitHub Copilot pudo ayudarnos a incorporarnos al proyecto. Eso solo ya es un gran ahorro de tiempo, ¡pero ahora realicemos algo de trabajo!

:bug: **HAY UN BUG EN EL SITIO WEB** :bug:

Hemos descubierto que algo está mal en el flujo de registro.
¡Los estudiantes actualmente pueden registrarse para la misma actividad **más de una vez**! Veamos qué tan lejos puede llevarnos Copilot para descubrir la causa y dar forma a una solución limpia.

Antes de sumergirnos, un rápido primer plano en cómo funciona Copilot. 🪧

### 📖 Teoría: Cómo funciona Copilot

En resumen, puedes pensar en Copilot como un colega muy especializado. Para ser efectivo con él, necesitas proporcionarle antecedentes (contexto) y dirección clara (prompts). Además, diferentes personas son mejores en diferentes cosas por sus experiencias únicas (modelos).

- **¿Cómo proporcionamos contexto?:** En nuestro entorno de codificación, Copilot considerará automáticamente el código cercano y las pestañas abiertas. Si estás usando chat, también puedes referirte explícitamente a archivos.

- **¿Qué modelo debemos elegir?:** Para nuestro ejercicio, no debería importar demasiado. ¡Experimentar con diferentes modelos es parte de la diversión! Eso es otra lección 🤖

- **¿Cómo hago prompts?:** Ser explícito y claro ayuda a Copilot a hacer el mejor trabajo. Pero a diferencia de algunos sistemas tradicionales, siempre puedes aclarar tu dirección con prompts de seguimiento.

> [!TIP]
> Hay varias otras formas de complementar el conocimiento y las capacidades de Copilot como [chat participants](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants), [chat variables](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables), [slash commands](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1), y [MCP tools](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

### :keyboard: Actividad: Usa Copilot para arreglar nuestro bug de registro :bug:

1. Pidámosle a Copilot que sugiera de dónde podría venir nuestro bug. Abre el panel **Copilot Chat** en **Ask mode** y haz la siguiente pregunta.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > @workspace Los estudiantes pueden registrarse dos veces para una actividad.
   > ¿De dónde podría venir este bug?
   > ```

1. Ahora que sabemos que el problema está en el archivo `src/app.py` y el método `signup_for_activity`, sigamos la recomendación de Copilot y arreglemos (semi-manualmente). Comenzaremos con un comentario y dejaremos que Copilot termine la corrección.
   1. Abre el archivo `src/app.py`.

      > 💡 **Consejo:** Si Copilot mencionó `src/app.py` en el chat, puedes hacer clic en el archivo directamente en la vista de chat para abrirlo.

   1. Cerca del final del archivo, busca la función `signup_for_activity`.

   1. Encuentra la línea de comentario que describe agregar un estudiante. Arriba de esto es donde parece lógico hacer nuestra verificación de registro.

   1. Ingresa el siguiente comentario y presiona enter para ir a la siguiente línea. Después de un momento, ¡aparecerá texto fantasma temporal con una sugerencia de Copilot!

      Comentario:

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="Copilot shadow text suggestion in the editor" src="https://github.com/ignaciomartinez96/unahur-getting-started-with-github-copilot/blob/main/.github/images/shadow-text.gif?raw=true" />

   1. Presiona `Tab` para aceptar la sugerencia de Copilot y convertir el texto fantasma en código.

   <details>
   <summary>Resultados de Ejemplo</summary><br/>

   Copilot crece cada día y no siempre puede producir los mismos resultados. Si no estás satisfecho con las sugerencias, aquí hay un ejemplo de un resultado de sugerencia válido que producimos durante la elaboración de este ejercicio. Puedes usarlo para continuar adelante.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: Actividad: Permite que Copilot genere datos de ejemplo 📋

En nuevas demandas de proyectos, a menudo es útil tener datos falsos realistas para pruebas. Copilot es excelente en esta tarea, así que agreguemos más actividades de muestra e introduzcamos otra forma de interactuar con Copilot usando **Inline Chat**

**Inline Chat** y el panel **Copilot Chat** son similares, pero difieren en alcance: Copilot Chat maneja preguntas más amplias, de múltiples archivos o exploratorias; Inline Chat es más rápido cuando deseas ayuda dirigida en el bloque exacto frente a ti.

1. Cerca de la parte superior del archivo `src/app.py` (alrededor de la línea 23), busca la variable `activities`, donde se configuran nuestras actividades extracurriculares de ejemplo.

1. Destaca el diccionario completo `activities` haciendo clic y arrastrando el mouse desde la parte superior hasta la inferior del diccionario. Esto ayudará a proporcionar contexto a Copilot para nuestro siguiente prompt.

   <img width="700" alt="Highlighted activities dictionary before opening inline chat" src="https://github.com/ignaciomartinez96/unahur-getting-started-with-github-copilot/blob/main/.github/images/activities-dict-highlighted.png?raw=true" />


1. Abre Copilot inline chat usando el comando de teclado `Ctrl + I` (Windows) o `Cmd + I` (Mac).

   > 💡 **Consejo:** Otra forma de abrir Copilot inline chat es: haz clic derecho en cualquiera de las líneas seleccionadas -> `Open Inline Chat`.

1. Ingresa el siguiente texto de prompt y presiona enter o el botón **Send** en el lado derecho.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Añade 2 más actividades relacionadas con deportes, 2 más actividades artísticas
   > y 2 más actividades intelectuales.
   > ```

1. Después de un momento, Copilot comenzará a hacer cambios directamente en el código. Los cambios se estilizarán de forma diferente para que cualquier adición y eliminión sea fácil de identificar. Tómate un momento para inspeccionar y verificar los cambios, y luego presiona el botón **Keep**.

   <details>
   <summary>Resultados de Ejemplo</summary><br/>

   Copilot crece cada día y no siempre puede producir los mismos resultados. Si no estás satisfecho con las sugerencias, aquí hay un resultado de ejemplo que producimos durante la elaboración de este ejercicio. Puedes usarlo para continuar adelante si tienes problemas.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. Ahora puedes ir a tu sitio web y verificar que las actividades nuevas sean visibles.

### :keyboard: Actividad: Usa Copilot para describir nuestro trabajo 💬

¡Buen trabajo arreglando ese bug y expandiendo las actividades de ejemplo! Ahora obtengamos nuestro trabajo comprometido e impulsado a GitHub, ¡de nuevo con la ayuda de Copilot!

1. En la barra lateral izquierda, selecciona la pestaña `Source Control`.

   > 💡 **Consejo:** Abrir un archivo desde el área de control de fuente mostrará las diferencias del original en lugar de simplemente abrirlo.

1. Encuentra el archivo `app.py` y presiona el signo `+` para reunir tus cambios en el área de staging.

   ![image](https://github.com/ignaciomartinez96/unahur-getting-started-with-github-copilot/blob/main/.github/images/staging-changes-icon.png?raw=true)

1. Arriba de la lista de cambios preparados, encuentra el cuadro de texto **Message**, pero **no ingreses nada** por ahora.
   - Típicamente, escribirías una breve descripción de los cambios aquí, ¡pero ahora tenemos a Copilot para ayudar!

1. A la derecha del cuadro de texto **Message**, encuentra y haz clic en el botón **Generate Commit Message** (icono de chispas).

1. Presiona el botón **Commit** y **Sync Changes** para hacer push a tus cambios en GitHub.

1. Espera un momento a que Mona verifique tu trabajo, proporcione comentarios y comparta la siguiente lección.

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your pushed the `src/app.py` file changes to the branch `accelerate-with-copilot`.

</details>
