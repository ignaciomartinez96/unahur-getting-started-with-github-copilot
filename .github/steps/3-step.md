## Paso 3: Activa el Hipervelocidad - Copilot Agent Mode 🚀

### 📖 Teoría: ¿Qué es Copilot Agent Mode?

Copilot [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) es la siguiente evolución en la codificación asistida por IA. Actando como un colega programador autónomo, realiza tareas de codificación de múltiples pasos bajo tu comando.

Copilot Agent Mode responde a errores de compilación y lint, monitorea salida de terminal y pruebas, y auto-corrige en un bucle hasta que se complete la tarea.

#### Agent Mode (de un vistazo)

| Aspecto | 🚪 Agent Mode |
| --- | --- |
| Autonomía y planificación | Desglosa solicitudes de alto nivel en trabajo de múltiples pasos e itera hasta que se complete la tarea. |
| Recopilación de contexto | Usa tu contexto actual y puede descubrir archivos adicionales relevantes cuando sea necesario. |
| Uso de herramientas | Selecciona e invoca herramientas automáticamente; también puedes dirigir herramientas con menciones como `#codebase`. |
| Comprobaciones de aprobación y seguridad | Las acciones sensibles pueden requerir aprobación antes de la ejecución, ayudándote a mantener el control. |

#### 🪧 Herramientas de Agent Mode

Agent mode usa herramientas para realizar tareas especializadas mientras procesa una solicitud del usuario. Ejemplos de tales tareas son:

- Buscar archivos relevantes para completar tu prompt
- Obtener contenido de una página web
- Ejecutar pruebas o comandos de terminal

