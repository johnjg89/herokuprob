#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import smtplib

import pymysql, yaml 
from PIL import Image,ImageDraw, ImageFont
from dateutil.parser import parse





def mail(correo,oo):


	try:
	 	smtpserver = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com", 587)
	 	smtpserver.ehlo()
	 	smtpserver.starttls()
	 	smtpserver.ehlo()

		with open('tree.yaml', 'r') as f:
			doc = yaml.load(f)	
		txt = doc["treeroot"]["branch1"]

  # Datos 
  		try:
  			gmail_user = "AKIAIQ673NA5RDUMX2CQ"
  			gmail_pwd = "AsCuuQe/j6xksk8EE5XFh+3sYnv7uhrLSnyuJM+MYJb4"
  			smtpserver.login(gmail_user, gmail_pwd)
  		except smtplib.SMTPException:
  			
  			print ("Autenticacion incorrecta" + "\n")
  			smtpserver.close()
  			getpass.getpass("Presione ENTER para continuar...")
  			
 	
	except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
 		print ("Fallo en la conexion con Gmail")
 		print (getpass.getpass("Presione ENTER para continuar..."))
 		sys.exit(1)
 	
 	while True:
 		to = correo
 		if to != "":
 			break
 		else:
 			print ("El correo es necesario!!!")
 
	sub = "Diseño Disponible" 
	bodymsg = "Hola " + oo +" tu Diseno esta listo"
	print ("")
	header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
	print (header)
	msg = header + "\n" + bodymsg + "\n\n"
	print (msg)
	print(to)

	smtpserver.sendmail("soulyen@gmail.com",to, msg)
	try:
		print ("correo")
		smtpserver.sendmail("soulyen@gmail.com",to, msg)
	except smtplib.SMTPException:
		print ("El correo no pudo ser enviado" + "\n")
		print  ("2")
		smtpserver.close()



def ima(url,name,date,dise,us,nombr):
	imagen = Image.open(url)
	ajustada = imagen.resize((800, 600))

	draw = ImageDraw.Draw(ajustada)
	font = ImageFont.truetype("arial.ttf", 100)
	font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 60)
	draw.text((190,280), "VERSION NO " , font=font, fill="RED")
	draw.text((200,330), "COMERCIAL " , font=font, fill="RED")
	font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 30)
	sfecha = date.strftime("%B %d, %Y")
	draw.text((50,550), ""+ sfecha , font=font, fill="RED")
	draw.text((50,520), "" + nombr, font=font, fill="RED")
	

	ajustada.save("./ImagesF/"+name+".png")
	#ajustada.show()
	saul = "./ImagesF/"+name+".png"
	with open('tree.yaml', 'r') as f:
		doc = yaml.load(f)
	txt = doc["treeroot"]["branch2"]
	conn = pymysql.connect(host='cloud.cyrxwagygq5a.us-east-1.rds.amazonaws.com', port=3306, user='CLOUD', passwd= txt, db='CLOUD')
	cursor = conn.cursor()
	cursor.execute(
	"UPDATE disenos_comentario SET imagen=%s  WHERE id=%s ", (saul, us))
	conn.commit()
	print("mama")
	cursor.close()
	mail(dise,nombr)

	return




def base():
	with open('tree.yaml', 'r') as f:
		doc = yaml.load(f)
	txt = doc["treeroot"]["branch2"]
	conn = pymysql.connect(host='cloud.cyrxwagygq5a.us-east-1.rds.amazonaws.com', port=3306, user='CLOUD', passwd= txt, db='CLOUD')
	cursor = conn.cursor()
	cursor.execute(
    "SELECT id, imagen,texto ,fecha_registro, correo , nombre  FROM disenos_comentario WHERE estado = 'En proceso' "
	)
	for x, y, z, a ,b ,k  in cursor.fetchall():

		print("{0} {1} {2} {3} {4} {5}".format(x, y, z, a ,b ,k))
		ima(y,z,a,b,x,k)
		
	print("hola")
	cursor.execute(
	"UPDATE disenos_comentario SET estado ='Disponible' WHERE estado='En proceso'"
	)
	conn.commit()
	print("mama")
	cursor.close()
	













def test():
	base()

if __name__ == '__main__':
    test()
