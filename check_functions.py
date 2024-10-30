
# Checks if a mouse action occurred inside a rectangle (rects must be aligned by their center)
def isWithinRect(centerX, centerY, width, height, mouseX, mouseY):
    if (centerX - width <= mouseX <= centerX + width) and (centerY - height <= mouseY <= centerY + height):
        return True
    return False
