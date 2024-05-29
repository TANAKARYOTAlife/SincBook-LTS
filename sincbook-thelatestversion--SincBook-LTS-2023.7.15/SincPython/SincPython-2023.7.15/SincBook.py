import os

class SincBook:
    def __init__(self):
        pass
    
    def get_My_Sinc_Book_Title(self):
        for My_Sinc_File in os.listdir():
            My_Sinc_File_extension = os.path.splitext(My_Sinc_File)[1]
            if(My_Sinc_File_extension == '.txt' ):    
                My_Sinc_Book_Title = os.path.splitext(My_Sinc_File)[0]
                break
            else:
                continue
        try:
            My_Sinc_Book_Title
        except:
            print( 'My_Sinc_Book_Title is not defined.')
            return
            
        print(  "==  My_Sinc_Book_Title  ==\n"
            '[' + My_Sinc_Book_Title + ']\n' + 
            "==  End_Of_My_Sinc_Book_Title  ==\n")

        return  My_Sinc_Book_Title
