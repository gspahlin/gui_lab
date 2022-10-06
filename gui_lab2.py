import PySimpleGUI as sg

#for this program, I want to implement a file browser that will print a file path

#layout
l_map = [
    [sg.Text('Use This to get a path'),
    sg.In(size = (25, 1), enable_events = True, key='-FOLDER-'),
    sg.FolderBrowse() 
    ],

    [sg.Button('Print')]

]

#create window
window = sg.Window('Path Grabber', l_map)

#create event loop 
while True:
    event, values = window.read()

    if event == '-FOLDER-':
        #values['-FOLDER-'] ends up being whatever is in the sg.In box
        folder = values['-FOLDER-']

    if event == 'Print':
        print(folder)


        #kill the program if the user hits the close box or 
    if event== sg.WIN_CLOSED:
        #this command breaks the loop
        break

#this command closes the Window that I've stored in the window variable
window.close()