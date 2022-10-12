

class label:
    #Class initialisation
    def __init__(self,Title='',Color=None) -> None:
        self.Title=Title                    #Set the Title of the Label
        

    #Label Representation
    def __repr__(self) -> str:
        return f'Label {self.Title}'