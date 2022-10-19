
# Habeba Morsy 
# Leena Alsaadi 


# This game is inspired by the classic PacMan game called Hoo-Box. It is designed so that the pac-man character
# must go through the maze while avoiding the colored boxes that are the "enemies" . These "enemies"  act as ghosts
# and float around the surface area, not following the maze. The "enemies"  bounce off the
# four walls of our game randomly moving around. The player has to try and collect as many small white boxes as they can
# in 60 seconds while avoiding the evil big boxes. The player has three lives and each time you come into contact with
# a box, you will lose a life. The player has to collect all the small boxes to win!
# Be careful and good luck :D

# Required Features

# User Input
  #  - UP - DOWN - RIGHT - LEFT, movement key for character
  # SPACE, pause game

# Game Over
    # Game is over when character gets hit by ghost(s) 3 times; show 'game over' screen

# Small Enough Window
    # game window -> 600 width, 600 height

# Graphics/Images
    # construct maze
	# pac man character

# Optional Features

# Enemies (colored boxes)
    # ghosts are harmful, move around in the maze
    # ghosts decrease one of three lives if you recruit(touch) them

# Restart from Game Over # we removed this feature and replaced it with sprite animantion
    # when the three lives are used up and Game Over screen pops up, hit button (r) to
    # restart game (don't re-run whole program)

# Sprite Animation
	# main character (pac-man) open, closes, rotates, and flips [1-5]

# Collectibles (small white boxes)
    # collectibles that appear on a counter on the screen

# Health bar (3 lives)
    # life decreases by one when character is in contact with ghost(s).
	# When health bar reaches 0 (after ghost touches 3 times), game is over.

# Extra(s)

# Timer
#   - 1 minute timer rounds for player to collect all collectables without getting in contact.


import pygame
import gamebox
import random

pygame.init()

height = 5
width = 150
vertical_height = 200
vertical_width = 5

camera = gamebox.Camera(800, 600) #game window

# sprite animation (opitonal feature)
player_sprite = gamebox.load_sprite_sheet("pacman_character.png", 1, 5)
player = gamebox.from_image(400, 250, player_sprite[1])
player.scale_by(.25) #resizes


frame = 0 #from lecture
start_game = False #to start run the game
time = 0
score = 0
num_lives = 3
first_ghost_postion = True #checks to see if code has ran once, so the ghosts can have set initial speed



def getrandx():
	'''
		Generates random x coordiante everytime you call.

	:return: Returns random integer for x in between 100 t0 800.
	'''
	return random.randint(100, 800)

def getrandy():
	'''
	Generates random y coordiante everytime you call.
	:return: Returns random integer for y in between 100 t0 490.
	'''
	return random.randint(100, 490)

dots_w = 10 #witdth
dots_h = 12 #hieght

# optional feature and image - collectables
collectables = [gamebox.from_color(225, 420, "white", dots_w, dots_h),
				gamebox.from_color(430, 120, "white", dots_w,dots_h),
				gamebox.from_color(100, 280, "white", dots_w,dots_h),
				gamebox.from_color(320, 275, "white", dots_w,dots_h),
				gamebox.from_color(340, 70, "white", dots_w,dots_h),
				gamebox.from_color(660, 430, "white", dots_w,dots_h),
				gamebox.from_color(460, 375, "white", dots_w,dots_h),
				gamebox.from_color(750, 50, "white", dots_w,dots_h),
				gamebox.from_color(775, 470, "white", dots_w,dots_h),
				gamebox.from_color(630, 325, "white", dots_w,dots_h),
				gamebox.from_color(50, 125, "white", dots_w,dots_h),
				gamebox.from_color(560, 310, "white", dots_w,dots_h),
				gamebox.from_color(75, 480, "white", dots_w,dots_h),
				gamebox.from_color(520, 410 , "white", dots_w,dots_h),
				gamebox.from_color(780, 220, "white", dots_w, dots_h),
				gamebox.from_color(30, 50, "white", dots_w, dots_h),
				gamebox.from_color(320, 460, "white", dots_w, dots_h),
				gamebox.from_color(215, 215, "white", dots_w, dots_h)
				]

wall_color = " dark orange"


