
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