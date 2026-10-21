##### CREACION DE PERSONAJES #####
define mel = Character("Melani")
define lau = Character("Laura")
define ros = Character("Rocio")

define paSanti = Character("Papá de Santiago")
define maVale = Character("Mamá de Valentina")

define fran = Character("Francisco")
define pab = Character("Pablo")
define santi = Character("Santiago")
define sof = Character("Sofia")
define vale = Character("Valentina")

define resExcelente = Character("¡Excelente Trabajo!")
define resBuen = Character("¡Buen Trabajo!")
define resAMej = Character("¡A mejorar!")

##### SPRITES #####
#image melani_normal = "images/melani_normal.png"
#image laura_normal = "images/laura_normal.png"


##### FONDOS #####
#image menu = "images/menu.png"
#image puerta = "images/puerta_entrada.png"
#image recepcion = "images/recepcion.png"
#image cocina = "images/cocina.png"
#image patio = "images/patio.png"
#image sala5 = "images/sala_5.png"
#image sala4 = "images/sala_4.png"



##### PUNTAJES #####
init:
    $ puntaje = 0


##### POSICION EN PANTALLA #####
transform posIzq:
    xpos 300
    ypos 100

transform posDer:
    xpos 1280
    ypos 100