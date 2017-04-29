#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import smtplib

import pymysql, yaml 
from PIL import Image,ImageDraw, ImageFont
from dateutil.parser import parse





def mail(correo,oo):


	try:
	 	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	 	smtpserver.ehlo()
	 	smtpserver.starttls()
	 	smtpserver.ehlo()
  
		with open('tree.yaml', 'r') as f:
			doc = yaml.load(f)	
		txt = doc["treeroot"]["branch1"]

  # Datos 
  		try:
  			gmail_user = "soulyen@gmail.com"
  			gmail_pwd = txt
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

	try:
		smtpserver.sendmail("Diseño.net <"+gmail_user+">", to, msg)
	except smtplib.SMTPException:
		print ("El correo no pudo ser enviado" + "\n")
		smtpserver.close()
		
		




def ima(url,name,date,dise):

	fin = open(url,"rb")#abre archivo ingresar a base de datos
   	img = fin.read()#lee el archivo 
   	
	ajustada = img.resize((800, 600))
	fin.close() #cierra el archivo
	draw = ImageDraw.Draw(ajustada)
	font = ImageFont.truetype("arial.ttf", 100)
	font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 60)
	draw.text((190,280), "VERSION NO " , font=font, fill="RED")
	draw.text((200,330), "COMERCIAL " , font=font, fill="RED")
	font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 30)
	sfecha = date.strftime("%B %d, %Y")
	draw.text((50,550), ""+ sfecha , font=font, fill="RED")
	draw.text((50,520), "" + dise, font=font, fill="RED")
	

	ajustada.save("./ImagesF/"+name+".png")
	#ajustada.show()
	mail(dise,name)

	return




def base():
	with open('tree.yaml', 'r') as f:
		doc = yaml.load(f)
	txt = doc["treeroot"]["branch2"]
	conn = pymysql.connect(host='localhost', port=3306, user='CLOUD', passwd= txt, db='CLOUD')
	cursor = conn.cursor()
	cursor.execute(
    "SELECT id, imagen,texto ,fecha_registro, correo FROM disenos_comentario WHERE estado = 'En proceso' "
	)
	for x, y, z, a ,b  in cursor.fetchall():

		print("{0} {1} {2} {3} {4}".format(x, y, z, a ,b))
		ima(y,z,a,b)
		
	print("hola")
	cursor.execute(
	"UPDATE diseno SET estado ='Disponible' WHERE estado='En proceso'"
	)
	conn.commit()
	print("mama")
	cursor.close()
	













def test():
	base()

if __name__ == '__main__':
    test()
