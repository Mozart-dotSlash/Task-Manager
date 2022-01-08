
import vscode
from vscode.window import show_error_message, show_info_message, show_input_box



ext = vscode.Extension(name = "testpy", display_name = "Task Manager", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"


@ext.command(keybind="ALT+5")        
def task_m():

    res = vscode.window.show_info_message('New Task?', 'Yes', 'No')

    while res == 'Yes':
        taskname = vscode.InputBoxOptions(title='Your Task Name-')
        resp1 = show_input_box(taskname)
        if not resp1:
            vscode.window.show_warn_message('No Task Added !!')
            res = vscode.window.show_info_message('New Task?', 'Yes', 'Nah')
        else:
            show_info_message(f"Your task '{resp1}' is updated")
            res = vscode.window.show_info_message('New Task?', 'Yes', 'Nah')
    else:
        return vscode.window.show_info_message('COOl ! Keep Me Updated !')    







vscode.build(ext)
