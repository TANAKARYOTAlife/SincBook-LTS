import os
import sys
import zipfile
sys.dont_write_bytecode = True
from YourBook import YourBook

class SincCreator():
    print('\n===  Sinc  ===')
    print(' ' + __name__ + ' is functioning.')
    print('===  Sinc  ===\n')    
    Your_Book = YourBook()
    Your_Book_Title = Your_Book.get_your_book_title()
    Your_Whole_Story = Your_Book.read_your_book()
    Your_Book_All_Line = Your_Whole_Story.splitlines()
    Your_Book_Directory = Your_Book_Title + '_html'

    def __init__(self):
        if(__name__ == '__main__'):
            self.make_your_book_directory()
            self.write_your_book_html()
            self.is_sinc_mimetype()
            self.is_sinc_metainf()
            self.print_mydesktop_path()
        
    def make_your_book_directory(self):
        if( SincCreator.Your_Book_Directory not in os.listdir()):    
            os.makedirs( SincCreator.Your_Book_Directory)
            print('==  YourBook_Directory  ==')
            print(' ' + SincCreator.Your_Book_Directory + ' is made.')
            print(' The path is ' + os.path.abspath(SincCreator.Your_Book_Directory))
            print('==  YourBook_Directory  ==\n')
        else:
            print('==  YourBook_Directory  ==')
            print(' ' + SincCreator.Your_Book_Directory + ' alredy exists.')            
            print('==  YourBook_Directory  ==\n')
            
    def make_your_book_html(self):
        Your_Book_HTML = ''
        is_My_Chapter_Title = True
        for Your_Book_Each_Line in SincCreator.Your_Book_All_Line:
            if( Your_Book_Each_Line== '' ):
                is_My_Chapter_Title = True
                continue
            if ( is_My_Chapter_Title ):
                Your_Book_HTML += '\t<h1>'+ Your_Book_Each_Line +'</h1>\n'
                is_My_Chapter_Title = False
            else:
                Your_Book_HTML += '\t<p>' + Your_Book_Each_Line + '</p>\n'
        return Your_Book_HTML
        
    def write_your_book_html(self):
        with open ( SincCreator.Your_Book_Directory + '/' +
                    SincCreator.Your_Book_Title + '.html' ,
                    'w',
                    encoding= 'UTF-8') as Your_Book_HTML:
            Your_Book_HTML.write(self.make_your_book_html())
            print('==  Your_Book_html ==')
            print(' ' + SincCreator.Your_Book_Title + '.html is published.' )
            print('==  Your_Book_html ==\n')    
    
    def is_sinc_mimetype(self):
        if( 'mimetype' in os.listdir()):
            print('==  Sinc_Mimetype  ==')
            print(' mimetype is defined.')
            print('==  Sinc_Mimetype  ==\n')
        else:
            with open( 'mimetype' , 'w' ) as Sinc_Mimetype_File:
                Sinc_Mimetype_File.write('application/epub+zip')

    def is_sinc_metainf(self):    
        if('META-INF' in os.listdir()):
            print('==  Sinc_META_INF  ==')
            print(' META_INF is defined.')
            print('==  Sinc_META_INF  ==\n')
        else:
            raise Exception('==  Sinc_META_INF is not defined.  ==')
    
    def is_onedrive(self):
        is_OneDrive_Desktop = False
        is_OneDrive_Desktop = os.path.isdir(os.path.expanduser('~/OneDrive/Desktop'))
        if( is_OneDrive_Desktop ):
            My_OneDrive_Desktop_Path = os.path.expanduser('~/OneDrive/Desktop')
            MyBook_Path = My_OneDrive_Desktop_Path    
        else:
            My_Desktop_Path = os.path.expanduser('~/Desktop')
            MyBook_Path = My_Desktop_Path
        return MyBook_Path , is_OneDrive_Desktop
    
    def print_mydesktop_path(self):
        MyDesktop_Path = self.is_onedrive()[0]
        is_onedrive = self.is_onedrive()[1]
        if(is_onedrive):
            print('==  MyDesktop_Path  ==')
            print(' OneDrive is enabled.')
            print(' MyDesktop_Path is ' + str(MyDesktop_Path))
            print('==  MyDesktop_Path  ==\n')
        else:
            print('==  MyBook_Path  ==')
            print(' OneDrive is not enabled')
            print(' MyBook_Path is\t' + str(MyDesktop_Path))
            print('==  MyBook_Path  ==\n')

    def sinc_not_zip(self):
        MyBook_Path = self.is_onedrive()[0]
        with zipfile.ZipFile(   MyBook_Path +'/'+ \
                                SincCreator.Your_Book_Title + '.epub', 
                                'w',
                                zipfile.ZIP_STORED) as Not_Zip_MyBook:
                    Not_Zip_MyBook.write('mimetype')

    def sinc_epub_metainf(self):
        MyBook_Directory = ['EPUB','META-INF']
        MyBook_File = 'mimetype'
        MyBook_Zips= []
        for dirpath , dirnames , filenames in os.walk('./'):
            if( dirpath == './' ):
                dirnames = MyBook_Directory
                filenames = [MyBook_File]
            elif( './EPUB' in dirpath ):
                pass
            elif('./META-INF' in dirpath ):
                pass
            else:
                continue
            for filename in filenames:
                if(filename == MyBook_File):
                    continue
                MyBook_Zips.append(os.path.join(dirpath,filename))
        return MyBook_Zips

    def sinc_zip(self,MyBook_Files):
        MyBook_Files = self.sinc_epub_metainf()
        MyBook_Path = self.is_onedrive()[0]
        for MyBook in MyBook_Files:
            with zipfile.ZipFile(   MyBook_Path + '/' +
                                    SincCreator.Your_Book_Title + '.epub', 
                                    'a',
                                    zipfile.ZIP_DEFLATED) as Zip_MyBook:
                Zip_MyBook.write(MyBook)

    def finalize_mybook(self):
        MyBook_Zips = self.sinc_epub_metainf()
        print('==  MyBook  ==')
        for MyBook_Zip in MyBook_Zips:
            print(MyBook_Zip)
        print('==  MyBook  ==\n')
    
    def sinc_mybook(self):
        self.sinc_not_zip()
        self.sinc_zip(self.sinc_epub_metainf())

if(__name__ == '__main__'):
    Sinc_Book = SincCreator()