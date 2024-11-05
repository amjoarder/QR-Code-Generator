import qrcode

image = qrcode.make("https://just.edu.bd/")
image.save("JUST.png")