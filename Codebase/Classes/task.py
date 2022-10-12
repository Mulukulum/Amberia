from priority import Priority

class task:
    def __init__(self, TaskTitle, TaskDesc=None, priority=None, DueDate=None, Labels=None): #Initializes the class
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.DueDate=DueDate
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its priority
        else:
            self.priority=Priority(10)                  #If not, then set it to a default value of 10
            #Line for error log

        if Labels==None:                                #Checks if any labels are selected
            self.Labels=[]                              #Makes it an empty list instead of None
        else: 
            self.Labels=list(Labels)                    #Makes a list of the selected labels

    def set_label(self,NewLabel):
        if NewLabel in self.Labels:                     #Checks if the label is already selected
            self.Labels.remove(NewLabel)                #Removes the label if it is already selected
        else: 
            self.Labels.append(NewLabel)                #Adds the label if it isnt selected

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
    
    def reconfigure(self,TaskTitle=None, TaskDesc=None, priority=None, DueDate=None, Labels=None):
        if TaskTitle!=None:
            self.TaskTitle=TaskTitle                    #Changes the title to a newly provided title
        if TaskDesc!=None:
            self.TaskDesc=TaskDesc                      #Changes the desc to a newly provided desc
        if DueDate!=None:
            self.DueDate=DueDate                        #Changes the due date to a newly provided due date
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its new priority
        if Labels!=None:
            self.set_label(Labels)            
    

    