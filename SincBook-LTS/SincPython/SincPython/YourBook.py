import os
import datetime

class YourBook:
    def __init__(self):
        print('\n===  Sinc  ===')
        print(' ' + __name__ + ' is functioned.')
        print('===  Sinc  ===\n')
        self.print_your_book_title()
        self.print_your_book_chapter()
        self.print_your_book_data()

    def get_your_book_title(self):
        for Sinc_Each_File in os.listdir():
            Sinc_Each_File_extension = os.path.splitext(Sinc_Each_File)[1]
            if( Sinc_Each_File_extension == '.txt' ):
                Your_Book_Title = os.path.splitext(Sinc_Each_File)[0]
                break
            else:
                continue
        try:
            Your_Book_Title
        except:
            raise Exception('===  YourBook is not defined.  ===')
        return Your_Book_Title
            
    def read_your_book(self):
        Your_Book_Title = self.get_your_book_title()
        with open( Your_Book_Title + '.txt' ,
                    'r',
                    encoding='UTF-8') as Your_Book_Content:
            Your_Whole_Story = Your_Book_Content.read() 
        return Your_Whole_Story
    
    def get_your_book_chapter(self):
        Your_Book_All_Line = self.read_your_book().splitlines()
        Your_Book_Chapter_Number = 1 + Your_Book_All_Line.count('')        
        return Your_Book_Chapter_Number

    def print_your_book_title(self):
        Your_Book_Title = self.get_your_book_title()
        print('==  Your_Book_Title  ==')
        print(' YourBook is ' + '[' + Your_Book_Title + '].' )
        print('==  Your_Book_Title  ==\n')

    def print_your_book_chapter(self):
        print('==  Your_Book_Chapter  ==')
        print(' YourBook has ' + str(self.get_your_book_chapter()) + ' chapters.' )
        print('==  Your_Book_Chapter  ==\n')
    
    def print_your_book_data(self):
        Your_Book_Path = os.path.abspath(self.get_your_book_title() + '.txt')
        print('==  YourBook_Data  ==')
        print(' YourBook path is ' + '\n' + ' ' +Your_Book_Path )
        def Sinc_Time_Stamp(time):
            return str(datetime.datetime.fromtimestamp(time))
        print(' YourBook is created on ' + Sinc_Time_Stamp(os.path.getctime(__file__)))
        print(' YourBook is modified on ' + Sinc_Time_Stamp(os.path.getmtime(__file__)))
        print('==  YourBook_Data  ==\n')

if(__name__ == '__main__'):
    YourBook()