> [!TIP]
> Aunque VS Code proporciona muchas herramientas integradas, también puedes proporcionar a Agent Mode poderes más específicos del dominio a través de **MCP tools**.
>
> Lee más sobre [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) y [GitHub MCP Server](https://github.com/github/github-mcp-server)

¡Ahora, probemos **Agent Mode**! 👩‍🚀

### :keyboard: Actividad: Usa Copilot para agregar una nueva característica! :rocket:

Nuestro sitio web lista actividades, ¡pero mantiene la lista de invitados en secreto 🤫

¡Usemos Copilot para cambiar el sitio web para mostrar estudiantes registrados bajo cada actividad!

1. En la parte inferior de la ventana de Copilot Chat, usa el dropdown para cambiar a **Agent** mode.

   <img width="350" alt="image" src="../images/agent-mode-dropdown.png" />

1. Abre los archivos relacionados con nuestra página web y luego arrastra cada ventana del editor (o archivo) al panel de chat, informando a Copilot para usarlos como contexto.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **Nota:** Agregar archivos como contexto es opcional. Si saltas esto, Copilot Agent Mode todavía puede usar herramientas como `#codebase` para buscar archivos relevantes de tu prompt. Agregar archivos específicos ayuda a apuntar a Copilot en la dirección correcta, lo cual es especialmente útil en bases de código más grandes.

   <img width="400" alt="image showing files added to context" src="../images/files-added-to-context.png" />

   > 💡 **Consejo:** También puedes usar el botón **Add Context...** para proporcionar otras fuentes de elementos de contexto, como un GitHub issue o los resultados de una ventana de terminal.

1. Pidéle a Copilot que actualice nuestro proyecto para mostrar los participantes actuales de actividades. Espera un momento a que lleguen las sugerencias de edición y se apliquen.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hola Copilot, ¿puedes editar las tarjetas de actividad para agregar una sección de participantes?
   > Mostrará qué participantes ya están registrados para esa actividad como una lista con viñetas.
   > ¡Recuerda hacerlo bonito!
   > ```

   Después de que Copilot termine el trabajo, tienes el control de qué cambios se quedan. 

   Usando los botones **Keep** que se muestran a continuación, puedes aceptar/descartar todos los cambios o revisar y decidir cambio por cambio. Esto se puede hacer desde la vista del panel de chat o mientras inspeccionas cada archivo editado.

      <img width="900" alt="buttons to keep or discard changes" src="../images/review-changes-buttons.png" />


1. Antes de simplemente aceptar los cambios, verifica nuestro sitio web de nuevo y confirma que todo se actualizó como se esperaba.
   
   Aquí hay un ejemplo de una tarjeta de actividad actualizada. Puede que necesites reiniciar la aplicación o refrescar la página.

   <img width="350" alt="Activity card with participant info" src="../images/activity-card-with-participants.png" />

   > 🪧 **Nota:** Tu tarjeta de actividad puede verse diferente. Copilot no siempre producirá los mismos resultados.

   <details>
   <summary>¿Necesitas ayuda? 🤷</summary><br/>
   Si el sitio web no se está cargando, aquí hay algunas cosas para verificar.

   - Reinicia el Debugger de VS Code para asegurar que se sirva la versión más reciente del sitio web.
   - Si olvidaste la URL, o cerraste la ventana, por favor revisa el paso 1.
   - Intenta refrescar la página web duro o abrir en una ventana privada para que descargue una copia nueva.

   </details>

1. Ahora que hemos confirmado que nuestros cambios son buenos, usa el panel para ciclar a través de cada edición sugerida y presiona **Keep** para aplicar el cambio.

   > 💡 **Consejo:** Puedes aceptar los cambios directamente, modificarlos, o proporcionar instrucción adicional para refinarlos usando la interfaz de chat.

### :keyboard: Actividad: Usa Agent mode para agregar botones funcionales "unregister"

Experimentemos con solicitudes más abiertas que agregarán más funcionalidad a nuestra aplicación web.

Si no obtienes los resultados deseados, puedes intentar otros modelos o proporcionar comentarios de seguimiento para refinar los resultados.

1. Asegúrate de que tu Copilot todavía esté en **Agent** mode.

   <img width="250" alt="agent mode" src="../images/agent-mode-dropdown.png" />

1. Haz clic en el icono **Tools** y explora todas las Herramientas actualmente disponibles para Copilot Agent Mode.

   <img width="250"  alt="tools icon" src="../images/tools-icon.png" />

1. ¡Hora de nuestra prueba! Pidámosle a Copilot que agregue funcionalidad para eliminar participantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Por favor agrega un icono de eliminar junto a cada participante y oculta los puntos.
   > Cuando se haga clic, desinscribirá a ese participante de la actividad.
   > ```

   La herramienta `#codebase` es usada por Copilot para encontrar archivos relevantes, fragmentos de código que sean relevantes para la tarea en cuestin.

   > 🪧 **Nota:** En este laboratorio incluimos explícitamente la herramienta `#codebase` para obtener los resultados más repetibles.
   > Siéntete libre de intentar el prompt **sin** `#codebase` y observa si Agent Mode decide reunir contexto más amplio del proyecto por sí solo.

1. Cuando Copilot termine, inspecciona los cambios de código y los resultados en el sitio web. Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta proporcionar a Copilot algunos comentarios para refinar los resultados.

   > 🪧 **Nota:** Si no ves actualizaciones en el sitio web, puede que necesites reiniciar el debugger

1. Pidéle a Copilot que arregle un bug de registro.

   > 💡 **Consejo:** Te recomendamos que pruebes el flujo de registro tú mismo para que puedas ver claramente los cambios de comportamiento antes y después.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > He notado que parece haber un bug.
   > Cuando se registra un participante, la página debe actualizarse para ver el cambio en la actividad.
   > ```

1. Cuando Copilot termine, inspecciona los resultados y valida el flujo de registro en el sitio web.

   Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta proporcionar a Copilot algunos comentarios.

1. **Commit** y **push** todos tus cambios a la rama `accelerate-with-copilot`.

1. Espera a que Mona verifique tu trabajo y comparta el siguiente paso.