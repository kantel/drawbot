size(640, 480)

my_text = "🐍 Hallo DrawBöttchen! 🐍"
print(my_text)

fill(0.9, 0, 0)
font("American Typewriter", 38)
text(my_text, (80, width()/2))

saveImage("images/drawbottest.jpg")