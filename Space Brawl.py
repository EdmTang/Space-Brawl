#Nitro Fissure
#Santiago,Edmond,Michael
#Space Brawl
#Hero has to fight his way through mini bosses to win the war. Dodge bullets and survive or start over again.
from gamelib import*

game=Game(1000,800,"Space Brawl")
logo=Image("logo.png",game)
logo.y-=200
play=Image("play.png",game)
play.y-=100
lvl1=Image("level1.png",game)
bk=Image("space.jpg",game)
bk.resizeTo(game.width,game.height)
hero=Image("hero.png",game)
hero.resizeBy(-50)
alien1=Image("alien1.png",game)
alien1.resizeBy(-50)
alien1.moveTo(200,200)
alien1.rotateBy(90)
alien1.y-=70
plasma1=Image("plasma1.png",game)
plasma1.resizeBy(-90)
plasma1.rotateBy(180)
booster=Animation("booster.png",8,game,1024/8,1024/8)
booster.rotateBy(180)
booster.resizeBy(-50)
lvl2=Image("lvl2.png",game)
hero.moveTo(700,500)
alien_plasma=Image("alien_plasma1.png",game)
win=Image("win.png",game)
lose=Image("lose.png",game)
alien2=Image("alien2.png",game)
alien3=Image("alien3.png",game)
split1=Image("alien3.png",game)
split2=Image("alien3.png",game)
split1.resizeBy(-20)
split2.resizeBy(-20)
minion=[]
fireball=[]
for index in range(10):
    fireball.append(Image("fire_ball.png",game))
for index in range(10):
    
    s=randint(50,1000)
    c=randint(50,1000)
    fireball[index].moveTo(c,0-s)
    fireball[index].resizeBy(-90)
for index in range(18):
    minion.append(Image("minion.png",game))
for index in range(18):
    minion[index].move(True)
    w=randint(50,750)
    minion[index].moveTo(w,300)
    minion[index].setSpeed(5,360)
    minion[index].resizeBy(-75)
    minion[index].rotateBy(180)
lvl1.moveTo(900,300)
plasma1.moveTo(400,0-100)
alien_plasma.rotateBy(270)
alien_plasma.resizeBy(-70)
#Start screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    play.draw()
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over=True
    game.update(60)
game.over=False
#Levelone

while not game.over:
    game.processInput()
    bk.draw()
    
    
        
    booster.moveTo(hero.x,hero.y+80)
    hero.draw()
    hero.move(True)
    
    alien1.draw()
    alien1.move(True)
    alien1.setSpeed(5)
    
    
    lvl1.draw()
    lvl1.x-=10
    plasma1.draw()
    plasma1.y-=7
    if hero.isOffScreen("left"):
        hero.health-=1000
    if hero.isOffScreen("right"):
        hero.health-=1000
    if lvl1.isOffScreen("left"):
        lvl1.visible=False
    
    alien_plasma.draw()
    alien_plasma.y+=8
    #alien bullet mechanics
    if alien_plasma.isOffScreen("bottom"):
        alien_plasma.moveTo(400,0-400)
    if alien_plasma.isOffScreen("top"):
        alien_plasma.visible=True
        alien_plasma.moveTo(alien1.x,alien1.y+100)
    if alien_plasma.collidedWith(hero):
        alien_plasma.visible=False
        hero.health-=15
    for index in range(18):
        minion[index].move(True)
        minion[index].setSpeed(5,90)
   
    #controls
    if keys.Pressed[K_LEFT]:
        hero.x-=4
    if keys.Pressed[K_RIGHT]:
        hero.x+=4
    if keys.Pressed[K_UP]:
        hero.y-=4
    if keys.Pressed[K_DOWN]:
        hero.y+=4
    #Shooting mechanics
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible=True
        plasma1.moveTo(hero.x,hero.y-50)
    #health indicators
    game.drawText("Hero Health:"+str(hero.health),5,780)
    game.drawText("Alien Health:"+str(alien1.health),5,5)
    
    if hero.collidedWith(alien1):
        hero.health-=100
    if alien1.health<=0:
        game.over=True
    
        
    if plasma1.collidedWith(alien1):
        alien1.health-=20
        plasma1.visible=False
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            minion[index].visible=False
            plasma1.visible=False
    for index in range(len(minion)):
        if minion[index].collidedWith(hero):
            minion[index].visible=False
            hero.health-=5
            
    if hero.health<=0:
        game.over=True
    
    
    game.update(60)
game.over=False
#LeveL2-------------------------------------------------------------------
hero.moveTo(700,500)
for index in range(10):
    s=randint(50,1000)
    c=randint(50,1000)
    fireball[index].moveTo(c,0-s)
   

