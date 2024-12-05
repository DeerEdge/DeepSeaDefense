from cmu_graphics import *
from check_functions import *

class Button:
    def __init__(self, name, centerX, centerY, width, height, label='', fill='white', border=None, borderWidth=2,
                 align='center', textFill='black', textFont='arial', image=None, imageWidth=None, imageHeight=None):
        self.id = name
        self.centerX = centerX
        self.centerY = centerY
        self.width = width
        self.height = height
        self.label = label
        self.fill = fill
        self.border = border
        self.borderWidth = borderWidth
        self.align = align
        self.textFill = textFill
        self.textFont = textFont
        self.actions = []
        self.image = image
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight

    def getShape(self):
        return [self.centerX, self.centerY, self.width, self.height, self.fill, self.border, self.borderWidth, self.align]

    def getLabel(self):
        return(self.label, self.centerX, self.centerY, self.textFill, self.textFont)

    def containsPoint(self, mouseX, mouseY):
        return isWithinRect(self.centerX, self.centerY, self.width, self.height, mouseX, mouseY)

    def draw(self):
        drawRect(self.centerX, self.centerY, self.width, self.height, fill=self.fill,
                 border=self.border, borderWidth=self.borderWidth, align=self.align)
        if self.image == None:
            drawLabel(self.label, self.centerX, self.centerY, fill=self.textFill, font=self.textFont, align=self.align,
                      size=18)
        else:
            drawImage(self.image, self.centerX, self.centerY, align=self.align, width=self.imageWidth, height=self.imageHeight,
                      border=self.border, borderWidth=self.borderWidth)