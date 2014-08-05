#!/usr/bin/env python
import mechanize
from PIL import Image
import urllib
br=mechanize.Browser()
br.open('http://www.enigmagroup.org/forums/login/')
br.set_handle_robots(False)
br.select_form('frmLogin')
br.form['user']='Zer0x'
br.form['passwrd']='21057094aA'
br.submit()

im=br.open("http://www.enigmagroup.org/missions/programming/3/")
im=br.open('http://www.enigmagroup.org/missions/programming/3/image.php').read()


fil=open('img.jpg','wb')
fil.write(im)
fil.close()
img=Image.open('img.jpg')
pix=img.getpixel((1,1))
resultat= str(pix[0])+';'+str(pix[1])+';'+str(pix[2])
dat={
    'color':resultat ,
    'submit' : '1'
}

pes=urllib.urlencode(dat)

res=br.open("http://www.enigmagroup.org/missions/programming/3/image.php",data=pes)

print res.get_data()







