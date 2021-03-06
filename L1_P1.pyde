from app import App
from modules import modules as moduleList

# App instance
app = None

# Bootstrap
# ==========================================================

def setup():
    global app
    
    # Configure program
    size(1200, 650)
    
    # Create app
    app = App()
    
    # Register modules inside App
    for module in moduleList:
        app.registerModule(module[0], module[1])
        
    for module in app.modules:
        module.afterLoadModules()
    
def draw():
    imageLoader = app.getModule('imageLoader')
    
    # Default background
    image(imageLoader.get('background'), 0 , 0 , width, height)
    
    # Draw modules
    for module in app.modules:
        if module.getIsActive(): module.draw()
    
def mousePressed():
    for module in app.modules: 
        if module.getIsActive(): module.mousePressed()
    
def keyPressed():
    for module in app.modules: 
        if module.getIsActive(): module.keyPressed()
    
def keyReleased():
    for module in app.modules: 
        if module.getIsActive(): module.keyReleased()
        
def mouseMoved():
    for module in app.modules: 
        if module.getIsActive(): module.mouseMoved()
