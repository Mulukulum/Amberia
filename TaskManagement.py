

class Task:
    def __init__(self, prio, date, time=None, labels=None, tasks=None, notes=None):
        self.priority = prio
        self.duedate = date
        self.duetime = time
        self.labels = labels
        self.notes = notes
        self.tasks = tasks

    def __str__(self):
        return 'Task with priority ' + str(self.priority) + '\n'\
                'Due on ' + self.duedate

class Section:
    def __init__(self, name, project=None, tasks=[]):
        self.name = name                 #Initialize name of section
        self.project = project
        self.tasks = tasks               #Initialize a list of tasks

    def set_project(self, newproject):   #Set the project to which the section belongs
        self.project = newproject         

    def add_task(self, newtask):         #Add a new task to the section
        self.tasks.append(newtask)

    def remove_task(self, deltask):      #Remove a task from the list of tasks
        self.tasks.remove(deltask)

    def display_tasks(self):             #Display the list of tasks
        for t in self.tasks:
            print(t)

    def __repr__(self):
        return f"Section({self.name},{self.project},{self.tasks})"

    def __str__(self):
        return 'Section name: ' + self.name + '\nProject name: ' + self.project.name + \
               '\nTasks: ' + str([str(t) for t in self.tasks])


class Project:
    def __init__(self, name, color, projects = [], parentprojects = []):
        self.name = name                 #Initialize name of project
        self.color = color               #Initialize display color
        self.sections = []               #Initialize list of sections
        defaultsection = Section("_projectname")
        defaultsection.set_project(self)
        self.sections.append(defaultsection)
        self.subprojects = projects           #Initialize list of sub projects 
        self.parentprojects = parentprojects  #Initialize list of parent projects 

    def set_name(self, name):                 #Set name of project
        self.name = name

    def set_color(self, color):
        self.color = color

    def add_section(self, newsection):
        self.sections.append(newsection)

    def remove_section(self, delsection):
        self.sections.remove(delsection)

    def add_project(self, newproject):
        self.subprojects.append(newproject)

    def remove_project(self, delproject):
        self.subprojects.remove(delproject)

    def add_parentproject(self, newparent):
        self.parentprojects.append(newparent)

    def remove_parentproject(self, delparent):
        self.parentprojects.remove(delparent)

    def display_sections(self):
        for s in self.sections:
            print(s)

    def display_projects(self):
        for p in self.subprojects:
            print(p)

    def display_parentprojects(self):
        for p in self.parentprojects:
            print(p)

    def __str__(self):
        return 'Project name: ' + self.name + \
               'Display color: ' + self.color + \
               'Sections: ' + str([str(s) for s in self.sections])

    def __repr__(self):
        return f"Project({self.name},{self.color},{self.sections},{self.subprojects},{self.parentprojects})"


T1 = Task(1, "2022-10-24", "0530")
T2 = Task(2, "2022-10-25", "0930")
print(T1)

print('-----------------')


P1 = Project("Math", "Blue")
P2 = Project("Science", "Red")
P1.add_parentproject(P2)

S1 = Section("Geometry")
S1.set_project(P1)
S1.add_task(T1)
S1.add_task(T2)

print(S1)

print('-----------------')

P1. add_section(S1)
print(P1)

S1.display_tasks()