class task:
    def __init__(self, task_title, task_desc=None, priority=None, due_date=None, labels=None):
        self.task_title=task_title
        self.task_desc=task_desc
        self.priority=priority
        self.due_date=due_date
        if labels==None:
            self.labels=[]
        else:
            self.labels=[labels]

    def set_label(self,new_label):
        if new_label in self.labels:
            self.labels.remove(new_label)
        else:
            self.labels.append(new_label) 