from screen import Screen
from button import Button
from selectable_button import SelectableButton
from player_button import PlayerButton

class StartScreen(Screen):
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
    
    def setup(self):
        global img
        
        img = loadImage('logo love it.png')

    def draw(self):
        background(112,238,255)
        fill(11, 60, 73)
        
        
        textSize(25)
        textAlign(LEFT)
        text('Teams', 100, 100)
        
        textSize(25)
        textAlign(LEFT)
        text('Spelers', 100, 350)
        
        image(img, 900, 200)
            
    def setMaxToFour(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def setMaxToSix(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
       
    def startGame():
        gameScreen = self.app.getScreen('game')
        self.app.setCurrentScreen(gameScreen)
                      
    def getSubModules(self):
        playerManager = self.app.getModule('playerManager')
        
        maxToFourButton = [SelectableButton, {
            'x': 100,
            'y': 150,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': '2 teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [255, 22, 84],
            'onSelect': self.setMaxToFour,
            'default': True
        }]
        
        maxToSixButton = [SelectableButton, {
            'x': 400,
            'y': 150,
            'width': 250,
            'height': 100, 
            'textSize':(23), 
            'color': [255,74,113],
            'text': '3 Teams',
            'textColor': [11, 60, 73],
            'group': 'maxPlayers',
            'selectedColor': [255, 22, 84],
            'onSelect': self.setMaxToSix
        }]
     
        startButton = [Button, {
            'x': 250,
            'y': 800,
            'width': 250,
            'height': 100,
            'textSize':(23),  
            'color': [255,74,113],
            'text': 'START',
            'textColor': [11, 60, 73],
            'callback': self.startGame
        }]
     
        return [
            maxToFourButton,
            maxToSixButton,
            startButton,
            [ PlayerButton, { 'x': 100, 'y': 400, 'player': playerManager.getPlayer(0) } ]
        ]
