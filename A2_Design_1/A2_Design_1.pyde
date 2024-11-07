# Size of the canvas
size(800, 500);

# Resize flower to middle
translate(width/2 - 100, height/2 - 100)

# Paint background white
background (255, 255, 255)


# Draw stem of middle flower 
line(96, 96, 96, 400);
line(105, 105, 105, 400);


# Leafs of flower on middle flower
ellipse(110, 200, 15, 15);
ellipse(91, 225, 15, 15);


# Change thick petal outline to thin black line on middle flower
strokeWeight(1);

# Insert each petal on middle flower
fill(255, 255, 255);
ellipse(50, 50, 100, 100);
ellipse(150, 50, 100, 100);
ellipse(50, 150, 100, 100);
ellipse(150, 150, 100, 100);

# Draw flower head (middle part of flower)
fill(255, 255, 255);
ellipse(100, 100, 100, 100);


# Putting in text (colour and front size)
# Black text color
fill(0) 
# Text size 
textSize(20)  

# Number "1" in each petal
# In top-left petal
text("1", 30, 50) 
# In top-right petal  
text("1", 155, 45)
# In bottom-left petal  
text("1", 30, 150)
# In bottom-right petal  
text("1", 155, 145) 

# Number "2" in the middle part of the flower 
text("2", 95, 108)

# Number "3" in stem 
# Adjusting text size 
textSize (17)
text("3", 96, 280)

# Number "4" in the leafs 
text ("4", 86, 230)
# In right leaf 
text ("4", 106, 206)



# Insert flower on the right 
# stem of right flower 
line (96 + 250, 96, 96 + 250, 400);
line (105 + 250, 105, 105 + 250, 400);

# Draw petals of right flower 
fill (255, 255, 255)
# Petals
ellipse (50 + 250, 50, 100, 100);
ellipse (150 + 250, 50, 100, 100);
ellipse (50 + 250, 150, 100, 100);
ellipse (150 + 250, 150, 100, 100);

# Centre of right flower 
fill (255, 255, 255)
ellipse (100 + 250, 100, 100, 100)

# Putting in text (colour and front size) for right flower 
# Black text color
fill(0) 
# Text size 
textSize(20)  

# Right flower numbers 
# Number 1 in top left petal 
text("1", 40 + 250, 50) 
# Number 1 in top right petal 
text ("1", 155 + 250, 50)
# Number 1 in bottom left petal 
text ("1", 40 + 250, 150)
#Number 1 in bottom right petal 
text ("1", 155 + 250, 150)

# Number 2 in centre of right flower 
text ("2", 95 + 250, 105)

# Number 3 on the stem of right flower 
# Adjusting text size 
textSize (17)
text("3", 96, 280)
text ("3", 96 + 250, 270)




# Insert left flower 
# Stem of left flower 
line (96 - 250, 96, 96 -  250, 400);
line (105 -  250, 105, 105 -  250, 400);

# Sraw petals of left flower 
fill (255, 255, 255)
# Petals 
ellipse (50 -  250, 50, 100, 100);
ellipse (150 -  250, 50, 100, 100);
ellipse (50 -  250, 150, 100, 100);
ellipse (150 -  250, 150, 100, 100);

# Middle centre of left flower 
fill (255, 255, 255)
ellipse (100 - 250, 100, 100, 100)

# Putting in text (colour and front size) for left flower 
# Black text color
fill(0) 
# Text size 
textSize(20)  

# Left flower numbers 
# Number 1 in top left petal 
text("1", 40 -  250, 50) 
# Number 1 in top right petal 
text ("1", 155 -  250, 50)
# Number 1 in bottom left petal 
text ("1", 40 - 250, 150)
# Number 1 in bottom right petal 
text ("1", 155 - 250, 150)

# Number 2 in centre of left flower 
text ("2", 95 - 250, 105)

# Number 3 on the stem of left flower 
# Adjusting text size 
textSize (17)
text("3", 96, 280)
text ("3", 96 - 250, 270)

# Insert text in sky
textSize (17)
text("5", 100, -50)



# Adding text in top right for key colours 
# Black text color
fill(0) 
# Size of font
textSize (20)
# Keys of colours
text("1 = orange", 370, -130)
text ("2 = yellow", 370, -110)
text ("3 = green", 370, -90)
text ("4 = dark green", 370, -70)
text ("5 = blue", 370, -50)
