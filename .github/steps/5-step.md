## Paso 5: Usa GitHub Copilot dentro de un pull request

¡Felicidades! Terminaste con la codificación para este ejercicio (y VS Code). Ahora es hora de fusionar nuestro trabajo. :tada: Para finalizar, aprendamos sobre dos características de acceso limitado de Copilot que pueden agilizar nuestros pull requests.

### 📖 Teoría: GitHub Copilot para pull requests

#### Resumen de pull request de Copilot

Típicamente, revisarías tus notas y mensajes de commit, luego los resumirías para la descripción de tu pull request. Esto puede llevar algo de tiempo, especialmente si los mensajes de commit son inconsistentes o el código no está bien documentado. Afortunadamente, Copilot puede considerar todos los cambios en el pull request y proporcionar los puntos altos importantes, ¡y con referencias también!

#### Revisión de código de Copilot

Más ojos en nuestro trabajo siempre es útil, así que pidámosle a Copilot que haga una primera pasada antes de un proceso normal de revisión de pares. Copilot es excelente atrapando errores comunes que se arreglan con ajustes simples, pero por favor recuerda usarlo responsablemente.

> [!NOTE]
> Estas características solo están disponibles en planes pagos de **GitHub Copilot**. [[docs]](https://docs.github.com/en/copilot/get-started/plans)

### :keyboard: Actividad: Resume y revisa un PR con Copilot

Both **Copilot pull request summaries** and **Copilot code review** have limited access, so this activity is mostly optional. If you don't have access, skip the optional steps of this activity.

1. En un navegador web, abre otra pestaña y navega a tu repositorio de ejercicio.

1. Podrías notar un **banner de notificación** sugiriendo crear un nuevo pull request. Haz clic en ese o usa la pestaña **Pull Requests** en la parte superior para **crear un nuevo pull request**. Por favor usa los siguientes detalles:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Mejorar el sistema de registro de actividades estudiantiles`

1. (Opcional) En la barra de herramientas de descripción de PR, haz clic en el icono **Copilot** y la acción **Summary**. Después de un momento, Copilot agregará una descripción basada en tus cambios. :memo:

   <img alt="Copilot summarize button" width="450px" src="../images/copilot-summarize-button.png">

1. (Opcional) En el panel de información en el lado derecho en la parte superior, localiza la sección **Reviewers** y haz clic en el botón **Request** junto a un icono **Copilot**. ¡Espera un momento a que Copilot agregue un comentario de revisión a tu pull request!

   <img alt="Copilot review button" width="300px" src="../images/copilot-review-button.png">

   > 💡 **Consejo:** Observa una entrada de log que Copilot fue solicitado para una revisión.

1. En la parte inferior, presiona el botón **Merge pull request**. ¡Buen trabajo! ¡Ya terminaste! :tada:

1. Espera un momento a que Mona verifique tu trabajo, proporcione comentarios, y publique una revisión final de este ejercicio.
