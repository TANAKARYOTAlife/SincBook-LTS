import os
import datetime

class YourBook:
    def __init__(self):
        print('===  Sinc  ===')
        print(' ' + __name__ + ' is functioning.')
        print('===  Sinc  ===\n') 
        self.print_your_book_title()
        self.print_your_book_chapter()
        self.print_your_book_data()

    def reach_your_book(self):
        for dirs,insideDirs,files in os.walk("./"):
            for file in files:
                sinc_file_name =  os.path.splitext(file)[0]
                sinc_file_extension = os.path.splitext(file)[1]
                if(sinc_file_extension == ".txt"):
                    your_book_name = sinc_file_name
                    your_book_path = os.path.join(dirs,file)
                    return your_book_name,your_book_path 
                
    def read_your_book(self):
        Your_Book_Path = self.reach_your_book()[1]
        with open( Your_Book_Path ,
                    'r',
                    encoding='UTF-8') as Your_Book_Content:
            Your_Whole_Story = Your_Book_Content.read() 
        return Your_Whole_Story
    
    def get_your_book_chapter(self):
        Your_Book_All_Line = self.read_your_book().splitlines()
        Your_Book_Chapter_Number = 1 + Your_Book_All_Line.count('')        
        return Your_Book_Chapter_Number

    def print_your_book_title(self):
        Your_Book_Title = self.reach_your_book()[0]
        print('==  Your_Book_Title  ==')
        print(' YourBook is ' + '[' + Your_Book_Title + '].' )
        print('==  Your_Book_Title  ==\n')

    def print_your_book_chapter(self):
        print('==  Your_Book_Chapter  ==')
        print(' YourBook has ' + str(self.get_your_book_chapter()) + ' chapters.' )
        print('==  Your_Book_Chapter  ==\n')
    
    def print_your_book_data(self):
        Your_Book_File = self.reach_your_book()[1]
        Your_Book_Path = os.path.abspath(Your_Book_File)
        print('==  YourBook_Data  ==')
        print(' YourBook path is ' + '\n' + ' ' +Your_Book_Path )
        def Sinc_Time_Stamp(time):
            return str(datetime.datetime.fromtimestamp(time))
        print(' YourBook is added on ' + Sinc_Time_Stamp(os.path.getctime(Your_Book_File)))
        print(' YourBook is modified on ' + Sinc_Time_Stamp(os.path.getmtime(__file__)))
        print('==  YourBook_Data  ==\n')

if(__name__ == '__main__'):
    YourBook()