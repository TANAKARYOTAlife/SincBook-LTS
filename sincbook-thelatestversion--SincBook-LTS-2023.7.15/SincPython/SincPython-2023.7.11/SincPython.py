import os
import sys
import Sinc_Data_File
import Sinc_Your_Directory
import Sinc_Your_Book_Read_and_Write
import Sinc_Zip


def main():
    sys.dont_write_bytecode = True
    Sinc_All_Functions_Py = os.listdir('SincPython/SincPython')
    def Sinc_Function():
        print('\n')
        print('==  Sinc_All_Funtions  ==')
        print('Sinc_All_Functions are below.')
        for Sinc_Each_Function in Sinc_All_Functions_Py:
            Sinc_Name_Ext_Function = os.path.splitext(Sinc_Each_Function)
            if(Sinc_Name_Ext_Function[1] == '.py' ):
                print( Sinc_Each_Function )
        print('==  End_of_Sinc_All_Funtions  ==')
        print('\n')
        print('==  Sinc_Funtions  ==')
        '''for key,value in Sinc_Order.items():        
            print( '    ' + str(value) + ' starts' )
            value
            print( '    ' + str(value) + ' ended. ')'''
    Sinc_Function()
    
def  Sinc_All_Functions_Number():
    global Sinc_All_Functions
    Sinc_All_Functions = {  True : 'SincPython.py' ,
                            True : 'Sinc_Data_File.py',
                            False : 'Sinc_Your_Book_Title.py',
                            True : 'Sinc_Your_Book_Title_Read_and_Write.py',
                            False : 'Sinc_File_Format.py',
                            False : 'Sinc_HTML_Format.py',
                            True : 'SincYour_Directory.py',
                            False : 'Sinc_Mimetype.py',
                            True : 'Sinc_Zip.py'}
    global Sinc_Order
    Sinc_Order = {  1 : Sinc_Data_File,
                    3 : Sinc_Your_Directory,
                    2 : Sinc_Your_Book_Read_and_Write,
                    4 : Sinc_Zip}
    print('==  Sinc_Order  ==')
    print('Sinc_All_Functions are done with the order below.')
    for key,value in Sinc_Order.items():
        print( ' ' + str(key) + ':' + str(value) )

Sinc_All_Functions_Number()
main()
