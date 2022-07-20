import qrcode
img = qrcode.make('some data')
type(img)
img.save('name_file.png')