from priority import Priority

class task:
    def __init__(self, TaskTitle, TaskDesc=None, priority=None, DueDate=None, Labels=None): #initializes the class
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.DueDate=DueDate
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its priority
        else:
            self.priority=Priority(10)                  #If not, then set it to a default value of 10
            #Line for error log

        if Labels==None: #checks if any labels are selected
            self.Labels=[] #makes it an empty list instead of None
        else: 
            self.Labels=list(Labels) #makes a list of the selected labels

    def set_label(self,new_label):
        if new_label in self.Labels: #checks if the label is already selected
            self.Labels.remove(new_label) #removes the label if it is already selected
        else: 
            self.Labels.append(new_label)  #adds the label if it isnt selected

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority},{self.DueDate},{self.Labels})" 
        #repr returns how to create the task

    