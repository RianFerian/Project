import qrcode
# 1 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Rian&entry.1476705422=Analyst
# 2 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Sam&entry.1476705422=Developer
# 3 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Ben&entry.1476705422=IT


img1 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Rian&entry.1476705422=Analyst")
img1.save("img1.png")

img2 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Sam&entry.1476705422=Developer")
img2.save("img2.png")

img3 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Ben&entry.1476705422=IT")
img3.save("img3.png")
