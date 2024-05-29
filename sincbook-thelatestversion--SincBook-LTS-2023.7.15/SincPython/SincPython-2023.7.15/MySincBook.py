import os
import sys
import datetime
import zipfile
from SincBook import SincBook

class MySincBook(SincBook):
    sys.dont_write_bytecode = True
    
    def __init__(self):
        try:
            self.My_Sinc_Book_Title = super().get_My_Sinc_Book_Title()
        except:
            print( 'My_Sinc_Book_title is not defined.' )

    def Make_My_Directory(self):
        My_Directory = self.My_Sinc_Book_Title + '_HTML_File'
        os.makedirs( My_Directory , exist_ok = True )
        print('==  My_Directory  ==')
        print( str(My_Directory) + ' was made.' )
        print(' The path is ' + os.path.abspath(My_Directory))
        print('==  End_of_My_Directory  ==\n')
        return My_Directory

    def Read_My_Sinc_Book(self):    
        with open( self.My_Sinc_Book_Title + '.txt' ,
                'r',
                encoding='UTF-8') as Sinc_File:
            Sinc_Whole_Sentence = Sinc_File.read()
            Sinc_Each_Line_With_Blank = Sinc_Whole_Sentence.splitlines()
    
        Sinc_My_Chapter_Number = 1
        for Sinc_Each_Line in  Sinc_Each_Line_With_Blank:
            if(Sinc_Each_Line == '' ):
                Sinc_My_Chapter_Number +=1
        
        print('==  My_Story  ==')
        print('My story has ')
        print( str(Sinc_My_Chapter_Number) + ' chapters.' )
        print('==  End_of_My_Story  ==\n')
        return Sinc_Each_Line_With_Blank
        
    def Write_My_Sinc_Book(self):
        is_My_Chapter_Title = True
        try:
            self.Make_My_Directory()
            self.My_Sinc_Book_Title
        except:
            print( self.My_Sinc_Book_Title + ' is not defined.' )
        with open ( self.Make_My_Directory() + '/' +
                    self.My_Sinc_Book_Title + '.html' ,
                    'w',
                    encoding= 'UTF-8' ) as Sinc_My_Book_HTML:
            for Sinc_Each_Line in self.Read_My_Sinc_Book():
                if ( is_My_Chapter_Title ):
                    Sinc_My_Book_HTML.write(    '\t<h1>'+
                                                Sinc_Each_Line + 
                                                '</h1>\n' )
                    is_My_Chapter_Title = False
                else:
                    if( Sinc_Each_Line == '' ):
                        is_My_Chapter_Title = True
                    else:
                        Sinc_My_Book_HTML.write(    '\t<p>'+
                                                    Sinc_Each_Line +
                                                    '</p>\n' )
            print('==  Write_My_Sinc_Book ==')
            print( self.My_Sinc_Book_Title + '.html was created,'  )
            print('==  End_Of_Write_My_Sinc_Book ==\n')

    def Print_Sinc_Data_File(self):
        Sinc_File_Name = os.path.basename(__file__)
        Sinc_File_Path = __file__
        print('==  Sinc_Data_File  ==')
        print('This Sinc_File_Name is ' + '\n' + Sinc_File_Name )
        print('This Sinc_File_Path is ' + '\n' + Sinc_File_Path )
        def Sinc_Time_Stamp(time):
            return str(datetime.datetime.fromtimestamp(time))
        print( 'This Sinc_File is created on ' + '\n'
            + Sinc_Time_Stamp(os.path.getctime(__file__)))
        print( 'This Sinc_File is last modified on ' + '\n'
            + Sinc_Time_Stamp(os.path.getmtime(__file__)))
        print('==  End_of_Sinc_Data_File  ==')
        print('\n')

    def check_Sinc_Mimetype(self):
        is_Mimetype = False
        for Sinc_File in os.listdir():
            if( os.path.isfile('mimetype')):
                is_Mimetype = True
                print('==  Sinc_Mimetype  ==')
                print('mimetype already exists.')
                print('==  End_Of_Sinc_Mimetype  ==\n')
                break
            else:
                continue
        if( is_Mimetype ):
            with open( 'mimetype' , 'w' ) as Sinc_Mimetype_File:
                Sinc_Mimetype_File.write('application/epub+zip')

    def Print_Sinc_Top_Directory(self):
        print('==  Sinc_Top_Directory  ==')
        print(os.listdir())
        print('==  End_Of_Sinc_Top_Directory  ==\n')

    def Print_Sinc_All_Files(self):
        print('==  print_Sinc_All_Files  ==')
        for dirpath , dirnames , filenames in os.walk('./'):
            print('Path\t\t' + str(dirpath))
            print('Directory\t' + str(dirnames))
            print('Filenames\t' + str(filenames) + '\n')
        print('==   End_of_print_Sinc_All_Files  ==\n')

    def Sinc_Zip(self):
        is_OneDrive_Desktop = os.path.isdir(os.path.expanduser('~/OneDrive/Desktop'))
        if( is_OneDrive_Desktop ):
            My_OneDrive_Desktop_Path = os.path.expanduser('~/OneDrive/Desktop')
            My_Zipfile_Path = My_OneDrive_Desktop_Path    
            print('==  My_Desktop_Path  ==')
            print('My_Desktop_Path is\t' + str(My_OneDrive_Desktop_Path))
            print('==  End_Of_My_Desktop_Path  ==\n')
        else:
            My_Desktop_Path = os.path.expanduser('~/Desktop')
            My_Zipfile_Path = My_Desktop_Path
            print('The path ' + '~/Onedrive/Desktop' + 'is not defined.\n' )
        
        def Sinc_Not_Zip_mimetype():
            with zipfile.ZipFile(   My_Zipfile_Path +'/'+ \
                                    self.My_Sinc_Book_Title + '.epub' , 
                                    'w' ,
                                    zipfile.ZIP_STORED,) as My_Book_Not_Zip_EPUB :
                    My_Book_Not_Zip_EPUB.write('mimetype')
        Sinc_Not_Zip_mimetype()

        def Sinc_Zip_EPUB_META_INF():
            def Sinc_Inner_Zip(Sinc_File):
                with zipfile.ZipFile(   My_Zipfile_Path + '/' +
                                    self.My_Sinc_Book_Title + '.epub' , 
                                    'a' ,
                                    zipfile.ZIP_DEFLATED) as My_Book_Zip_EPUB:
                    My_Book_Zip_EPUB.write(Sinc_File)
            Sinc_Zip_Directory_Names = ['EPUB','META-INF']
            print('==  ' + self.My_Sinc_Book_Title + '.epub All_File  ==')
            for dirpath , dirnames , filenames in os.walk('./'):
                if( dirpath == './' ):
                    dirnames = Sinc_Zip_Directory_Names
                    filenames = []
                elif( './EPUB' in dirpath ):
                    pass
                elif('./META-INF' in dirpath ):
                    pass
                else:
                    continue
                for filename in filenames:
                    print(os.path.join(dirpath,filename))
                    Sinc_Inner_Zip(os.path.join(dirpath,filename))
            print('==  ' + 'End_Of_' + self.My_Sinc_Book_Title + '.epub All_File  ==\n')
        Sinc_Zip_EPUB_META_INF()
            
                       

My_Sinc_Book = MySincBook()
My_Sinc_Book.Make_My_Directory()
My_Sinc_Book.Read_My_Sinc_Book()
My_Sinc_Book.Write_My_Sinc_Book()
My_Sinc_Book.Print_Sinc_Data_File()
My_Sinc_Book.check_Sinc_Mimetype()
My_Sinc_Book.Print_Sinc_Top_Directory()
My_Sinc_Book.Print_Sinc_All_Files()
My_Sinc_Book.Sinc_Zip()
