import pgzrun
import random
#screen
WIDTH = 800
HEIGHT = 800
#score
score = 0
#actors
ship = Actor("ship")
bug = Actor("bug")
ship.pos = 400,700
bug.pos = 400,80
#bullet list
bullets = []
#draw
def draw():
  screen.blit("space",(0,0))
  bug.draw()
  ship.draw()
  for bullet in bullets:
    bullet.draw()
  screen.draw.text(str(score),(5,10), fontsize = 55)


def on_key_down(key):
  if key == keys.SPACE:
    if len(bullets) < 3: 
      bullet = Actor("bullet")
      bullet.pos = ship.pos
      bullets.append(bullet)
    
#update function
def update():
  global score
  bug.y = bug.y + 3
  if bug.y > 750:
    bug.y = 0
    bug.x = random.randint(20,720)
  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5
 
    

  for bullet in bullets:
    if bullet.colliderect(bug):
      bug.y = 0
      bug.x = random.randint(20,720)
      bullets.remove(bullet)
      score = score + 1
    if bullet.y < 0:
      bullets.remove(bullet)
    else:
      bullet.y = bullet.y - 5
  
    
 

  
pgzrun.go()