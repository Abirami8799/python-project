from PIL import Image, ImageDraw, ImageFont



def coupons(names: str, certificate: str, font_path: str):
	
		
		text_y_position = 420
		img = Image.open(certificate, mode ='r')
		image_width =1200
		image_height = 730
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(font_path, size=100,encoding="utf-8" )
		text_width, _ = draw.textsize(names, font = font)
        
		draw.text(
			
			(
				(image_width - text_width) / 2,
				text_y_position
			),
		    names,
			font = font	,
			fill=(0,0,0)
			
           )
        
		

		img.save("{}.png".format(names))


s ='தேன்மொழி'


	
FONT = r"C:\WINDOWS\FONTS\LATHA.TTF"
CERTIFICATE = "D:/dbp/top.jpg"
 


coupons(s, CERTIFICATE, FONT)
