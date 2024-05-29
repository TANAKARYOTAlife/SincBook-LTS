import os
import Sinc_Your_Book_Title

#Sinc_Your_Directory
def Sinc_Your_Directory():
	Your_Directory = Sinc_Your_Book_Title.Sinc_Your_Book_Title() + '_HTML_Text'
	os.makedirs( Your_Directory , exist_ok = True )
	print('==  Your_Directory  ==')
	print( str(Your_Directory) + ' was made.' )
	print('\n')
	print(' The path is ' + '\n'
			+ os.path.abspath(Your_Directory))
	print('==  End_of_Your_Directory  ==')
	print('\n')
	return Your_Directory
