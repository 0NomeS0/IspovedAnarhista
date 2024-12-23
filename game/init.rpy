
#Песронажи
define me = Character("[myname]", color = "#fa0000" )
define unk = Character('Неизвестный', color="#c8ffc8", image = "unk")
define vik = Character('*******', color="#0400ff", image = "vik")
define i = Character("Я", color = "#fa0000" )
define ns = Character("Настя", color = "#830083", image = "ns")
define army = Character("Военные", color = "#1e6900")
define general = Character("Генерал", color = "#41ff5b")
define mam = Character("Мама", color = "#e5ff00")

#Музыка и звуки
define audio.main_menu = "audio/music/test.mp3"
define audio.shum = "audio/music/shum.mp3"
define audio.room = "audio/music/room.mp3"
define audio.street = "audio/music/street.mp3"

define audio.click = "audio/sounds/click.ogg"
define audio.glass_break = "audio/sounds/glass_break.mp3"
define audio.soundFall = "audio/sounds/soundFall.mp3"
define audio.soundPaper = "audio/sounds/soundPaper.ogg"
define audio.soundWalk = "audio/sounds/soundWalk.ogg"
define audio.soundTea = "audio/sounds/soundTea.ogg"
define audio.soundOpenDoor = "audio/sounds/soundOpenDoor.mp3"
define audio.hihihi = "audio/sounds/hihihi.mp3"
define audio.shoot = "audio/sounds/shoot.ogg"
define audio.kickHead = "audio/sounds/kickHead.ogg"

init:
    image dust = Dust("images/dust.png")
    image screamer = "images/bg/screamer.png"
    define rt = 0


#Метка где перед главным меню показывает заставку 
label splashscreen:
    
    scene black

    pause(0.5)

    scene bg dark with fade
    # если мы напишем просто pause , то ренпи будет ожидать клика

    pause

    scene black with fade
    #Проиграть указанное видео
    $ renpy.movie_cutscene("video/main_menu.ogv")

image menu_slideshow:
    
    "gui/bg blood.jpg" with dissolve

    pause 3.0

    "gui/bg dark.jpg" with fade

    pause 2.5 

    repeat

#Тестовая анимация для Viktora(Проверка как меняются спрайты со временем)
image vik move:
    "vik normal"
    #Вариации 
    choice:
        pause 3
    choice:
        pause 5
    choice:
        pause 7
    "vik happy"
    0.25 # Делает паузу на четверть секунды
    repeat #Повторяем 
