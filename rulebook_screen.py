from cmu_graphics import *
from check_functions import *
from widgets import *

def rulebook_onScreenActivate(app):
    app.pointerLocation = (0, 0)
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    app.pointerColor = "red"

def rulebook_redrawAll(app):
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawRect(10, 10, 980, 630, fill='burlyWood', border='tan', borderWidth=2)
    drawRect(12, 12, 976, 626, fill='wheat')
    drawLabel(
        "Hello there general. You have been chosen to fight against the incoming alien monsters. We have tried our",
        20, 30, size=18, align='left')
    drawLabel(
        "best to hold them so far. Your job now is to place our newly designed towers to defeat the oncoming enemies!",
        20, 50, size=18, align='left')

    drawLabel(
        "You have 7 different towers that you can use. Each has a unique feature of its own!: ", 20,
        80, size=18, align='left')
    drawLabel(
        "   Patrol Tower: This tower shoots the bullet projectile at enemies in range.",
        20, 100, size=18, align='left')
    drawLabel(
        "   Laser Turret: This tower continuously tracks and beams at enemies in range.",
        20, 120, size=18, align='left')
    drawLabel(
        "   Magic Portal: This tower both damages enemies in range and teleports them back if charge-up is done.",
        20, 140, size=18, align='left')
    drawLabel(
        "   Resource Mine: This tower mines resources so we can fund the construction of all towers. If minerals",
        20, 160, size=18, align='left')
    drawLabel(
        "                              are in range, extra profit is made!",
        20, 180, size=18, align='left')
    drawLabel(
        "   Submarine: Submarines tour the waters and fire at enemies in range.",
        20, 200, size=18, align='left')
    drawLabel(
        "   Tooth Trap: This trap harms enemies that come in contact with it.",
        20, 220, size=18, align='left')
    drawLabel(
        "   Monster Net: This net slows enemies for a short time that come in contact with it.",
        20, 240, size=18, align='left')

    drawLabel(
        "There are 4 unique map assets that may appear while you play: ", 20,
        270, size=18, align='left')
    drawLabel(
        "   Minerals: This asset has a mineral icon and placing mines in range will increase profits!",
        20, 290, size=18, align='left')
    drawLabel(
        "   Acid_74: Watch out! This leaked lab experiment heals monsters as they come in range!",
        20, 310, size=18, align='left')
    drawLabel(
        "   Tornado: Mother nature is fighting with us! Tornadoes hurt the monsters as they come in range!",
        20, 330, size=18, align='left')
    drawLabel(
        "   Fog: We can't see the monsters when they go into the fog!",
        20, 350, size=18, align='left')

    drawLabel(
        "To play the game, click on the Start Game! button on the title screen and choose a level! You can choose", 20,
        380, size=18, align='left')
    drawLabel(
        "from generated levels with easy, medium, or hard level of difficulty, or play your own custom maps! When", 20,
        410, size=18, align='left')
    drawLabel(
        "the game loads, press start round and start placing towers! If you lose all of your hearts, the game ends.", 20,
        430, size=18, align='left')
    drawLabel(
        "Remember, towers can be upgraded by pressing on them once they have been constructed in the playable area.",
        20,
        450, size=18, align='left')

    drawLabel(
        "To create your own maps, click on the Map Editor button on the title screen. Here you can draw the enemy path", 20,
        480, size=18, align='left')
    drawLabel(
        "by clicking in the playable box (blue area). You can also add assets by simply clicking on them and placing.", 20,
        500, size=18, align='left')
    drawLabel(
        "You can toggle to edit different maps as well! Just choose which one you would like to edit!", 20,
        520, size=18, align='left')

    drawLabel(
        "Now, its time to stop those monsters. Good luck general!", 20,
        570, size=18, align='left')

    app.backButton.draw()
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def rulebook_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.backButton.containsPoint(mouseX, mouseY):
        setActiveScreen('title')

def ruolebook_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = "red"
    app.pointerLocation = (mouseX, mouseY)

