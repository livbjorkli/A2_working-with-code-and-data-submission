# Size of the canvas
size(800, 500);

# Paint background white
background (255, 255, 255)


# Petals on flower 
fill (255, 255, 255)
ellipse (400, 175, 110, 110)
ellipse (400, 325, 110, 110)
ellipse (325, 250, 110, 110)
ellipse (475, 250, 110, 110)

# Putting in text (colour and front size)
# Black text color
fill(0) 
# Text size 
textSize(20)

# Text in flower petals 
# Top petal
text("1", 400, 180) 
# Bottom petal
text ("1", 400, 350)
# Left petal
text ("1", 300, 250)
# Right petal
text ("1", 500, 250)

# Large flower in centre 
fill (255, 255, 255)
ellipse (400, 250, 100, 100)

# Text in centre of flower 
# Black text color
fill(0) 
text ("2", 390, 250)



# Stem of flower 
stroke (0)
strokeWeight (1)
line(420, 380, 420, 650);
line (400, 380, 400, 650)

# Text in centre of flower 
# Black text color
fill(0) 
text ("3", 405, 445)



# Adding in line to represent the ground 
stroke (0)
strokeWeight (1)
line (0, 450, 800, 450)

# Text in ground
# Black text color
fill(0) 
# Text on right side of ground
text ("4", 600, 500)
# Text on left side of ground 
text ("4", 200, 500)


# Bee on middle of flower 
# Shape of bee 
fill (255, 255, 255)
ellipse (430, 250, 50, 30)

# Text in shape of bee
# Black text color
fill(0) 
textSize (15)
text ("5", 410, 258)

# Bee stripes
fill (255)
rect (420, 238, 5, 26)
rect (435, 238, 5, 26)

# Text in bee stripe
# Black text color
fill(0) 
textSize (10)
# Text in left stripe
text ("6", 420, 260)
# Text in right stripe 
text ("6", 435, 260)

# Wing of bee
fill(255, 255, 255)
ellipse (430, 240, 30, 15)

# Text in wing of bee
# Black text color
fill(0) 
textSize (10)
text ("7", 429, 243)



# Antennae of bee
stroke (0)
strokeWeight (1)
# Left atennae 
line (409, 240, 395, 225)
# Right antennae
line (405, 249, 395, 265)


# Stinger of bee
fill (255)
triangle (455, 245, 465, 250, 455, 255)


# Text in wing of bee
# Black text color
fill(0) 
textSize (20)
text ("7", 90, 100)

# Inserting the sun in left corner 
fill (255)
stroke (1)
ellipse (90, 100, 150, 150)
fill(0) 
textSize (20)
text ("8", 85, 110)

# Adding in text for the sky
fill(0) 
textSize (20)
text ("9", 600, 200)


# Adding text in top right for key colours 
# Black text color
fill(0) 
# Size of font
textSize (20)
# Keys of colours
text("1 = purple", 670, 20)
text ("2 = pink", 670, 40)
text ("3 = green", 670, 60)
text ("4 = dark green", 670, 80)
text ("5 = yellow", 670, 100)
text ("6 = black", 670, 120)
text ("7 = white", 670, 140)
text ("8 = orange", 670, 160)
text ("9 = blue", 670, 180)
