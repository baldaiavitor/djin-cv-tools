from PIL import ImageColor

class BasicColors:
    Black	=	"#000000"	
    White	=	"#FFFFFF"	
    Red	=	    "#FF0000"
    Lime	=	"#00FF00"
    Blue	=	"#0000FF"
    Yellow	=	"#FFFF00"
    Magenta	=	"#FF00FF"
    Maroon	=	"#800000"
    Olive	=	"#808000"
    Green	=	"#008000"
    Purple	=	"#800080"
    Navy	=	"#000080"

def RGB(color:BasicColors):
    return ImageColor.getcolor(color, "RGB")

def RGBA(color:BasicColors):
    return ImageColor.getcolor(color, "RGBA")

def BGRA(color:BasicColors):
    RGBAColor =  ImageColor.getcolor(color, "RGBA")
    BGRAColor = (RGBAColor[2], RGBAColor[1], RGBAColor[0], RGBAColor[3])
    return BGRAColor