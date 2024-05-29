#import
import os
import zipfile
import subprocess
import shutil
import Sinc_Your_Book_Title

#Enter_Your_Title
Your_Title = Sinc_Your_Book_Title.Sinc_Your_Book_Title()

def Sinc_Not_Zip_mimetype() :
    My_desktop_path = os.path.expanduser('~/OneDrive/Desktop')
    print(My_desktop_path)
    with zipfile.ZipFile( My_desktop_path +'/'+Your_Title + '.epub' , 
                        'w' ,
                        zipfile.ZIP_STORED,) as Your_Book_Not_Zip_EPUB :
        Your_Book_Not_Zip_EPUB.write('mimetype')

def Sinc_Zip_EPUB_File():
    My_desktop_path = os.path.expanduser('~/OneDrive/Desktop')
    with zipfile.ZipFile( My_desktop_path + '/' + Your_Title + '.epub' , 
                        'a' ,
                        zipfile.ZIP_DEFLATED,
                        allowZip64 = True ) as Your_Book_Zip_EPUB:
        for dirpath , dirnames , filenames in os.walk( './' ):
            Your_Book_Zip_EPUB.write(dirpath)
            for Sinc_All_File in filenames:
                if( filenames != os.path.join(dirpath,Sinc_All_File)):
                    Your_Book_Zip_EPUB.write(os.path.join(dirpath,Sinc_All_File))

Sinc_Not_Zip_mimetype()
Sinc_Zip_EPUB_File()
