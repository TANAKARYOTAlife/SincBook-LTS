import os
import datetime

#Sinc_File_Data_Function
def Sinc_Data_File():
	Sinc_File_Name = os.path.basename(__file__)
	Sinc_File_Path = __file__
	print('\n')
	print('==  Sinc_File_Data  ==')
	print('This Sinc_File_Name is ' + '\n' + Sinc_File_Name )
	print('This Sinc_File_Path is ' + '\n' + Sinc_File_Path )
	def Sinc_Time_Stamp(time):
		return str(datetime.datetime.fromtimestamp(time))
	print( 'This Sinc_File is created on ' + '\n'
		+ Sinc_Time_Stamp(os.path.getctime(__file__)))
	print( 'This Sinc_File is last modified on ' + '\n'
		+ Sinc_Time_Stamp(os.path.getmtime(__file__)))
	print('==  End_of_Sinc_File_Data  ==')
	print('\n')	
	print('==  Sinc_All_File_Composition  ==')
	for dirpath , dirnames , filenames in os.walk('./'):
		print('Path' + ' ' + str(dirpath))
		print('Directory' + ' ' + str(dirnames))
		print('Filenames' + ' ' + str(filenames))
	print('==   End_of_All_Sinc_File_Composition  ==')
	print('\n')

Sinc_Data_File()
