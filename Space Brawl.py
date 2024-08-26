# Hero has to fight his way through mini bosses to win the war. Dodge bullets and survive or start over again.
from gamelib import Game, Image, Animation, randint, mouse, keys
from gamelib import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE  # Constants

game = Game(1000, 800, "Space Brawl")
logo = Image("assets/logo.png", game)
logo.y -= 200
play = Image("assets/play.png", game)
play.y -= 100
lvl1 = Image("assets/level1.png", game)
lvl1.moveTo(900, 300)
bk = Image("assets/space.jpg", game)
bk.resizeTo(game.width, game.height)
hero = Image("assets/hero.png", game)
hero.resizeBy(-50)
alien1 = Image("assets/alien1.png", game)
alien1.resizeBy(-50)
alien1.moveTo(200, 200)
alien1.rotateBy(90)
alien1.y -= 70
plasma1 = Image("assets/plasma1.png", game)
plasma1.resizeBy(-90)
plasma1.rotateBy(180)
plasma1.moveTo(400, -100)
booster = Animation("assets/booster.png", 8, game, 128, 128)
booster.rotateBy(180)
booster.resizeBy(-50)
lvl2 = Image("assets/lvl2.png", game)
hero.moveTo(700, 500)
alien_plasma = Image("assets/alien_plasma1.png", game)
alien_plasma.rotateBy(270)
alien_plasma.resizeBy(-70)
win = Image("assets/win.png", game)
lose = Image("assets/lose.png", game)
alien2 = Image("assets/alien2.png", game)
alien3 = Image("assets/alien3.png", game)
split1 = Image("assets/alien3.png", game)
split2 = Image("assets/alien3.png", game)
split1.resizeBy(-20)
split2.resizeBy(-20)
minion = []
fireball = []
for index in range(10):
    new_fireball = Image("assets/fire_ball.png", game)
    new_fireball.moveTo(randint(50, 1000), randint(-1000, -50))
    new_fireball.resizeBy(-90)
    fireball.append(new_fireball)
for index in range(18):
    new_minion = Image("assets/minion.png", game)
    new_minion.move(True)
    new_minion.moveTo(randint(50, 750), 300)
    new_minion.setSpeed(5, 360)
    new_minion.resizeBy(-75)
    new_minion.rotateBy(180)
    minion.append(new_minion)

# Start screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    play.draw()
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(60)
game.over = False

# Levelone
while not game.over:
    game.processInput()
    bk.draw()

    booster.moveTo(hero.x, hero.y+80)
    hero.draw()
    hero.move(True)

    alien1.draw()
    alien1.move(True)
    alien1.setSpeed(5)

    lvl1.draw()
    lvl1.x -= 10
    plasma1.draw()
    plasma1.y -= 7
    if hero.isOffScreen("left"):
        hero.health -= 1000
    if hero.isOffScreen("right"):
        hero.health -= 1000
    if lvl1.isOffScreen("left"):
        lvl1.visible = False

    alien_plasma.draw()
    alien_plasma.y += 8
    # alien bullet mechanics
    if alien_plasma.isOffScreen("bottom"):
        alien_plasma.moveTo(400, -400)
    if alien_plasma.isOffScreen("top"):
        alien_plasma.visible = True
        alien_plasma.moveTo(alien1.x, alien1.y+100)
    if alien_plasma.collidedWith(hero):
        alien_plasma.visible = False
        hero.health -= 15
    for index in range(18):
        minion[index].move(True)
        minion[index].setSpeed(5, 90)

    # controls
    if keys.Pressed[K_LEFT]:
        hero.x -= 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_UP]:
        hero.y -= 4
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    # Shooting mechanics
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible = True
        plasma1.moveTo(hero.x, hero.y-50)
    # health indicators
    game.drawText("Hero Health:"+str(hero.health), 5, 780)
    game.drawText("Alien Health:"+str(alien1.health), 5, 5)

    if hero.collidedWith(alien1):
        hero.health -= 100
    if alien1.health <= 0:
        game.over = True

    if plasma1.collidedWith(alien1):
        alien1.health -= 20
        plasma1.visible = False
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            minion[index].visible = False
            plasma1.visible = False
    for index in range(len(minion)):
        if minion[index].collidedWith(hero):
            minion[index].visible = False
            hero.health -= 5

    if hero.health <= 0:
        game.over = True

    game.update(60)