# graphics
walls = [ 	gamebox.from_color(300,300, wall_color, width , height),
			gamebox.from_color(500, 300, wall_color, width, height),
		  	gamebox.from_color(300,200, wall_color, vertical_width , vertical_height),
		   	gamebox.from_color(500, 200, wall_color, vertical_width, vertical_height),
			gamebox.from_color(300,200, wall_color, width , height),
			gamebox.from_color(500, 200, wall_color, width, height),
			gamebox.from_color(300,200, wall_color, width , height),
	  		gamebox.from_color(400,300, wall_color, 200 , height),
		   	gamebox.from_color(0, 0, wall_color, 5, 1000 ),
		  	gamebox.from_color(800, 0, wall_color, 1600, 5),
			gamebox.from_color(800, 0, wall_color, 5, 1000),
			gamebox.from_color(0, 500, wall_color, 1600, 5),
			gamebox.from_color(50,100, wall_color, width , height),
			gamebox.from_color(200, 450, wall_color, width, height),
			gamebox.from_color(300, 500, wall_color, width, height),
		  	gamebox.from_color(550, 430, wall_color, vertical_width , 140),
		   	gamebox.from_color(440, 400, wall_color, vertical_width, 100),
			gamebox.from_color(670, 100, wall_color, width, height),
		  	gamebox.from_color(650, 200, wall_color, vertical_width , vertical_height/2),
			gamebox.from_color(150, 500, wall_color, width, height),
			gamebox.from_color(150, 450, wall_color, vertical_width, vertical_height/2),
			gamebox.from_color(300, 500, wall_color, width, height),
			gamebox.from_color(175, 50, wall_color, vertical_width, vertical_height/2),
			gamebox.from_color(650, 50, wall_color, vertical_width, vertical_height),
			gamebox.from_color(600, 100, wall_color, width/2, height),
		  	gamebox.from_color(75, 270, wall_color, vertical_width , vertical_height),
			gamebox.from_color(90, 240, wall_color, 200, height),
			gamebox.from_color(400, 50, wall_color, width/2, height),
		  	gamebox.from_color(400, 50, wall_color, vertical_width , vertical_height/2),
			gamebox.from_color(680, 450, wall_color, width, height),
		  	gamebox.from_color(700, 450, wall_color, vertical_width , vertical_height/2),
			gamebox.from_color(200, 350, wall_color, width, height),
		  	gamebox.from_color(200, 350, wall_color, vertical_width , vertical_height/2),
			gamebox.from_color(750, 350, wall_color, width, height),
		  	gamebox.from_color(500, 150, wall_color, vertical_width , vertical_height/2)
		   ]

# optional feature - enemies
ghosts = [gamebox.from_color(getrandx(), getrandy(), "brown", 23, 23),
		  gamebox.from_color(getrandx(), getrandy(), "green", 23,23),
		  gamebox.from_color(getrandx(), getrandy(), "black", 23, 23),
		  gamebox.from_color(getrandx(), getrandy(), "purple", 23, 23),
		  gamebox.from_color(getrandx(), getrandy(), "sky blue", 23, 23)]


def changedir(posistion, dir=""):
	"""
	Changes the direction of ghost boxes to randomly move.
	:param posistion: Which ghost we are using (position in list).
	:param dir: The direction we need to exclude because it was already moving in that direction.
	:return: None (just changes direction of ghost boxes)
	"""
	exclude = 0 #direction of ghost to exclude so it prevents the random genrator from randomly going that same direction
	if dir == "UP":
		exclude = 3
	elif dir == "DOWN":
		exclude = 4
	elif dir == "RIGHT":
		exclude = 1
	elif dir == "LEFT":
		exclude = 2
	ghost = ghosts[posistion]

	new_dir = exclude
	while (new_dir == exclude):
		new_dir = random.randint(1, 6)

	my_speed = 7
	if new_dir == 1:
		ghost.speedx = my_speed
		ghost.speedy = 0
	if new_dir == 2:
		ghost.speedx = my_speed * -1
		ghost.speedy = 0
	if new_dir == 3:
		ghost.speedx = 0
		ghost.speedy = my_speed
	if new_dir == 4:
		ghost.speedx = 0
		ghost.speedy = my_speed * -1

	if new_dir == 5: #allows to go diagonole
		ghost.speedx = my_speed/2
		ghost.speedy = my_speed/2
	if new_dir == 6: #allows to go diagonole
		ghost.speedx = -1*my_speed/2
		ghost.speedy = -1*my_speed/2


