# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:20:43 2020

@author: rajee
"""

from PIL import Image
import numpy as np
import keyscheduler as ks
import common as com


def extract(im,xparams,yparams):
    msg=""
    seedx = xparams[2]
    seedy = yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedx%yparams[4]
    istraversed =[]
    msglen = im[indexx][indexy]*255
    istraversed.append((indexx,indexy))
    seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
    seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedy%yparams[4]
    msglen += im[indexx][indexy]
    istraversed.append((indexx,indexy))
    i = 0
    print(msglen)
    while i<msglen:
        seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
        seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
        indexx = seedx%xparams[4]
        indexy = seedy%yparams[4]  
        if (indexx,indexy) not in istraversed:
            if(im[indexx][indexy]%2==0):
               msg = msg +'0'
            elif(im[indexx][indexy]%2!=0):
               msg = msg + '1'
            i +=1
            istraversed.append((indexx,indexy))
    return msg
            
                    
def decrypt(key,image):
    keybin= com.strToBinary(key)
    im = np.array(Image.open(image,'r').convert("L"))
    params = ks.keyscheduler(keybin)
    xparams,yparams = params[0],params[1]
    xparams.append(im.shape[0])
    yparams.append(im.shape[1])
    whitemessage = extract(im, xparams, yparams)
    message = com.getXOR(whitemessage,keybin)
    plaintext = com.binToString(message)
    return plaintext
    
       
# Driver Code 
if __name__ == '__main__': 
    key = input("enter the secret key :")
    image = input("enter the path of image file :")
    message =decrypt(key,image)
    print("message:" +str(message))
