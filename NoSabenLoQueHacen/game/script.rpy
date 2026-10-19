# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy at posDer


    #show eileen at posIzq

    # Presenta las líneas del diálogo.

    #e "Has creado un nuevo juego Ren'Py."

    #e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"


    #####  DE AQUI EMPIEZAN LOS DIALOGOS DEL JUEGO #####

    #scene puerta 

    #show melani_normal

    mel "Bien… ya estoy aquí."
    mel "¡Qué emoción! espero poder usar todo lo que aprendí."
    mel "{i} ¿Cómo se llamaba la directora? {/i}"
    mel "{i} Mmm... {/i}"
    mel "{i} De última le pregunto su nombre. {/i}"

    #scene recepcion

    lau "Hola Melani! Buen día."
    lau "Que bueno que llegaste."
    lau "Antes que nada necesito que firmes la asistencia."

    mel "¡Claro!"
    mel "Creo que llegue un poco temprano."

    lau "No te preocupes por eso."
    lau "Te da algo de tiempo para adaptarte."
    lau "¿Quieres un tour por las aulas?..."
    lau "o prefieres que vayamos a tu sala?"

    mel "Mmm..."

    menu:
        "Dar un recorrido":
            jump recorrido
        "Ir directo a la sala":
            jump irSala

    # Finaliza el juego:

    #return

label recorrido:
    mel "Mejor recorremos un poco."
    mel "Así me guío mejor."

    lau "Bueno pasemos entonces."
    lau "Primero tenemos la cocina"

    #scene cocina

    lau "Rocío es la encargada de la cocina."
    lau "Después de izar la bandera pasará por tu sala para servir el té a los chicos."
    lau "Ten preparados sus manteles y sus tacitas."

    mel "Esta bien."
    mel "¿Le dan almuerzo también?"

    lau "¡Claro! Rocio también se encarga de eso."
    lau "Así que no tienes de qué preocuparte."

    #scene patio

    lau "Luego tenemos el patio."
    lau "Tenemos algunos juegos."
    lau "A media mañana suena el timbre para el recreo de los chicos."
    lau "Ten en cuenta de que algunos son muy de jugar a lo bruto."
    lau "Estate bien atenta por si alguno se está por caer o algo parecido."
    
    #scene sala5
    
    mel "¿Esta es mi sala?"
    mel "Es bastante amplia."
    mel "¡Incluso hay muchos juguetes!"
    mel "¡Es muy bonita!"

    lau "Verdad que tiene bastante."
    lau "Pero no es tu sala."
    lau "Aquí es donde trabaja Elena."
    lau "La seño de la sala de 5 años."

    mel "Bueno… ¡Me servirá de guía para decorar la mía!"

    lau "me agrada tu motivación."
    
    jump caminoLineal1


label irSala:
    mel "¡Vamos directo!"
    mel "Estoy muy emocionada por conocer mi sala."

    lau "Bueno vamos entonces."

    #scene cocina

    mel "{i}Esta parece ser la cocina… {/i}"
    mel "{i}¿Será que dan desayuno y almuerzo? {/i}"
    mel "{i}Ohh, un cartel…  “Desayuno xhs” {/i}"
    mel "{i}Parece que si hay desayuno. {/i}"

    #scene patio

    mel "{i}Ooh el patio tiene varios juego… {/i}"
    mel "{i}Ya me imagino a los chicos divirtiéndose. {/i}"

    #scene sala5

    mel "AAA esta muy bonita!"
    mel "Es más amplia de lo que me imagine."

    lau "Todavía falta para que lleguemos Melani."

    mel "Que?"
    mel "{i}Entonces no es esta…? {/i}"
    mel "{i}Bueno no perdamos la esperanza. {/i}"


    jump caminoLineal1