for index in range(18):
    
    w=randint(50,750)
    minion[index].moveTo(w,300)    
    minion[index].setSpeed(5)
lvl2.moveTo(900,300)
alien2.setSpeed(5,270)
alien2.moveTo(600,100)
for index in range(18):
    minion[index].visible=True

while not game.over and hero.health>0:
    game.processInput()
    bk.draw()
    booster.moveTo(hero.x,hero.y+80)
    hero.draw()
    alien2.draw()
    alien2.move(True)
    plasma1.draw()
    plasma1.y-=8
    lvl2.draw()
    lvl2.x-=10
    for index in range(18):
        minion[index].draw()
        minion[index].move(True)
    
    for index in range(10):
        fireball[index].draw()
        z=randint(3,5)
        fireball[index].y+=z
    
    if plasma1.collidedWith(alien2):
        alien2.health-=15
        plasma1.visible=False
    game.drawText("Hero Health:"+str(hero.health),5,780)
    game.drawText("Alien Health:"+str(alien2.health),5,5)
    if hero.collidedWith(alien2):
        hero.health-=101
    
    for index in range(len(fireball)):
        if fireball[index].isOffScreen("bottom"):
            fireball[index].visible=True
            g=randint(50,1000)
            h=50
            fireball[index].moveTo(g,0-h)
        if fireball[index].collidedWith(hero):
            fireball[index].visible=False
            hero.health-=5
        if fireball[index].collidedWith(plasma1):
            plasma1.visible=False
            fireball[index].visible=False
    if keys.Pressed[K_LEFT]:
        hero.x-=4
    if keys.Pressed[K_RIGHT]:
        hero.x+=4
    if keys.Pressed[K_UP]:
        hero.y-=4
    if keys.Pressed[K_DOWN]:
        hero.y+=4
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible=True
        plasma1.moveTo(hero.x,hero.y-50)
    if plasma1.collidedWith(alien1):
        alien1.health-=20
        plasma1.visible=False
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            minion[index].visible=False
            plasma1.visible=False
    for index in range(len(minion)):
        if minion[index].collidedWith(hero):
            minion[index].visible=False
            hero.health-=5
    
        if alien2.health<0:
            game.over=True
    
    game.update(60)
game.over=False
#level 3------------------------------------------------------------------------
hero.moveTo(700,500)
alien3.moveTo(120,120)
for index in range(18):
    minion[index].visible=False
while not game.over and hero.health>0:
    game.processInput()
    bk.draw()
    booster.moveTo(hero.x,hero.y+80)
    hero.draw()
    plasma1.draw()
    plasma1.y-=8
    alien3.draw()
    split1.draw()                                                            
    split2.draw()
    for index in range(18):
        minion[index].draw()
        minion[index].move(True)
    for index in range(len(minion)):
        if minion[index].collidedWith(plasma1):
            plasma1.visible=False
            minion[index].visible=False
    split1.visible=False
    split2.visible=False
    split1.move(True)
    split2.move(True)
    split1.setSpeed(5,90)
    split2.setSpeed(5,270)
    alien3.move(True)
    alien3.setSpeed(5,90)
    if hero.collidedWith(alien3):
        hero.health-=101
    if hero.collidedWith(split1) or hero.collidedWith(split2):
        hero.health-=101
    game.drawText("Hero Health:"+str(hero.health),5,780)
    game.drawText("Alien Health:"+str(alien3.health),5,5)
    if alien3.health<0:
        split1.moveTo(alien3.x-40,alien3.y)
        split2.moveTo(alien3.x+40,alien3.y)
        split1.visible=True
        split2.visible=True
        alien3.visible=False
    if plasma1.isOffScreen("top") and keys.Pressed[K_SPACE]:
        plasma1.visible=True
        plasma1.moveTo(hero.x,hero.y-50)
    if plasma1.collidedWith(alien3):
        alien3.health-=11
        plasma1.visible=False
    if keys.Pressed[K_LEFT]:
        hero.x-=4
    if keys.Pressed[K_RIGHT]:
        hero.x+=4
    if keys.Pressed[K_UP]:
        hero.y-=4
    if keys.Pressed[K_DOWN]:
        hero.y+=4
    if hero.health<0:
        game.over=True
    

    game.update(60)
game.over=False
hero.moveTo(700,500)
while not game.over and hero.health>0:
    game.processInput()
    bk.draw()
    
    game.update(60)
game.over=False
#Win Screen
while not game.over and hero.health>0:
    game.processInput()
    bk.draw()
    win.draw()
    game.update(60)
game.quit()
#Lose Screen
while not game.over and hero.health<0:
    game.processInput()
    bk.draw()
    lose.draw()
    game.update(60)
game.quit()

