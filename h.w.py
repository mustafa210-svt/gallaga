import pgzrun
import random

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Score
score = 0

# Ship
ship = Actor("ship")
ship.pos = WIDTH / 2, HEIGHT - 50

# Bug settings
num_bugs = 5
bug_width = 80
bug_height = 60
bug_row_y = 50
bug_spacing = WIDTH / (num_bugs + 1)  # Slightly increase spacing to make bugs closer

# Create a list of bugs and position them in a row
bugs = [Actor("bug") for _ in range(num_bugs)]
for i, bug in enumerate(bugs):
    bug.x = i * bug_spacing + bug_spacing / 2
    bug.y = bug_row_y

# Bullet list
bullets = []

# Draw function
def draw():
    screen.blit("space", (0, 0))
    for bug in bugs:
        bug.draw()
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text(f"Score: {score}", (5, 10), fontsize=55, color="white")

# Key press handler
def on_key_down(key):
    if key == keys.SPACE:
        if len(bullets) < 3:
            bullet = Actor("bullet")
            bullet.pos = ship.x, ship.y - 20  # Position the bullet slightly above the ship
            bullets.append(bullet)

# Update function
def update():
    global score

    # Move the bugs down more slowly
    for bug in bugs:
        bug.y += 1  # Slower falling speed
        if bug.y > HEIGHT:
            bug.y = bug_row_y
            bug.x = random.randint(bug_width // 2, WIDTH - bug_width // 2)

    # Move the ship
    if keyboard.left:
        ship.x -= 5
        if ship.x < 0:
            ship.x = 0
    if keyboard.right:
        ship.x += 5
        if ship.x > WIDTH:
            ship.x = WIDTH

    # Update bullet positions
    for bullet in bullets[:]:
        bullet.y -= 5
        for bug in bugs:
            if bullet.colliderect(bug):
                score += 1
                bug.y = bug_row_y
                bug.x = random.randint(bug_width // 2, WIDTH - bug_width // 2)
                bullets.remove(bullet)
                break  # Exit loop once we have handled the collision
        else:
            # Remove bullet if it goes off-screen
            if bullet.y < 0:
                bullets.remove(bullet)

pgzrun.go()

 