label caminoLineal1:
    #scene sala4

    lau "Ahora si… Taran!"
    lau "Esta es tu sala."

    mel "Está… {w=0.5}algo vacía…"

    lau "La inauguramos hace poco."
    lau "Para que los chicos estén más cómodos."
    lau "Trabajar con muchos niños siendo tan pocas seños es muy cansado."
    lau "Y como una de las auxiliares está de licencia."
    lau "Andamos con poco personal."
    lau "Hasta que llegó nuestra salvadora."

    mel "¿Quién yo?"

    lau "¡Por supuesto!"
    lau "Llevamos algunas de las mesas y sillas de la otra sala hasta aquí."
    lau "Y como es tu primer día empezarás con 5 de los chicos."
    lau "Al menos hasta que agarres maña."
    lau "Ponte cómoda… iré a traer la planilla de asistencia de los chicos."

    mel "¡Está bien!"
    mel "De paso iré preparando algunas de las actividades que traje."

    lau "Bueno ya vuelvo."

    mel "Bien… hoy trabajaremos los alimentos saludables."
    mel "{i}Para aprovechar iré pegando las caritas y colocando la división de saludable y No saludable en el pizarrón. {/i}"

    lau "Holis! ya volví y te traje la planilla."
    lau "También quería avisarte que ya llegaron algunos de los chicos."

    mel "Gracias! creo que medio prepare la sala."
    mel "Enseguida voy para la recepción."

    lau "Bueno, cualquier cosa estoy en la dirección por si necesitas algo."
    lau "Ten un buen dia Melani."

    mel "Bien, gracias Laura."
    mel "{i}Okey entonces a quienes vamos a tener hoy? {/i}"
    mel "{i}Francisco, Pablo, Sofía, Santiago y Valentina… {/i}"
    mel "{i}Bueno vamos a conocerlos entonces. {/i}"

    #scene recepcion

    mel "{i}Ooh, son dos. {/i}"
    mel "Buenas, me llamo Melani"
    mel "Soy la maestra de salita de 4"

    paSanti "Buen dia, soy el papá de Santiago."
    paSanti "Saluda a la nueva seño…"

    santi "..."

    paSanti "Es algo tímido al principio."

    mel "Aa, no se preocupe."
    mel "Hola Santi, soy Melani."

    santi "Hola..."

    mel "Vamos al aula qué te parece?"

    santi "Si..."

    maVale "Buen día, ¿usted es la maestra de 4 verdad?"

    mel "Sí, mi nombre es Melani."

    vale "Holaaa."

    maVale "Bueno te la dejo, me tengo que ir."
    maVale "Chau hija, nos vemos más tarde."

    mel "Si esta bien, que tenga buen dia!"

    paSanti "Yo también me retiro."
    paSanti "Portate bien con la seño."

    santi "Sí papá."

    mel "Vamos al aula chicos"

    vale "Siii"
    santi "Si"

    #scene sala4

    mel "Chicos en la esquina hay algunos juguetes para que se diviertan."

    santi "Bueno..."
    vale "Siii"

    mel "{i}Son tan lindos. {/i}"
    mel "{i}Okey vamos anotando en la asistencia. {/i}"
    mel "{i}Mmm… {/i}"
    mel "{i}Parece que a Vale le gustan los peluches. {/i}"
    mel "{i}Y Santiago eligió los bloques. {/i}"
    mel "{i}Bueno… {w=0.5}ya que están distraídos. {/i}"
    mel "{i}Aprovecho y reviso la recepción de nuevo. {/i}"
    mel "Chicos ya vuelvo."
    mel "Voy a buscar a sus compañeritos."

    santi "..."
    vale "Buenoo"

    #scene recepcion

    mel "¡Buen día!"
    "..."
    "..."
    "..."
    mel "Vamos a la salita chicos."

    #scene sala4

    mel "Ya volvii!"
    mel "Aaa, Que pasó!?"

    santi "Snif..."

    vale "Seño se puso a llorar."

    mel "{i}Ahora que hago!? {/i}"

    menu:
        "Dejarlo pasar":
            "se eligio op 1"
            jump caminoLineal2

        "Consolar a Santiago":
            "se eligio op 2"
            $puntaje +=1
            jump caminoLineal2
        "Hablar con ambos":
            "se elijio op 3"
            $puntaje +=2
            jump caminoLineal2

    #return

label caminoLineal2:
    "camino lineal 2"
    "cantidad de puntaje [puntaje]"

    return