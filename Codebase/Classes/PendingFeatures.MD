**Templates:**

Template tasks and projects are a way to quickly replicate projects or tasks.

Given a set of tasks or projects, the template task/project creates a copy 
that can quickly be put into a different place

For example, say a user wishes to create a project to revise for exams
Assuming they have a section for each subject, it would be a pain to go 
and create individual tasks for stuff that would be shared between sections

In the case of exam revision, every subject is going to have 
a 'practice problems' task and a 'make a summary sheet' task and
a bunch of other similar stuff

So, to make things easier you do it ONCE and then save it as a template
And then the user should be able to add that same template somewhere else 
and avoid doing the same thing twice

Similar thing with tasks is a task template

One thing to note here is that completing a task in a template copy does not modify the template itself
They're copies, and not interlinked at all

Ideally, templates will have their own tables

**LinkerTasks: (More on this stuff at the end of [THIS](./PendingFeatures.MD)**

A subclass of tasks that hyperlinks to another set of projects/tasks

Linker tasks can link to other projects, sections or tasks. It can link to MULTIPLE of these

They have a flag used for checking if on completion of its ParentTask (i.e the task that holds the linker task), 

the stuff its linking must also be completed. The user can specify which 
particular tasks/projects/sections that it links to should be completed and which ones shouldn't be completed
on completion of the parent task

Ideally a LinkerTask will user an interfacelinkertask, which is just a linker task that links to one other thing
And that interfacelinker task holds a flag to decide if the things its linking to gets completed on completion of its parent linker task.

Note: Completing a section just refers to finishing all the tasks contained within it and deleting
Completing a project just finishes all the tasks within that project

**In order to know what recursion is you must first know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to maximum recursion depth exceeded**

Linking and projects within projects cannot be brought up without talking about
the question of recursion. 

Recursion placed its somewhere that its not designed for, is painful to think about

To avoid the user messing stuff up, we define a few rules and conventions

**For Projects:**

All projects referencing other projects will be connected using
a hyperlink object class. They're just references and one is not a subproject of another

When a user wishes to actually nest projects, we connect the 2 projs
using a LinkerObject Class with a parent project and a child project attribute
Same as before, but this DOES NOT HAVE the flag to see if on completion of the parent task/project,
the child proj should be completed. When linked with linker objects they are automatically completed. 

This doesn't really seem to solve the problem of projects potentially linking to themselves, with hyperlinks
especially when completing stuff is involved. 

Using Linker objects, an easy fix for this is to first remove/complete all the 
references to said project first, this will ensure that nothing else links to it and breaks
any possiblity of having an infinite loop

**For Tasks:**

Differentiate between subtasks and tasks that are linked using hyperlinktasks when coding

linkertasks have the flag set as I mentioned before

just ensure that when completing a task you specifically handle the hyperlink class stuff first

**Completion or Deletion**

COMPLETE != DELETE

Completion of a task/project just changes a "iscompleted" attribute on it.
(I was considering moving them to a whole other table but that seemed kind of wasteful and complicated to handle
I'll leave it upto you guys to discuss how you'd like to implement it)

This is because being able to do a quick undo for accidentally completing tasks is useful

**Other Task Related Things:**


**Task Constructor:**
Having a task constructor would be useful. User specifies just names for multiple tasks
and you get a list of them where ever the original "task constructor" task was.

Could Probably use this a lot when making templates because I can see that being useful 

**YOUR TEXT HERE**

A text task, its just that. Its a bunch of text which doesn't count for overall completion. 
It only exists to add notes to stuff.

**Again?**

Tasks should probably be able to repeat perodically
Ideally we give the user options as to how they'd like to
have the tasks repeated

Again, implementation is your discretion. 

Keep an eye on the '\#pending-features' channel, I'll ping you guys if theres anything important

You will be left with a lot of questions and probably won't understand all of it perfectly
because I suck at explaining things properly so just ask if you need help w/ something