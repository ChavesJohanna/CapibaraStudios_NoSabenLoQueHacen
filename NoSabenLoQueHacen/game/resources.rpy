##### CREACION DE PERSONAJES #####
define tuto = Character("Tutorial")

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
image melani_normal = "images/melani_normal.png"
image melani_feliz = "images/melani_feliz.png"
image melani_pensando = "images/melani_pensando.png"
image melani_hablando = "images/melani_hablando.png"
image melani_asustada = "images/melani_asustada.png"
image melani_cansada = "images/melani_cansada.png"

image laura_normal = "images/laura_normal.png"
image laura_amable = "images/laura_amable.png"
image laura_hablando = "images/laura_hablando.png"
image laura_mostrando = "images/laura_mostrando.png"

image paSanti_normal = "images/paSanti_normal.png"
image paSanti_hablando = "images/paSanti_hablando.png"

image maVale_normal = "images/maVale_normal.png"
image maVale_hablando = "images/maVale_hablando.png"

image santi_normal = "images/santi_normal.png"
image santi_hablando = "images/santi_hablando.png"
image santi_llorando = "images/santi_llorando.png"

image vale_normal = "images/vale_normal.png"
image vale_hablando = "images/vale_hablando.png"
image vale_preocupada = "images/vale_preocupada.png"
image vale_preocupada_hablando = "images/vale_preocupada_hablando.png"


##### FONDOS #####
image recepcion = "images/recepcion.png"
#image cocina = "images/cocina.png"
image patio = "images/patio.png"
image sala4 = "images/sala_de_melani.png"



##### PUNTAJE #####
init:
    $ puntaje = 0


##### POSICION EN PANTALLA #####
transform posIzq:
    xpos 300
    ypos 200

transform posDer:
    xpos 1280
    ypos 200

transform posCen:
    xpos 900
    ypos 200

transform posNinio1:
    xpos 1100
    ypos 500

transform posNinio2:
    xpos 1500
    ypos 500


##### INTERFACES DEL JUEGO #####

### MENU PRINCIPAL ###
screen menu_principal():

    tag menu

    add "images/menu_principal.png"

    add "images/game_menu_height250.png": #se usa de prueba para donde estara el titulo del juego
        xpos 200
        ypos 120

    # Contenedor de los botones.
    #vbox:
        #xalign 0.05
        #yalign 0.5
        #spacing 15

    style_prefix "menu_principal"

    imagebutton:
        idle "images/boton_menu_jugar.png"
        hover "images/boton_menu_jugar.png"
        xpos 250
        ypos 600
        action Start()

        at transform:
            xanchor 0.5
            yanchor 0.5
            subpixel True

            on hover:
                ease 0.2 zoom 1.1

            on idle:
                ease 0.2 zoom 1.0            


    imagebutton:
        idle "images/boton_menu_opciones.png"
        xpos 650
        ypos 750
        action ShowMenu("preferences")
        
        at transform:
            xanchor 0.5
            yanchor 0.5
            subpixel True

            on hover:
                ease 0.2 zoom 1.1

            on idle:
                ease 0.2 zoom 1.0    

    imagebutton:
        idle "images/boton_menu_salir.png"
        xpos 250
        ypos 900
        action Quit(confirm=True)

        at transform:
            xanchor 0.5
            yanchor 0.5
            subpixel True

            on hover:
                ease 0.2 zoom 1.1

            on idle:
                ease 0.2 zoom 1.0    


### MENU A LADO DE LOS DIALOGOS ###
screen menu_rapido():

    vbox:
        #xalign 0.0
        xpos 80
        ypos 900
        #yalign 1.0
        xoffset 80 
        yoffset -50
        spacing 20 #espacio entre los botones

        imagebutton:
            idle "images/boton_pausa.png"
            action ShowMenu('preferences')

            at transform:
                xanchor 0.5
                yanchor 0.5
                subpixel True

                on hover:
                    ease 0.2 zoom 1.1

                on idle:
                    ease 0.2 zoom 1.0    

        imagebutton:
            idle "images/boton_auto.png"
            action Preference("auto-forward", "toggle")

            at transform:
                xanchor 0.5
                yanchor 0.5
                subpixel True

                on hover:
                    ease 0.2 zoom 1.1

                on idle:
                    ease 0.2 zoom 1.0                
        
        imagebutton: 
            idle "images/boton_saltar.png"
            action Skip() alternate Skip(fast=True, confirm=True)

            at transform:
                xanchor 0.5
                yanchor 0.5
                subpixel True

                on hover:
                    ease 0.2 zoom 1.1

                on idle:
                    ease 0.2 zoom 1.0              
            


init python:
    config.overlay_screens.append("menu_rapido")
