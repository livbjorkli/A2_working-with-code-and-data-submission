# Size of the canvas
size(800, 500);

# Resize tree to middle
translate(width/2 - 100, height/2 - 100)

# Paint background white
background (255, 255, 255)

# Insert text in sky 
# Black text color
fill(0) 
# Size of font
textSize (20)
text("6", 100, -60)

# Adding in line to represent the ground
stroke (0)
strokeWeight (1)
line (-400, 270, 600, 270)

# Adding in the tree
# Draw the stem of the tree
fill (255, 255, 255)
rect (50, 190, 100, 250)

# Putting in text (colour and font size)
# Black text colour 
fill(0)
# Text size
textSize (20)

# Number 3 for the stem of the tree 
text ("3", 100, 305)


# Tree triangles 
# Bottom triangle tree
fill (255, 255, 255)
triangle (0, 190, 200, 190, 100, 80)

# Inserting Number 4 for the bottom tree
fill (0)
text ("4", 100, 180)

# Middle triangle tree
fill (255, 255, 255)
triangle (10, 130, 190, 130, 100, 30)

# Inserting Number 4 for the middle tree
fill (0)
text ("4", 100, 100)

# Top triangle tree
fill (255, 255, 255)
triangle (20, 80, 180, 80, 100, 0)

# Inserting Number 4 for the top tree
fill (0)
text ("4", 100, 50)

# Putting in text (colour and font size)
# Black text colour 
fill(0)
# Text size
textSize (20)

# Inserting Number 2 for the ground 
text ("2", 300, 300)
text ("2", -100, 300)

# Adding in left butterfly 
fill (255, 255, 255)
stroke (0)
strokeWeight (1)

# Rotate body of butterfly 
rotate (PI/3.10)

# Adding in left wing of left butterfly
ellipse (30, 100, 30, 50)

# Adding in antennae on left butterfly 
# Left antennae
stroke (0)
strokeWeight (1)
line (45, 90, 35, 70)
# Right antennae
line (45, 90, 55, 70)

# Adding in right wing of left butterfly 
ellipse (60, 100, 30, 50)

# Body of left butterfly 
stroke (0)
strokeWeight (1)
line (45, 90, 45, 110)



# Inserting butterfly on the right 
# Left wing
fill (255)
stroke (0)
strokeWeight (1)
ellipse (30, 0, 30, 40)
# Right wing
ellipse (60, 0, 30, 40)

# Inserting antennae on right butterfly 
stroke (0)
strokeWeight (1)
# Left antennae
line (45, -10, 40, -30)
# Right antennae 
line (45, -10, 50, -30)

# Insert body of butterfly on the right
stroke (0) 
strokeWeight (1)
line (45, -15, 45, 15)

# Putting in text (colour and font size)
# Black text colour 
fill(0)
# Text size
textSize (20)

# Number "1" in the left wing of the right butterfly 
text ("1", 24, 8)

# Number "1" in the right wing of the right butterfly 
text ("1", 55, 8)

# Number "1" in the left wing of the left butterfly 
text ("1", 24, 108)

# Number "1" in the right wing of the right butterfly 
text ("1", 55, 108)


# Adding the shape of an eclipse to be a sun in the left corner
fill (255)
stroke (0)
ellipse (-160, 125, 130, 130)

# Rotate number 5 to be straight
rotate (PI/0.6)

# Adding text "5" in sun
fill(0)
textSize (17)
text ("5", -195, -75)

# Adding text in top right for key colours 
# Black text color
fill(0) 
# Size of font
textSize (20)

# Adding text in top right for keys colours
text("1 = yellow", 380, -110)
text ("2 = light green", 380, -90)
text ("3 = brown", 380, -70)
text ("4 = dark green", 380, -50)
text ("5 = orange", 380, -30)
text ("6 = light blue", 380, -10)
