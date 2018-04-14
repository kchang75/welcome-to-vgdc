# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character(_('Tuffy'), color="#000080")
define p = Character(_('Pegu'), color="#00c0ff")

default lab = False
default social = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg titanwalk #titan walk big TITAN sign
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tuffy bye
    with dissolve

    # These display lines of dialogue.

    t "Hi! I'm Tuffy and I'm here to welcome you to the Video Game Development Club!"

    show tuffy 
    
    t "I'm super ready to tell you about all the stuff we do in the VGDC!"

    t "First of all, the Video Game Development club (if you can't tell by the name) is a club about making games!"

    t "We like video games so much that we want to do it for a living."

    t "The point of the VGDC is to make games together in order to learn useful skills for the future."

    t "At the moment, the VGDC is working on a game called the Penguin Delivery Service."

    show tuffy at left
    with move

    show pegu at right
    with dissolve

    p "My name is Pegu and I'm the star of PDS!"

    p "I deliver the mail to people on my shiny Pegway™!"

    t "We don't want to be sued by S*gway."

    p "You can learn more about PDS by talking to an officer!"

    t "Our goal is to finish this game by the end of the semester, so we can start new projects in Fall!"

    hide pegu
    with dissolve

    t "So time for questions!"


    jump choices
    
label choices:
    
    if lab and social:
        jump end

    menu:

        t "So, what would you like to know more about?"

        "Game labs" if not lab:
            jump gamelabs

        "Socials" if not social:
            jump socials

        "Nothing else":
            jump end

label socials:

    $ social = True

    t "Ah, I see you like to have fun!"

    t "Anyways, the VGDC holds several social events during the school year..."

    scene bg party
    with fade

    t "where we play games and have fun!"

    show tuffy at left
    with dissolve

    t "Occasionally, we'll have parties in the Titan Student Union, where there's lots provided for us!"

    t "Members can also bring their own games with them if they so wish."

    t "Current games in our library include the Jackbox Party Pack, Mario Kart 8, Pokken, Cards Against Humanity ... and more!"

    t "So we don't just make games, but we play them as well!"

    jump choices

label gamelabs:
    
    $ lab = True

    t "Ah, I see you want to work on games!"

    scene bg gamelab
    with fade

    t "Game labs are weekly meetings where our club gets together in a lab in the Computer Science Department."

    show tuffy at left
    with dissolve

    t "Everyone uses this time to work on the game and communicate with other members."

    t "The great thing about game labs is if you run into a problem, there's people that can help!"

    t "Making games is more fun when it's a collaborative effort!"

    jump choices

label haloween:

    t "Like Haloween!"

    t "No, that's not a typo!"

    t "Halo-ween is our Halloween event, where members can play games and eat candy to their hearts' delight!"

    t "Usually held the week of Halloween, Halo-ween is a day, filled with movies, games, and candy!"

    jump choices

label escaperoom:
label blizzardtour:
label gamejams:
label workshops:
label collaborations:

label end:

    scene bg titanwalk
    show tuffy
    with fade

    t "Well that's all I have to say for now!"

    t "Thanks for stopping by!"

    show tuffy bye

    t "Have a nice day!"

    # This ends the game

    return