def game (keys):
	'''
	Function used for the cover of the game (start page).
	:param keys: Presses the space bar to start the game.
	:return: None (used for tick funciton so we can display start page and press space bar (keys) to start the game.)
	'''

	global start_game
	camera.clear('grey')
	camera.draw("Habeba Morsy (dep4bx)", 25, " dark orange", 400, 450)
	camera.draw("Leena Alsaadi (la5sz)", 25, "navy blue", 400, 500)
	camera.draw("Press SPACE to Start", 30, "white", 400, 550)
	game_title_ptone = gamebox.from_text(300, 100, "HOOO-", 150, "Dark orange")
	game_title_pttwo = gamebox.from_text(580, 100, "BOX", 150, "navy blue", italic=False)
	game_description = gamebox.from_text(400, 225, "How to play:", 40, "dark orange")
	game_descriptionpttwo = gamebox.from_text(400, 275, "Collect as many small boxes as you can in under 60 seconds", 25, "navy blue")
	game_descriptionptthree = gamebox.from_text(400, 300, "while avoiding the evil, big boxes. You have 3 lives. Each", 25, "navy blue")
	game_descriptionptfour = gamebox.from_text(400, 325, "time you come into contact with a box, you will lose a life.", 25, "navy blue")
	game_descriptionptfive = gamebox.from_text(400, 350, "Collect all the small boxes to win!", 25, "navy blue")
	game_descriptionptsix = gamebox.from_text(400, 375, "Be careful and good luck :D", 25, "navy blue")


	camera.draw(game_description)
	camera.draw(game_descriptionpttwo)
	camera.draw(game_descriptionptthree)
	camera.draw(game_descriptionptfour)
	camera.draw(game_descriptionptfive)
	camera.draw(game_descriptionptsix)
	camera.draw(game_title_ptone)
	camera.draw(game_title_pttwo)
	if pygame.K_SPACE in keys:
		start_game = True #start the game

#for the sprite character
right_pos = True
left_pos = False
up_pos = False
down_pos = False

