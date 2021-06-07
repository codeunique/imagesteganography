# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:20:43 2020

@author: rajee
"""

from PIL import Image
import numpy as np
import keyscheduler as ks
import common as com
from os import system, name 



    
def embed(im,xparams,yparams,message):
    seedx = xparams[2]
    seedy = yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedx%yparams[4]
    istraversed =[]
    im[indexx][indexy]=len(message)//255
    seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
    seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedy%yparams[4]
    im[indexx][indexy]= len(message)%255
    i = 0
    print(len(message))
    while i<len(message):
        seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
        seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
        indexx = seedx%xparams[4]
        indexy = seedy%yparams[4]        
        if (indexx,indexy) not in istraversed:
            if (message[i]=='0') and (im[indexx][indexy]% 2 != 0):     
                    if im[indexx][indexy] == 255:
                        im[indexx][indexy] -= 1
                        #im[indexx][indexy] = 0
                    else:
                        im[indexx][indexy] +=1
                        #im[indexx][indexy] = 0
                      
            elif (message[i]== '1') and (im[indexx][indexy]% 2 == 0): 
                 if im[indexx][indexy] ==0:
                        im[indexx][indexy] +=1
                        #im[indexx][indexy] = 0
                 else:
                     im[indexx][indexy] -=1
                     #im[indexx][indexy] = 0
            i +=1
            istraversed.append((indexx,indexy))
            
                    
def encrypt(key,message,image):
    plaintextbin = com.strToBinary(message) 
    keybin= com.strToBinary(key)
    whitemessage = com.getXOR(plaintextbin,keybin)
    im = np.array(Image.open(image,'r').convert("L"))
    params = ks.keyscheduler(keybin)
    xparams,yparams = params[0],params[1]
    xparams.append(im.shape[0])
    yparams.append(im.shape[1])
    embed(im, xparams, yparams, whitemessage)
    img = Image.fromarray(im)
    imagename = "newimage1.png"
    img.save(imagename)
    print("image is ready as:" + imagename)
    
       
# Driver Code 
if __name__ == '__main__': 
    key =input('enter the 32 characters secret key:')
    data = input("enter the message to embedd :")
    image = input("enter the path of image file :")
    encrypt(key,data,image)
