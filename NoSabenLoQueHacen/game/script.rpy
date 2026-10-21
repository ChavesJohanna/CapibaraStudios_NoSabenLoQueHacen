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
            jump op1

        "Consolar a Santiago":
            "se eligio op 2"
            $puntaje +=1
            jump op2

        "Hablar con ambos":
            "se elijio op 3"
            $puntaje +=2
            jump op3

    #return

label op1:
    "camino de la opcion 1"
    "cantidad de puntaje [puntaje]"

    mel "Santiago tranquilo ya pasó..."
    mel "Valentina ordena los juguetes por favor."

    vale "Pero.."

    mel "En un ratito vamos a tomar el té."
    mel "Ordenemos la salita..."

    vale "..."

    santi "..."

    mel "{i}No se que paso pero los chicos se ven descontentos{/i}"
    mel "{i}Tengo que estar más atenta.{/i}"

    jump resultadoMejorar



label op2:
    "camino de la opcion 2"
    "cantidad de puntaje [puntaje]"

    mel "Chicos que paso?"
    mel "{i}Santiago esta en el suelo llorando.{/i}"
    mel "{i}Me pregunto que pasó...{/i}"
    mel "{i}Tengo que tranquilizarlo.{/i}"

    santi "Snif..."

    mel "Santiago..."
    mel "Tranquilo..."
    mel "Ya pasó... ya pasó"
    mel "Tranquilo si?"

    santi "..."
    santi "..."

    mel "{i}Hay un peluche sobre los bloques...{/i}"
    mel "Valentina ten más cuidado."

    vale "..."
    vale "Yo no hice nada."

    mel "Mmm..."
    mel "{i}...{/i}"
    mel "{i}No tendria que haberme ido.{/i}"
    mel "{i}Seré más cuidadosa la proxima vez.{/i}"

    jump resultadoBuen



label op3:
    "camino de la opcion 3"
    "cantidad de puntaje [puntaje]"

    mel "¿Que pasó chicos?"
    mel "Me cuentan por favor..."

    santi "Snif... ella fue..."

    vale "Yo no hice nada."

    mel "Valentina cuentame que paso antes de que llorara tu compañerito."

    vale "Estabba jugando yy lo tiré..."

    mel "{i}Parece que tiró la torre con un peluche{/i}"
    mel "Esta bien... sabes por que esta llorando?"

    vale "No..."

    mel "Él estaba jugando con su torre que le tomo tiempo construir..."
    mel "y cuando tiraste el peluche, la torre se cayó..."
    mel "eso lo puso triste... la torre era importante para él..."
    mel "entiendes?"

    vale "..."
    vale "si..."

    mel "Bueno... que te parece si le pedimos perdón."
    mel "Decile “Perdón, fue un accidente.”"

    vale "..."
    vale "Perdón..."

    mel "Bien hecho vale..."
    mel "Santiago... esta bien que te sientas triste."
    mel "Tu compañera no queria lastimarte, fue un accidente..."
    mel "¿Quieres un abraso?"

    santi "..."
    santi "si..."
#se abrazan
    mel "..."
    mel "Valentina ¿que tal si le ayudamos a contruir otra torre?"
    mel "¿Que dices?"
    
    vale "Sii."

    mel "Santiago contruyamos una más alta los tres."
    mel "¿Que te parece?"

    santi "..."
    santi "Esta bien...!"

    mel "{i}Fiuu eso salió bien{/i}"
    mel "{i}Ahora juguemos un ratito con ellos{/i}"

    jump resultadoExcelente


label resultadoExcelente:

    resExcelente "Tus decisiones favorecieron un ambiente seguro y permitieron que los niños expresaran lo que sentían."
    resExcelente "Además de resolver las situaciones del momento..."
    resExcelente "ayudaste a que comenzaran a desarrollar herramientas para relacionarse con los demás."

    resExcelente "{b}Para recordar:{/b} acompañar a los niños en los conflictos también es una oportunidad para enseñarles a resolverlos."

    jump final


label resultadoBuen:

    resBuen "Lograste responder adecuadamente a la mayoría de las situaciones y mantener un ambiente de cuidado."
    resBuen "En algunas situaciones, sin embargo..."
    resBuen "podrías darles a los niños más espacio para expresar lo que sienten y participar en la resolución del conflicto."

    resBuen "{b}Para recordar:{/b} no solo importa resolver el conflicto, sino también acompañar a los niños para que puedan comprenderlo y buscar soluciones."

    jump final


label resultadoMejorar:

    resAMej "Algunas de tus decisiones permitieron resolver las situaciones rápidamente."
    resAMej "pero no siempre tuvieron en cuenta lo que los niños estaban sintiendo..."
    resAMej "o la posibilidad de que participaran en la resolución del conflicto."

    resAMej "{b}Una próxima vez:{/b} antes de intervenir, intentá observar qué está ocurriendo..."
    resAMej "escuchar a los niños y ayudarlos a encontrar una solución adecuada."

    resAMej "{b}Para recordar:{/b} acompañar no significa resolver todo por ellos."

    jump final



label final:
    "haz llegado al final..."
    "¡Gracias por jugar!"
    "La historia continuara..."
    return