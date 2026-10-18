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
    lau "¿Quieres un tour por las aulas? o..."
    lau "prefieres que vayamos a tu sala?"

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
    jump caminoLineal1


label irSala:
    mel "¡Vamos directo!"
    jump caminoLineal1

label caminoLineal1:
    #scene sala4

    lau "Ahora si… Taran!"
    return