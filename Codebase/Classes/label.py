
class Label:
    #Class initialisation
    def __init__(self,Title='',Color=None) -> None:
        self.Title=Title                    #Set the Title of the Label
        self.Color=Color
    #Label Representation
    def __repr__(self) -> str:
        return f'Label({self.Title},{self.Color})'
    
    def __str__(self) -> str:
        return f'Label {self.Title} Color {self.Color}'