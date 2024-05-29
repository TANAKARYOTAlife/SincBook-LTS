def Sinc_HTML_Read():
    with open( '' + '.html',
                'r',
                encoding='UTF-8') as Sinc_HTML_Format:
        Sinc_Your_Html = Sinc_HTML_Format.read()
    
def Sinc_HTML_Write():
    with open( 'page-content' + '.html',
                'w',
                encoding='UTF-8') as Sinc_HTML_Element:
        Sinc_Your_Book_Html = Sinc_Your_Html.format( Your_Title = '' )
        Sinc_HTML_Element.write(Sinc_Your_Book_Html)
