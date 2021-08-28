import qrcode

print("Convert your links to QR Code instantly ")

link = input("Enter your link here : ")
out = input("Enter the name of output image :")

img = qrcode.make(link)
type(img)

img.save(f"./img/{out}.png")
img.show()

print("Thanks for using the program!")
