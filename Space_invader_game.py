# space invaders
import turtle
import os
import math
import random
import winsound
#setup screen and graphics
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# creat player turtal
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# move player left and right
Playerspeed = 15 
def move_left():
 x = player.xcor()
 x -= Playerspeed
 if x < -280 :
 	x = -280
 player.setx(x)

def move_right():
 x = player.xcor()
 x += Playerspeed
 if x > 280 :
 	x = 280
 player.setx(x)
# graphics audio
def laser():
    winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
def explosion():
    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

#firw fn 
def fire():
	global bulletstate
	if bulletstate=="ready":
		laser()
		bulletstate="fire"
		x=player.xcor()
		y=player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()





#creat keyword blindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire,"space")

number_of_enemis=5
enemies=[]
for i in range(number_of_enemis):
	enemies.append(turtle.Turtle())
#creat the  enemy
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x,y)
enemyspeed = 4

# define bullet state
#bullet ready to fire 
#bullet is firing
# creat wepon
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=20
bulletstate="ready"

# if collision

def iscollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance<15:
		return True
	else:
		return False


# Game over !
finish=turtle.Turtle()
finish.hideturtle()
finish.shape("triangle")
finish.color("red")

# main game loop
while True:
	for enemy in enemies:
		
		#move enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		#move enemy down and back
		if x > 280:
			for enemy in enemies:
				y = enemy.ycor()
				y-=40
				enemy.sety(y)
			enemyspeed *= -1

		elif x < -280:
			for enemy in enemies:
				y = enemy.ycor()
				y -= 40
				enemy.sety(y)
			enemyspeed *= -1
		if enemy.ycor()< -300:
			enemy.sety(280)
	# check for collision
		if iscollision(bullet,enemy):
			explosion()
			bullet.hideturtle()
			bulletstate="ready"
			bullet.setposition(0, -400)
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x,y)
			score+=10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
			score_pen.hideturtle()


		if iscollision(enemy,player):
			player.hideturtle()
			enemy.hideturtle()
			finish.write("Game Over !",align="center", font=("Arial", 16, "normal"))
			break

	# move the bullet (fire)
	if bulletstate=="fire":
		y=bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)

	#check of bullet in the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate="ready"

















wn.mainloop()