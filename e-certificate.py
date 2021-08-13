
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from email import message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def certificatetemplate(name):
    font_path = "C:\WINDOWS\FONTS\TIMES.TTf"
    certificate = "D:/dbp/top.jpg"
    text_y_position = 450
    
    img = Image.open(certificate, mode ='r')
	
    image_width =1200
	
    image_height = 730
	
    draw = ImageDraw.Draw(img)
	
    font = ImageFont.truetype(font_path, size=100 )
	
    text_width, _ = draw.textsize(name, font = font)

	
    draw.text(
			(
				(image_width - text_width) / 2,
				text_y_position
			),
			name,
			font = font	,
			fill=(0,0,0)
           )

	
    img.save("{}.png".format(name))

    return(name+'.png')


def sendmail(pngname,receiverid):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = input('enter your emailid')
    password = input('enter your password')
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() 
        server.starttls(context=context) 
        server.ehlo() 
        server.login(sender_email, password)
        f= open(pngname, 'rb')
        msg = MIMEMultipart()
        msg['Subject'] = 'sending mail through python'
	msg['From']=sender_email
	msg['To']=receiverid
        body="your certificate has been attached here"
        msgText = MIMEText('<b>%s</b>'%(body),'html')  
        msg.attach(msgText) 
        img=MIMEImage(f.read(),name=os.path.basename(pngname))
        img.add_header("Content-ID","<{}>".format(pngname))
        msg.attach(img)
        server.sendmail(sender_email,receiverid, msg.as_string())
    
    except Exception as e:
         print(e)
    finally:
         server.quit()


col_list = ["Name", "Email"]
df=pd.read_csv('demolist.csv',usecols=col_list)
new=df.dropna()
for i,j in zip(new['Name'], new['Email']):
    value=certificatetemplate(i)
    sendmail(value,j)

