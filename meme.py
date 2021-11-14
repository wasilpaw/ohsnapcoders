from PIL import Image, ImageDraw, ImageFont

meme = Image.open('meme_back.png')
meme_size = (1280,1024)             # resize background to a standard resolutions
meme = meme.resize(meme_size)
actor = Image.open('kid.png')
actor_size = (512,544)
actor = actor.resize(actor_size)    # resize the top element
meme.paste(actor,(400,200),actor.convert('RGBA'))   # place the element on top of background
draw = ImageDraw.Draw(meme)
text = "10 MINUTES LATE TO CLASS"
font = ImageFont.truetype('impact.ttf', 100)
draw.text((150, 50), text, font=font)
text2 = "TEACHER ISN'T THERE YET"
font = ImageFont.truetype('impact.ttf', 92)
draw.text((200, 800), text2, font=font)
meme.save("meme.png")


