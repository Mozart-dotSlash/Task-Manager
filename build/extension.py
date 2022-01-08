# Built using vscode-ext

import sys

import vscode
from vscode.window import show_error_message, show_info_message, show_input_box
import os

ext = vscode.Extension(name = "testpy", display_name = "Task Manager", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"


@ext.command(keybind="ALT+5")        
def add_task(): 

    cwd = vscode.window.show_open_dialog()
    dirn = os.path.dirname(cwd[0]['path'])
    file = open(dirn+'/Tasks.txt', 'a+')
    res = vscode.window.show_info_message('Add New Task?', 'Yes', 'No')
    if res == 'Yes':
        nooftasks = vscode.InputBoxOptions('How many new tasks?')
        n= show_input_box(nooftasks) 
        for i in range(int(n)):
            file.write('\nName:\nDate(dd-mm-yyyt):\nTime(00.00hrs):\n')
        file.close()    
        vscode.window.show_text_document(dirn+'/Tasks.txt')
    else:
        return vscode.window.show_info_message('COOl ! Keep Me Updated !')   

@ext.command(keybind="ALT+4")

#This fn of the code basically shows the list of tasks in a project and can delete if any task is done 

def mark_done():
    cwd = vscode.window.show_open_dialog()
    dirn = os.path.dirname(cwd[0]['path'])
    try:
         file = open(dirn+'/Tasks.txt', 'r')
         tasks = file.readlines()
         file.close()
    except:
         vscode.window.show_error_message('Tasks not added to this project !')      
    
    #Standardising txt file
    x=1
    while x > 0:
        try:
            n=tasks.index('\n')
            tasks.pop(n)
        except:
            x=0   


    taskshow = []
    for i in range(0,len(tasks),3):
        try:
            taskshow.append(tasks[i] + tasks[i+1] + tasks[i+2])
        except:
            continue    

    # Removing the DONE task from txt file 
    for i in range(len(taskshow)):
            t = vscode.window.show_quick_pick(taskshow)
            if not t:
                vscode.window.show_info_message('No Task Marked Done !')
                break
            else:
                n = taskshow.index(t)
                taskshow.pop(n)
                vscode.window.show_info_message(t+' marked done and removed !')
 
   

    file = open(dirn+'/Tasks.txt', 'w')
    taskfinal = []
    for i in range(len(taskshow)):
         a= taskshow[i].split('\n')
         for j in range(3):
             taskfinal.append(a[j]+'\n')
         taskfinal.append('\n')

    taskfinal.append('\n')

    for i in range(len(taskfinal)):
             file.write(taskfinal[i])
    file.close()
    
    vscode.window.show_info_message('Task List Updated !')

#This fn can EDIT the tasks txt file
@ext.command(keybind="ALT+3")
def edit_task():
    edit = vscode.window.show_info_message('Wanna Edit Tasks ?', 'Yes', 'No')
    if edit == 'Yes':
        cwd = vscode.window.show_open_dialog()
        dirn = os.path.dirname(cwd[0]['path'])
        try:    
          file = open(dirn+'/Tasks.txt', 'r')
          tasks = file.readlines()
          file.close()
        except:
          return vscode.window.show_error_message('Tasks not added to this project !') 

        vscode.window.show_text_document(dirn+'/Tasks.txt') 
        stat = vscode.window.show_info_message('Done Editing ?', 'Yes')
        file = open(dirn+'/Tasks.txt', 'r')
        tasks = file.readlines()
        file.close()
        if stat == 'Yes':
            x=1
            while x > 0:
               try:
                n=tasks.index('\n')
                tasks.pop(n)
               except:
                x=0   

            taskshow = []
            for i in range(0,len(tasks),3):
               try:
                  taskshow.append(tasks[i] + tasks[i+1] + tasks[i+2])
               except:
                  continue
        vscode.window.show_info_message('Task edited !')         
        vscode.window.show_quick_pick(taskshow)

            




def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
