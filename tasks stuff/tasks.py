class task:
    def __init__(self, task_title, task_desc=None, priority=None, due_date=None, labels=None): #initializes the class
        self.task_title=task_title
        self.task_desc=task_desc
        self.priority=priority
        self.due_date=due_date
        if labels==None: #checks if any labels are selected
            self.labels=[] #makes it an empty list instead of None
        else: 
            self.labels=[labels] #makes a list of the selected labels

    def set_label(self,new_label):
        if new_label in self.labels: #checks if the label is already selected
            self.labels.remove(new_label) #removes the label if it is already selected
        else: 
            self.labels.append(new_label)  #adds the label if it isnt selected

    def __repr__(self):
        return "task('{}','{}','{}',{},{},{})".format(self.task_title,self.task_desc,self.priority,self.due_date,self.labels) #repr returning how to recreate the task

    