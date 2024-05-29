import os
import Sinc_File_Format

#Sinc_Your_Book_Title
def Sinc_Your_Book_Title():
	for Sinc_File in os.listdir():
		Sinc_File_Name = Sinc_File_Format.Sinc_File_Format(Sinc_File)[0]
		Sinc_File_Type = Sinc_File_Format.Sinc_File_Format(Sinc_File)[1]
		if(Sinc_File_Type == '.txt' ):
			global Your_Title
			Your_Title = Sinc_File_Name
			print('\n')
			print('==  Sinc_Your_Book_Title  ==')
			print ('Your_Book_Title is ' + '\n' \
					+ '「' + Your_Title + '」' )
			print('==  End_of_Your_Book_Title  ==')
			print('\n')
			return Your_Title
