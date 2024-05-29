import os

#Sinc_File_Format
def Sinc_File_Format(Sinc_File):
	base,ext = os.path.splitext(Sinc_File) 
	if( ext == '.py' ):
		pass
	elif( ext == '.html' ):
		pass
	elif( ext == '.xml' ):
		pass
	elif( ext == '.opf' ):
		pass
	elif( ext == '.css' ):
		pass
	else:
		pass
	return base,ext
