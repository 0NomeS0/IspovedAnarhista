label chap1:
    #$ renpy.pause(5)
    #Включить 3д сцену

    #camera:
    #    perspective True

    play music "music/shum.mp3" fadein 0.5
    scene bg dark with Dissolve(5.0)
    show dust with Dissolve(5.0)
    $ renpy.pause(4.0)
    "{k=5.5}Раз два три четыре пять, я иду тебя искать{/k}"
    "Deep adadas fd fg {space=510} Текст когда space."
    '''
        Я открыл свои глаза и ничего не увидел. 
        {w}Совсем ничего. 
        {w}Меня окружала Белая пустота. 
    '''
    i "Хм... и куда это меня занесло? {w}Здесь есть кто-нибудь?"
    unk "Ага..."

    "Сказал до боли знакомый голос."
    "Я обернулся и увидел себя"
    play sound soundFall
    window hide
    show unk normal at moverUpDown#zoomin #with Dissolve(3.0)
    extend ", только более молодого."

    "Наклонив голову, я убедился что перед мной не зеркало , ибо мой двойник даже не думал повторять мои движения."
    i "Где я?"
    play sound hihihi
    unk @happy "Хах, это и есть твой первый вопрос? {w}То есть, себе."
    
    i '''
    Что за хрень ты несешь?!

    ГДЕ Я?!

    КУДА Я ПОПАЛ?!

    Ты Т-ты просто очень похож на меня {w=5},но ты не можешь являться мной!

    Э-этого просто не может быть.

    Ведь если Я убью тебя то произойдет временной парадокс!
    '''

    unk sad "Во первых успокойся." 
    unk normal "Во вторых перестань тараторить." 
    play sound hihihi
    unk happy "Черт....Ты совершенно ничего не помнишь что с тобой произошло?!"
    if(persistent.test > 2):
        play sound hihihi
        unk happy "АХАХАХАХАХ, ТЫ ТАК МНОГО РАЗ УМЕР, КАКОЙ ТЫ ЖАЛКИЙ"
    else:
        unk happy "Пока что ты умер [persistent.test] раз"
    

    i "Ты о чём?"
    unk sad "Fine. Скажи кто я, тьфу блен, то есть , ты"
    $ myname = renpy.input("Моё имя...",length  = 10 , allow="ячсмитьбюфывапролджэйцукенгшщзхъ-ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЪ") 
    show dust with Dissolve(5.0)
    me "Меня зовут [myname], живу в стране Z и восточном районе Центорий"
    scene black with fade 
    stop music
    jump chap2
    
    return