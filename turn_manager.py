import ui
from module import Module
from button import Button

class TurnManager(Module):
    
    currentPlayer = None
    
    def getHandle(self):
        return 'turnManager'    
        
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        self.currentPlayer = playerManager.getPlayer(0)
        
    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        playerImage = imageLoader.get('pion-' + str(self.currentPlayer.index + 1))
        
        # Set styling
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_XL)
        textAlign(LEFT)
        
        # Draw UI elements
        text('Huidige beurt', ui.SPACING_SM, ui.SPACING_MD)
        image(playerImage, ui.SPACING_SM + 150 + ui.SPACING_SM, ui.SPACING_MD + ui.SPACING_SM, 50, 50)
            
    def nextPlayer(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        players = playerManager.getPlayers()
        
        # Find new index
        currentIndex = 0 if self.currentPlayer == None else players.index(self.currentPlayer)
        nextIndex = currentIndex + 1
        
        # Reset index if max players exceeded
        if nextIndex >= len(players):
            nextIndex = 0
            
        # Set new current player
        self.currentPlayer = playerManager.getPlayer(nextIndex)
        
        # Handle bot turn
        if self.currentPlayer is playerManager.botPlayer:
            botManager.handleBotTurn()
            
            if not botManager.breakPoint:
                self.nextPlayer()
            
    def isBotPlaying(self):
        botManager = self.app.getModule('botManager')
        return self.currentPlayer != None and self.currentPlayer.isBot() and not botManager.breakPoint
        
    def getSubModules(self):
        modules = []
        turnManager = self.app.getModule('turnManager')
        
        modules.append([Button, {
            'x': ui.SPACING_SM,
            'y': ui.SPACING_MD + ui.SPACING_SM,
            'width': 150,
            'height': 50,
            'textSize': ui.TEXT_SIZE_MD,  
            'text': 'Volgende',
            'callback': turnManager.nextPlayer,
            'disabled': self.isBotPlaying
        }])
        
        return modules
