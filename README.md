# Calculadora para CI/CD con Python

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=tolarteh_cicd-pipeline-python&metric=coverage)](https://sonarcloud.io/dashboard?id=tolarteh_cicd-pipeline-python)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tolarteh_cicd-pipeline-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=tolarteh_cicd-pipeline-python)

## Integrantes

Diego Sanchez Buitrago | Tomas Olarte Hernandez

**Dueño del repositorio:** Tomas Olarte Hernandez

## Evidencias

- PR punto 9: https://github.com/tolarteh/cicd-pipeline-python/pull/1
- Pipeline fallido por error intencional: https://github.com/tolarteh/cicd-pipeline-python/actions/runs/43667126933

## Preguntas

1. ¿Qué ventajas le proporciona a un proyecto el uso de un pipeline de CI? Menciona al menos tres ventajas *específicas* y explica por qué son importantes.

**R1:** Dentro de las ventajas que vemos más importante están la retroalimentación rápida del estado de un cambio, automatización de pasos que debo tener en cuenta durante la integración y de manera última velocidad en ese proceso. La importancia en parte es porque cambio la mentalidad de cómo confío: ahora son los datos de mi pipeline lo que permite estar tranquilo que seguí todos los pasos posibles para asegurar que el artefacto se realizara con los pasos adecuados y la barrera de calidad que considero adecuada, da paz mental. Y con esa paz, otorgada por los esfuerzos de probablemnte los ingenieros más senior que tenga, otros ingenieros/as pueden proponer cambios/mejoras y tener la misma paz mental porque el pipeline no se ejecuta de manera opcional. Últimamente me lleva a una mayor velocidad manteniendo el estándar de calidad.

2. ¿Cuál es la diferencia entre una prueba unitaria, una prueba de componente y una prueba de aceptación? Da un ejemplo de algo que probarías con cada una (en el contexto de cualquier aplicación que conozcas, descríbela primero).

**R2:** Las pruebas unitarias se dedican a la parte más pequeña, la unidad de código. Ahí el desarrollador revisa que lo que tenía intención de construir funciona como lo espera en esos pequeños componentes. Las de componente tienen la misma intención que la unitaria, pero ya toman todo un componente/módulo del código para hacerlo, para ver cómo colaboran sus partes internas. La prueba de aceptación ya busca ponerse desde la perspectiva del usuario, debe seguir los pasos como los haría este para lograr una acción en el software. Entonces la diferencia principal de estas tres puebas está en el alcance que manejan y el punto de vista de donde parten.

Para el caso de odoo CRM por ejemplo tendríamos: prueba unitaria para comprobar si el cálculo del ingreso esperado de una oportunidad está bien implementado, es decir, que el valor (300.000) x probabilidad de cierre (10%) dé el valor esperado (30.000).
Una prueba de componente al módulo de oportunidades revisaría si se puede crear una oportunidad, asociarla a un cliente y guardar la etapa en la que está correctamente.
Por último, una prueba de aceptación podría ser verificar si un vendedor puede registrar un cliente potencial, convertirlo en oportunidad y asignarle una actividad de seguimiento hasta marcarla como ganada desde la interfaz.

3. Describe brevemente qué hace cada uno de los *steps* principales de tu workflow de GitHub Actions (desde el checkout hasta el push de Docker). Explica el propósito de cada uno **(qué hace y para qué se hace)**.

**R3:** Los pasos principales arrancan con el checkout con historial completo que descarga una copia del código y su historia para poderla usar en sonarcube. Luego se configura Python, luego dependencias en requirements.txt, se continua con ejecución de black sólo en modo verificación, pylint y flake8 para formateo del código. Más adelante comienzan las pruebas unitarias (de calculadora.py) y de componente (de app.py) revisando que el coverage sea mínimo del 80%.
Terminando esto exitósamente, se construye la imagen de docker, se inicia el contenedor y se realizan las pruebas de aceptación con Selenium. Se muestran los logs por si algo falla, se guardan reportes para sonar scan que es el que comprueba la quality gate. Si pasa esa gate, entra a docker hub, almacena la imagen del docker y apunta a que esta sería la latest (esto último sólo cuando se hace el push a `main`).

4. ¿Qué problemas o dificultades encontraron al implementar este taller? ¿Cómo los solucionaron? **Cada integrante** describe al menos un problema o aprendizaje propio, identificándose con su nombre.

**R4:** Inicialmente Tomas tuvo problemas en la configuración de sonar-project.properties porque pensó que el sonar.organization era como salía en la aplicación (Tomas Olarte) y no la de la url (tolarteh). Luego de corregido, la siguiente dificultad estuvo en coordinar la aprobación de PRs después que salimos del salón de clase. Por ejemplo Diego cuando fue a aprobar el Pull Request, escribió "Approve" y lo envió, pero GitHub no me dejaba hacer el merge. Luego de revisar que sólo había quedado el comentario y no como aprobación se arregló repitiendo la revisión.

5. ¿Qué ventajas ofrece construir la imagen Docker, ejecutar las pruebas de aceptación sobre ella y publicar exactamente esa misma imagen, en lugar de simplemente validar el código?

**R5:** La mayor ventaja es la consistencia. Sabemos los problemas que llevaba armar ambientes de otras maneras, ya que debíamos seguir una serie de pasos de instalación directamente sobre el sistema operativo, e incluso aunque se hiciera con scripts, podrían ocurrir errores como librerías con dependencias o más difícil, otros programas instaladas en el sistema operativo que podrían conllevar a problemas en la aplicación. Por eso el infierno de que todo funcionara en el computador del desarrollador pero que no pudiera pasar así de limpio al servidor de producción. Docker y tecnologías similares de contenedores nos ayudan a resolver esa inconsistencia entre ambientes.

6. Sobre el Pull Request de la sección 9: ¿qué pruebas agregaron y qué error de la calculadora detectaría cada una? Con el error intencional, ¿en qué paso falló el pipeline, qué pasos no se ejecutaron y cómo impidieron la protección de `main` y el pipeline que ese error llegara a `main` y a Docker Hub?

**R6:** Agregamos pruebas para operar decimales y números negativos en las unitarias, detectando posibles errores de redondeo (con los decimales) y permitir detectar errores de signo de las operaciones con negativos.
El error intencional hizo fallar 5 de 29 pruebas unitarias, en ese punto falló y no continúo el proceso. Así, no se crearon imagenes de docker (no llegó a las pruebas de aceptación) ni mucho mejor se registró el docker (esto sólo se hace cuando se está haciendo el merge a main y esto era un paso antes). La protección del main junto con un esquema de automatización de pruebas, permitió que antes incluso de entrar a revisar y aprobar el PR detectáramos problemas en la calidad del código.
