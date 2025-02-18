import qrcode

url = input("Enter URL: ")  # gets the url from user
img = qrcode.make(url)    # convert to a qr code
img.save("qrcode.png")    # saves