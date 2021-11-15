from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from email import message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import cairocffi
import pangocffi
import pangocairocffi

def certificatetemplate(name):
    filename = "certificate.png"
    surface = cairocffi.ImageSurface.create_from_png(filename)
    context = cairocffi.Context(surface)
    context.translate(100,120)
    PANGO_SCALE = pangocffi.units_from_double(1)
    WIDTH=300
    HEIGHT=200
    layout = pangocairocffi.create_layout(context)
    layout.set_markup(name)
    layout.set_width(300*1100)
    ink_box,log_box = layout.get_extents()
    text_width,text_height = (1.0*log_box.width/PANGO_SCALE,
                          1.0*log_box.height/PANGO_SCALE)
    context.move_to(WIDTH/2-text_width/2, HEIGHT/2-text_height/2)

    pangocairocffi.show_layout(context, layout)
    surface.write_to_png(str(name)+'.png')
    surface.finish()

    return(name+'.png')



def sendmail(pngname,receiverid):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "gmdabirami1999@gmail.com"
    password = "mythili@8799"
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

