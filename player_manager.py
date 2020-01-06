from module import Module
from player import Player

class PlayerManager(Module):
    
    # The max amount of players
    maxPlayers = None
    
    # The current bot player
    botPlayer = None
    
    # List containing all player objects
    _players = []
    _activePlayers = []
    
    def getHandle(self):
        return 'playerManager'
    
    def init(self):
        self._players = self.app.getModulesByType(Player)
        
        # Create active player list
        self.updateActiveList()
    
    # Updates the list of active players
    def updateActiveList(self):
        self._activePlayers = list(filter(lambda p: p.isPlaying(), self._players))
    
    # Sets the max amount of players
    def setMaxPlayers(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.updateActiveList()
    
    # Returns a player by its index
    def getPlayer(self, index):
        if index < 0 or index > (self.maxPlayers - 1):
            return None
        
        return self._players[index]
    
    # Returns a player by its location
    def getPlayersByLocation(self, location):
        return [ player for player in self.getPlayers() if player.getLocation() == location ]
            
        return None
    
    # Returns all active players
    def getPlayers(self):
        return self._activePlayers
    
    # Returns all players
    def getAllPlayers(self):
        return self._players
    
    def getSubModules(self):
        modules = []
        
        # Create 6 players
        for i in range(6):
            imageFile = 'pion-' + str(i + 1)
            modules.append([Player, { 'index': i, 'image': imageFile }])
            
        return modules
    
