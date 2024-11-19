class Button:
    def __init__(self, name, centerX, centerY, width, height, label='', fill='white', border=None, borderWidth=2,
                 align='center', textFill='black', textFont='monospace'):
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

    def getShape(self):
        return [self.centerX, self.centerY, self.width, self.height, self.fill, self.border, self.borderWidth, self.align]

    def getLabel(self):
        return(self.label, self.centerX, self.centerY, self.textFill, self.textFont)