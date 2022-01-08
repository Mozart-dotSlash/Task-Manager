
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

'''    
    res = vscode.window.show_info_message('Add New Task?', 'Yes', 'No')
    while res == 'Yes':
        taskname = vscode.InputBoxOptions(title='Your Task Name-')
        resp1 = show_input_box(taskname)                            #Task Name
        taskdate = vscode.InputBoxOptions(title='Date-')
        resp2 = show_input_box(taskdate)                            #Task Date
        tasktime = vscode.InputBoxOptions(title='Time-')
        resp3 = show_input_box(tasktime)                            #Task Time
    

        if not resp1:
            vscode.window.show_warn_message('No Task Added !!')
            res = vscode.window.show_info_message('New Task?', 'Yes', 'Nah')
        else:
            file.write(resp1 + ' ' * (20-len(resp1)) + " on " + resp2 + ' at ' + resp3 + '\n') #File Tasks is updated with a new Task
            show_info_message(f"Your taskname '{resp1}' is updated")
            res = vscode.window.show_info_message('New Task?', 'Yes', 'Nah')
    else:
        file.close()

        return vscode.window.show_info_message('COOl ! Keep Me Updated !')
'''    

@ext.command(keybind="ALT+4")
def mark_done():
    cwd = vscode.window.show_open_dialog()
    dirn = os.path.dirname(cwd[0]['path'])
    try:
         file = open(dirn+'/Tasks.txt', 'r')
         tasks = file.readlines()
         file.close()
    except:
         vscode.window.show_error_message('Tasks not added to this project !')      
    
    #Standardising text Doc
    x=1
    while x > 0:
        try:
            n=tasks.index('\n')
            tasks.pop(n)
        except:
            x=0   
    print(tasks)

    taskshow = []
    for i in range(0,len(tasks),3):
        try:
            taskshow.append(tasks[i] + tasks[i+1] + tasks[i+2])
        except:
            continue    
    

     
    for i in range(len(taskshow)):
        try:
            t = vscode.window.show_quick_pick(taskshow)
            n = taskshow.index(t)
            taskshow.pop(n)
            vscode.window.show_info_message('Task marked done and removed !')
        except:
            vscode.window.show_info_message('No Task Marked Done !')
   

    file = open(dirn+'/Tasks.txt', 'w')
    taskfinal = []
    for i in range(len(taskshow)):
         a= taskshow[i].split('\n')
         print(a)
         for j in range(3):
             taskfinal.append(a[j]+'\n')
    taskfinal.append('\n')
    for i in range(len(taskfinal)):
             file.write(taskfinal[i])
    file.close()
    
    vscode.window.show_info_message('Task List Updated !')
             
            

vscode.build(ext)

