import PySimpleGUI as sg

layouts = {
    "main":[],
    "sel"
}

layouts["main"] = [
    # Row 1
    [
        sg.Text("Hello world!")
    ],
    # Row 2
    [
        sg.Button("OK", key="okButton")
    ]
]

mainWindow = sg.Window("Test", layouts["main"])

# Main loop
while True:
    winEvent, winEventValues = mainWindow.read()

    # Event handling
    if winEvent == sg.WIN_CLOSED:
        print("App terminated, close button.")
        break

    if winEvent == "okButton":
        print("App terminated, button click.")
        break

# End app
mainWindow.close()