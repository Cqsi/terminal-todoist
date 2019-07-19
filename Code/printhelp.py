def print_help():

    print("""
    Welcome to the todoist-terminal help. The commands and their explanations are printed below.
    If anything is unclear, please visit https://github.com/Cqsi/terminal-todoist and check
    the README for more help on the commands.

    * todo get - gets all the projects and its tasks and prints it neatly into the terminal

    * todo create project <name of your project> - creates a project with given name

    * todo create task <name of your task> <name of the project you want to put in> - creates 
      a task with given name and puts it into the project with the name you entered

    * todo remove project <name of project> - removes project with given name

    * todo remove task <name of task> - removes task with given name

    * todo complete <name of task> - completes task with given name

    * todo help - gives you help about commands
    """)