import qrcode
# 1 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Rian&entry.1476705422=Analyst
# 2 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Sam&entry.1476705422=Developer
# 3 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Ben&entry.1476705422=IT
# 4 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Charlie&entry.1476705422=Sales
# 5 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Lisa&entry.1476705422=Actuary
# 6 https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Angel&entry.1476705422=Legal


img1 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Rian&entry.1476705422=Analyst")
img1.save("img1.png")

img2 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Sam&entry.1476705422=Developer")
img2.save("img2.png")

img3 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Ben&entry.1476705422=IT")
img3.save("img3.png")

img4 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Charlie&entry.1476705422=Sales")
img4.save("img4.png")

img5 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Lisa&entry.1476705422=Actuary")
img5.save("img5.png")

img6 = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSfmrjqnslKTmh6QzzLckqoRiG2QDtDDXR2lr-Yv7KpT0Le0xw/formResponse?entry.1358643624=Angel&entry.1476705422=Legal")
img6.save("img6.png")