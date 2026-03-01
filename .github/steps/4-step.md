## Paso 4: Planifica tu implementación con el Planning Agent 🙷

En el paso anterior, Agent Mode nos ayudó a movernos rápido y enviar nueva funcionalidad. 🚀

Ahora disminuyamos la velocidad por una ronda y trabajemos como arquitectos: define un fuerte enfoque de pruebas primero, luego tránslo para implementación. Esto nos da mejor claridad, menos sorpresas, y resultados más limpios. 🪧

### 📖 Teoría: ¿Qué es Copilot Plan Agent?

Copilot [Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning) te ayuda a diseñar una solución antes de que se realice ningún cambio de código.

En lugar de saltar directamente a ediciones, investiga tu solicitud, hace preguntas aclaratorias, y elabora un plan de implementación que puedes refinar.

#### Plan Agent (de un vistazo)

| Aspecto | 🫚 Plan Agent |
| --- | --- |
| Propósito | Crea un plan de implementación estructurado antes de que inicie cualquier codificación. |
| Recopilación de contexto | Usa investigación de solo lectura para entender requisitos y restricciones. |
| Estilo de colaboración | Hace preguntas aclaratorias, luego actualiza el plan usando tus respuestas. |
| Iteración | Soporta múltiples pasadas de refinamiento antes de la implementación. |
| Seguridad | No edita archivos hasta que apruebes el plan y lo transfieras a **Agent Mode**. |
| Entrega | El botón **Start implementation** transfiere el plan aprobado a **Agent Mode** para codificación. |

> [!TIP]
> Puedes comenzar desde una solicitud de alto nivel y luego agregar restricciones y detalles en prompts de seguimiento.

### ⌨️ Actividad: Planifica e implementa pruebas backend

Tu backend sigue teniendo cero cobertura de pruebas. Usa **Plan Agent** para crear un plan, responder preguntas, e iniciar la implementación.

1. Abre el panel **Copilot Chat** y cambia a **Plan Agent**.

   <img width="350" alt="image" src="https://github.com/ignaciomartinez96/unahur-getting-started-with-github-copilot/blob/main/.github/images/plan-mode-dropdown.png?raw=true" />


1. Comencemos con un prompt amplio y Copilot nos ayudará a llenar los detalles:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Quiero agregar pruebas backend FastAPI en un directorio de pruebas separado.
   > ```

1. Espera a que Copilot genere su primer plan. Si te hace preguntas, respóndelas lo mejor que puedas.

   > 🪧 **Nota:** No te preocupes por hacerlo perfecto, siempre puedes refinar el plan más adelante.

1. Puedes refinar el plan y proporcionar detalles adicionales en prompts de seguimiento

   Aquí hay algunos ejemplos:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Utilicemos el patrón de prueba AAA (Arrange-Act-Assert) para estructurar nuestras pruebas
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Asegúrate de que usemos `pytest` y lo agreguemos al archivo `requirements.txt`
   > ```


1. Revisa el plan propuesto y cuando estés satisfecho con él, haz clic en **Start implementation** para transferir a **Agent Mode**.

   <img width="350" alt="image" src="https://github.com/ignaciomartinez96/unahur-getting-started-with-github-copilot/blob/main/.github/images/plan-mode-start-implementation.png?raw=true" />

   Observa que al hacer clic en el botón se cambió de **Plan** a **Agent Mode**. A partir de este punto, Copilot puede editar tu base de código, como antes.

1. Mira a Copilot implementar el plan que acaba de crear. Puede preguntarte por permisos para ejecutar ciertas herramientas (por ejemplo, ejecutar comandos o crear entornos virtuales). Aprueba estos permisos para que pueda continuar trabajando.

1. Revisa los cambios y asegúrate de que las pruebas se ejecuten exitosamente. Si es necesario, continúa guiándolo hasta que la implementación esté completa.

   **🎯 Meta: Obtén todas las pruebas pasando (verde) antes de que avances. ✅**

   > 🪧 **Nota:** Agent Mode puede completar esto en un paso, o puede necesitar prompts de seguimiento de ti.

1. **Commit** y **push** todos tus cambios a la rama `accelerate-with-copilot`.

1. Espera a que Mona verifique tu trabajo y comparta el siguiente paso.

<details>
<summary>¿Tienes problemas? 🤷</summary><br/>

- Si las pruebas no se ejecutaron, pidéle a Copilot que las ejecute por ti.
- Asegúrate de que `pytest` esté agregado en `requirements.txt` y que existe un directorio `tests/`.

</details>
