import PySimpleGUI as sg
#create layout
layout = [
    [sg.Text('Press The Button For a Fun Time ;)')],
    [sg.Button('OOOH Mystery!')]
]

#create window
window = sg.Window('Hello Gui World', layout, resizable=True)

#create the event loop
while True:
    event, values = window.read()

    #try another case
    if event=='OOOH Mystery!':
        print('BANANA')

    #kill the program if the user hits the close box or 
    if event== sg.WIN_CLOSED:
        #this command breaks the loop
        break

#this command closes the Window that I've stored in the window variable
window.close()