from button import Button

class SelectableButton(Button):
    
    group = None
    selected = False
    default = False
    
    onSelect = None
    onDeselect = None
    selectedColor = None
    selectedTextColor = None
    
    _siblings = None
    _originalColor = None
    _originalTextColor = None
    
    def setup(self):
        self._originalColor = self.color
        self._originalTextColor = self.textColor
    
        self._siblings = []
    
        if self.default:
            self.select()
    
    # Find siblings after loading modules
    def afterLoadModules(self):
        siblings = self.app.getModulesByType(SelectableButton)
        
        for sibling in siblings:
            sameParent = sibling.getTopLevelParent() is self.getTopLevelParent()
            
            if sibling.group == self.group and not (sibling is self) and sameParent:
                self._siblings.append(sibling)
        
    # Selects the button
    def select(self):
        for sibling in self._siblings:
            sibling.deselect()
            
        self.selected = True
        
        if self.selectedColor != None: 
            self.color = self.selectedColor
            
        if self.selectedTextColor != None: 
            self.textColor = self.selectedTextColor
        
        if self.onSelect != None:
            self.onSelect()
    
    # Deselects the button
    def deselect(self):
        self.selected = False
        
        if self.selectedColor != None: 
            self.color = self._originalColor
            
        if self.selectedTextColor != None: 
            self.textColor = self._originalTextColor
        
        if self.onDeselect != None:
            self.onDeselect()
    
    def callback(self):
        if len(self._siblings) > 0:
            self.select()
        else:
            if self.selected:
                self.deselect()
            else:
                self.select()
        