def tick(keys):
	'''
	Main function for game to run. Takes in user input and allows keys (up, down, right, left) to move player and
	navigate through the maze. Changes direction based on what user presses.
	Allows ghosts to randomly move all around the maze.
	Displays the game and all of its components.
	:param keys: Up, down, left, right keys to move the player in those directions.
	:return: None (used to run game)
	'''

	global first_ghost_postion
	global start_game
	global time
	global score
	global num_lives
	global frame
	global player
	global player_sprite
	global right_pos, left_pos, up_pos, down_pos

	camera.clear("navy blue")
	game(keys)
	if start_game: #if true, game runs
		camera.clear("navy blue")
		camera.draw(player)
		camera.draw(gamebox.from_text(400, 550, "TIME: " + str(int(time)), 20, "white"))
		camera.draw(gamebox.from_text(600, 550, "SCORE: " + str(int(score)), 20, "white"))
		life_display = 'LIVES: ' + str(int(num_lives))
		camera.draw(life_display, 20, "white", 180, 550)

		for wall in walls:
			camera.draw(wall)
			if player.touches(wall):
				player.move_to_stop_overlapping(wall)

		for dots in collectables:
			camera.draw(dots)
			if player.touches(dots):
				score += 1 #score count
				dots.y = 900
				if score == 18:
					camera.clear("navy blue")
					camera.draw(gamebox.from_text(400, 300, "HEHE :) YOU WON!!", 70, "yellow"))
					camera.draw(gamebox.from_text(400, 550, "TIME: " + str(int(time)), 20, "white"))
					camera.draw(gamebox.from_text(600, 550, "SCORE: " + str(int(score)), 20, "white")) #displays score
					camera.draw(life_display, 20, "white", 180, 550)
					gamebox.pause() #winning the game

			for ghost in ghosts:
				if player.touches(ghost):
					ghost.y = getrandy()
					num_lives -= 1 #life counter #optional feature - health bar (lives)
					life_display = 'LIVES: ' + str(int(num_lives))
					camera.draw(life_display, 20, "white", 180, 550) #displays lives
					if num_lives == 0:
						camera.clear("navy blue")
						camera.draw(gamebox.from_text(400, 300, "GAME OVER", 60, "red"))
						camera.draw(gamebox.from_text(400, 200, " OOPS :O YOU HAVE BEEN KILLED", 60, "red"))
						camera.draw(gamebox.from_text(400, 550, "TIME: " + str(int(time)), 20, "white"))
						camera.draw(gamebox.from_text(600, 550, "SCORE: " + str(int(score)), 20, "white"))
						camera.draw(life_display, 20, "white", 180, 550)
						gamebox.pause() #game over

		time += 1 / 30 #time tracker
		if time > 60:
			camera.clear("navy blue")
			camera.draw(gamebox.from_text(400, 200, "TOO SLOW... TIME IS UP!", 60, "red"))
			camera.draw(gamebox.from_text(400, 300, "GAME OVER :(", 60, "red"))
			camera.draw(gamebox.from_text(400, 550, "TIME: " + str(int(time)), 20, "white"))
			camera.draw(gamebox.from_text(600, 550, "SCORE: " + str(int(score)), 20, "white"))
			camera.draw(life_display, 20, "white", 180, 550)
			gamebox.pause() #game over

		if first_ghost_postion: #runs only first time
			first_ghost_postion = False  #proof that it runs once, stops it from running again
			for ghost in range(0,len(ghosts)): #access each index in the aray to loop through each ghosts
				changedir(ghost)
				ghosts[ghost].move_speed()

		# checks to make sure the ghosts are not out of our game screen.
		# if ghost boxes are close to a corner, it randomly changes direction of boxes to move around.
		for position in range(0,len(ghosts)):
			ghost = ghosts[position]

			camera.draw(ghost)
			if ghost.x < 50:
				changedir(position,"LEFT")
				ghost.move_speed()

			elif ghost.x > 750:
				changedir(position,"RIGHT")
				ghost.move_speed()

			elif ghost.y < 50:
				changedir(position,"DOWN")
				ghost.move_speed()

			elif ghost.y > 450:
				changedir(position,"UP")
				ghost.move_speed()

			ghost.move_speed()


		player_move = False
		if player.x > 800:
			player.x = 0
		if player.x < 0:
			player.x = 800
		if player.y > 500:
			player.y = 0
		if player.y <0:
			player.y = 500

		#for sprite animantion movement
		if pygame.K_RIGHT in keys:
			if right_pos == False:
				if up_pos == True:
					player.rotate(270) # moves in counter clockwise
					right_pos = True
					up_pos = False
					down_pos = False
					left_pos = False

				if down_pos == True:
					player.rotate(90)
					right_pos = True
					up_pos = False
					down_pos = False
					left_pos = False

				if left_pos == True:
					player.flip()
					right_pos = True
					up_pos = False
					down_pos = False
					left_pos = False

			player.x += 5
			player_move = True
		if pygame.K_LEFT in keys:
			if right_pos == True:
				player.flip()
				right_pos = False
				up_pos = False
				down_pos = False
				left_pos = True

			if up_pos == True:
				player.rotate(90)
				right_pos = False
				up_pos = False
				down_pos = False
				left_pos = True

			if down_pos == True:
				player.rotate(270)
				right_pos = False
				up_pos = False
				down_pos = False
				left_pos = True

			player.x += -5
			player_move = True

		if pygame.K_UP in keys:
			if right_pos == True:
				player.rotate(90)
				right_pos = False
				up_pos = True
				down_pos = False
				left_pos = False

			if left_pos == True:
				player.rotate(270)
				right_pos = False
				up_pos = True
				down_pos = False
				left_pos = False

			if down_pos == True:
				player.rotate(180)
				right_pos = False
				up_pos = True
				down_pos = False
				left_pos = False

			player.y -= 5
			player_move = True

		if pygame.K_DOWN in keys:
			if right_pos == True:
				player.rotate(270)
				right_pos = False
				up_pos = False
				down_pos = True
				left_pos = False

			if up_pos == True:
				player.rotate(180)
				right_pos = False
				up_pos = False
				down_pos = True
				left_pos = False

			if left_pos == True:
				player.rotate(90)
				right_pos = False
				up_pos = False
				down_pos = True
				left_pos = False
			player.y += 5
			player_move = True

		# got from gamebox lecture
		if player_move:
			frame += 0.3
			if frame >= 4:
				frame = 0
			player.image = player_sprite[int(frame)]
		else:
			player.image = player_sprite[-1]


	camera.display()


gamebox.timer_loop(30, tick)




