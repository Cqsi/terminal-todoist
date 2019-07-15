# Terminal Todoist v1.0
![erminal Todoist](https://github.com/Cqsi/terminal-todoist/blob/master/Pictures/terminal_todoist.jpg)
## **Info**
Todoist is an app where you organize yourself by setting up projects and tasks. They are easy to access on their website, both on phone (app) and computer, but since some of us really live in the terminal, I thought it would be cool to code a program which enables you to get and edit your tasks and projects in the terminal (Command Prompt). This is currently only working on Windows, and I'm probably not going to add macOS or Linux support in the future.

## What commands are there?
You access this program by starting your command with **todo**. Then there are three base commands: <br/>
* **get** - gets all the projects and its tasks and prints it neatly into the terminal (so `todo get` will do that)
* **create** - create either a project or task (the next step in the command is where you choose)
* **remove** - remove either a project or task (the next step in the command is where you choose)

In the next step of the command you choose between **project** and **task**. So if you for example want to create a project you're going to do `todo create project`, BUT you still need to put the name of the project.

**Commands:**
* `todo get` - gets all the projects and its tasks and prints it neatly into the terminal

* `todo create project <name of your project>` - creates a project with given name
* `todo create tasks <name of your task> <name of the project you want to put in>` - creates a task with given name and puts it into the project with the name you entered

* `todo remove project <name of project>` - removes project with given name
* `todo remove task <name of task>` - removes task with given name

## Installation help

This guide provides help on how to set up the projects.

To get the project, simply run<br/>
`git clone https://github.com/Cqsi/terminal-todoist`<br/>

After you have cloned the project, do:
`cd todoist`<br/>
`pip install -r requirements.txt`<br/><br/>
You need to add the GithubAutomation folder to your path variable. To do this go to<br/><br/>
`Control panel -> System -> Advanced System Settings -> Environment Variables`<br/><br/>
Then in system-variables click on the Path variable, then edit and add the path for the GithubAutomation folder. All this is done in order for you to run your `todo` command from anywhere (i.e you can be in any direcotry in CMD, it doesn't matter).
After that is done go to the create.py, rm.py and get.py files and put in your Todoist API-key. Then go to the "terminal-todoist/batch" folder and edit the todo.bat file, and put in the path for the "terminal-todoist/code" folder instead of the default path that I used, so that the Command Promppt can run the files. That should be it.