
class Section:
    def __init__(self, name, project=None, tasks=list()):
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
        print(*self.tasks,sep='\n')      #Displays tasks without a for loop         

    def __repr__(self):
        return f"Section({self.name},{self.project},{self.tasks})"              

    def __str__(self):
        return f'Section name: {self.name} \nProject name: {self.project.name} \nTasks: {[str(t) for t in self.tasks]}'        
        #fstring returns the string representation


class Project:
    def __init__(self, name, color=None, projects = list(), parentprojects = list()):
        self.name = name                 #Initialize name of project
        self.color = color               #Initialize display color
        self.sections = list()               #Initialize list of sections
        defaultsection = Section(f"_{self.name}")
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
        print(*self.sections,sep='\n')

    def display_projects(self):
        print(*self.subprojects,sep='\n')

    def display_parentprojects(self):
        print(*self.parentprojects,sep='\n')
          

    def __str__(self):
        return  f'Project name: {self.name} \
                \nDisplay color: {self.color} \
                \nSections: {[str(s) for s in self.sections]}'

    def __repr__(self):
        return f"Project({self.name},{self.color},{self.sections},{self.subprojects},{self.parentprojects})"