game.over = False

# LeveL2-------------------------------------------------------------------
hero.moveTo(700, 500)
for index in range(10):
    fireball[index].moveTo(randint(50, 1000), randint(-1000, -50))

for index in range(18):
    minion[index].moveTo(randint(50, 750), 300)
    minion[index].setSpeed(5)
lvl2.moveTo(900, 300)
alien2.setSpeed(5, 270)
alien2.moveTo(600, 100)
for index in range(18):
    minion[index].visible = True

while not game.over and hero.health > 0:
    game.processInput()
    bk.draw()
    booster.moveTo(hero.x, hero.y+80)
    hero.draw()
    alien2.draw()
    alien2.move(True)
    plasma1.draw()
    plasma1.y -= 8
    lvl2.draw()
    lvl2.x -= 10
    for index in range(18):
        minion[index].draw()
        minion[index].move(True)

    for index in range(10):
        fireball[index].draw()
        fireball[index].y += randint(3, 5)

    if plasma1.collidedWith(alien2):
        alien2.health -= 15
        plasma1.visible = False
    game.drawText("Hero Health:" + str(hero.health), 5, 780)
    game.drawText("Alien Health:" + str(alien2.health), 5, 5)
    if hero.collidedWith(alien2):
        hero.health -= 101

    for index in range(len(fireball)):
        if fireball[index].isOffScreen("bottom"):
            fireball[index].visible = True
            fireball[index].moveTo(randint(50, 1000), -50)
        if fireball[index].collidedWith(hero):
            fireball[index].visible = False
            hero.health -= 5
        if fireball[index].collidedWith(plasma1):
            plasma1.visible = False
            fireball[index].visible = False
    if keys.Pressed[K_LEFT]:
        hero.x -= 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_UP]:
        hero.y -= 4
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible = True
        plasma1.moveTo(hero.x, hero.y-50)
    if plasma1.collidedWith(alien1):
        alien1.health -= 20
        plasma1.visible = False
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            minion[index].visible = False
            plasma1.visible = False
    for index in range(len(minion)):
        if minion[index].collidedWith(hero):
            minion[index].visible = False
            hero.health -= 5

        if alien2.health < 0:
            game.over = True

    game.update(60)
game.over = False

# level 3---------------------------------------------------------------------
hero.moveTo(700, 500)
alien3.moveTo(120, 120)
for index in range(18):
    minion[index].visible = False
while not game.over and hero.health > 0:
    game.processInput()
    bk.draw()
    booster.moveTo(hero.x, hero.y+80)
    hero.draw()
    plasma1.draw()
    plasma1.y -= 8
    alien3.draw()
    split1.draw()
    split2.draw()
    for index in range(18):
        minion[index].draw()
        minion[index].move(True)
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            plasma1.visible = False
            minion[index].visible = False
    split1.visible = False
    split2.visible = False
    split1.move(True)
    split2.move(True)
    split1.setSpeed(5, 90)
    split2.setSpeed(5, 270)
    alien3.move(True)
    alien3.setSpeed(5, 90)
    if hero.collidedWith(alien3):
        hero.health -= 101
    if hero.collidedWith(split1) or hero.collidedWith(split2):
        hero.health -= 101
    game.drawText("Hero Health:"+str(hero.health), 5, 780)
    game.drawText("Alien Health:"+str(alien3.health), 5, 5)
    if alien3.health < 0:
        split1.moveTo(alien3.x-40, alien3.y)
        split2.moveTo(alien3.x+40, alien3.y)
        split1.visible = True
        split2.visible = True
        alien3.visible = False
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible = True
        plasma1.moveTo(hero.x, hero.y-50)
    if plasma1.collidedWith(alien3):
        alien3.health -= 11
        plasma1.visible = False
    if keys.Pressed[K_LEFT]:
        hero.x -= 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_UP]:
        hero.y -= 4
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if hero.health < 0:
        game.over = True
    game.update(60)
game.over = False
hero.moveTo(700, 500)
while not game.over and hero.health > 0:
    game.processInput()
    bk.draw()
    game.update(60)
game.over = False

# Win/Lose Screen
while not game.over:
    game.processInput()
    bk.draw()
    if hero.health > 0:
        win.draw()
    else:
        lose.draw()
    game.update(60)
game.quit()
