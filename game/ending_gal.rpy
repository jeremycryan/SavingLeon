init python:
    import math
    if not persistent.endings_left:
        persistent.endings_left = [False, False, False, False, False, False]
        persistent.endings_right = [False, False, False, False, False, False]

default locks_left = [False, False, False, False, True, True]
default locks_right = [False, False, True, True, False, False]

default pics_left = ["Aden_bad_ending.png", "Aden_good_ending.png",
                "Brian_bad_ending.png", "Brian_good_ending.png",
                "Nate_bad_ending.png", "Nate_good_ending.png"]
default pics_right =["Reg_bad_ending.png", "Reg_good_ending.png",
                    "Serpens_bad_ending.png", "Serpens_good_ending.png",
                    "Leon_bad_ending.png", "Leon_good_ending.png"]

screen endings:
    tag menu
    add "empty_book.png"

    grid 2 3:
        spacing 25
        align(0.15, 0.5)
        for i in range(6):
            fixed:
                xysize(349,275)
                add "polaroid_frame.png"
                $letter = chr(ord('A') + i + int(math.floor(i/2)*2))
                if persistent.endings_left[i]:
                    button:
                        align(0.5, 0.1)
                        add pics_left[i]:
                            zoom 0.18
                        action Show("endings_close", dissolve, pics_left[i])
                text "Ending [letter]":
                    font "Candara.ttf"
                    align(0.5, 1.0)
                    color "#000"
                if locks_left[i]:
                    add "locked_X.png":
                        align(0.5, 0.5)

    grid 2 3:
        spacing 25
        align(0.9, 0.5)
        for i in range(6):
            fixed:
                xysize(349,275)
                add "polaroid_frame.png"
                $letter = chr(ord('C') + i + int(math.floor(i/2)*2))
                if persistent.endings_right[i]:
                    button:
                        align(0.5, 0.1)
                        add pics_right[i]:
                            zoom 0.18
                        action Show("endings_close", dissolve, pics_right[i])
                text "Ending [letter]":
                    font "Candara.ttf"
                    align(0.5, 1.0)
                    color "#000"
                if locks_right[i]:
                    add "locked_X.png":
                        align(0.5, 0.5)


    textbutton "Back":
        action Return()
        align(0.99, 0.99)

screen endings_close(img):
    imagebutton idle img action Hide("endings_close", dissolve)