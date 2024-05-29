#Sinc_Your_Book_Read_and_Write
import Sinc_Your_Book_Title
import Sinc_Your_Directory

def Sinc_Your_Book_Read() :
	Your_Title = Sinc_Your_Book_Title.Sinc_Your_Book_Title()
	Sinc_Your_Chapter_Number = 1
	with open( Your_Title + '.txt' ,
				'r',
				encoding='UTF-8') as Your_Book:
		Sinc_Your_Line = Your_Book.read().split('\n')
		for Sinc_Your_Chapter in  Sinc_Your_Line:
			if(Sinc_Your_Chapter == '' ):
				Sinc_Your_Chapter_Number +=1
		print('==  Your_Story  ==')
		print('Your story has ')
		print( str(Sinc_Your_Chapter_Number) + ' sections.' )
		print('==  End_of_Your_Story  ==')
		print('\n')
		return Sinc_Your_Line
	
def Sinc_Your_Book_Write():
	Your_Title = Sinc_Your_Book_Title.Sinc_Your_Book_Title()
	Your_Chapter_Title_Bool = True
	tab = '		'	
	with open ( Sinc_Your_Directory.Sinc_Your_Directory() +
				'/' +
				Your_Title + '.html' ,
				'w',
				encoding= 'UTF-8') as Sinc_Your_Book_HTML:
		for Sinc_Each_Your_Line in Sinc_Your_Book_Read():
			if ( Your_Chapter_Title_Bool ):
				Sinc_Your_Book_HTML.write(	tab +
											'<h1>'+
											Sinc_Each_Your_Line + 
											'</h1>' + '\n')
				Your_Chapter_Title_Bool = False
			else:
				if( Sinc_Each_Your_Line == '' ):
					Your_Chapter_Title_Bool = True
				else:	
					Sinc_Your_Book_HTML.write( 	tab +
												'<p>'+
												Sinc_Each_Your_Line +
												'</p>' + '\n')
		print( Your_Title + '.html was created,'  )
		

Sinc_Your_Book_Write()

