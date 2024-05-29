#import
import os

#Sinc_Mimetype_Function
def Sinc_Mimetype():
    with open( 'mimetype' , 'w' ) as Sinc_Mimetype_File:
        Sinc_Mimetype_File.write('application/epub+zip')

Sinc_Mimetype()
