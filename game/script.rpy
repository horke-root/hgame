# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.





### Background ###

image bg fupper:
    "bg/fupper.png"
    size (1280, 720)

# Игра начинается здесь:
label start:

    scene bg fupper
    cutscene "fap...fap..fap"
    show bg fupper with dissolve:
        xpos 0.3 ypos 1.0 xanchor 0.3 yanchor 0.60 zoom 2.0
        linear 12 yanchor 0.59
    cutscene "fap...fap..fap"
    jump inroom
    return

