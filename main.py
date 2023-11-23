import PySimpleGUI as sg
from video import *
from libs import *

layouts = {
    "main":[]
}

layouts["main"] = [
    # Row 1
    [
        sg.Text("Please type the link for a Youtube video below")
    ],
    # Row 2
    [
        sg.In("Video URL", key="--VIDURL--")
    ],
    # Row 3
    [
        sg.Radio("Video and Audio", "TYPERAD", default=True, key="--RADTYP1--"),
        sg.Radio("Audio only", "TYPERAD", default=False, key="--RADTYP2--")
    ],
    # Row 4
    [
        sg.Radio("Best quality", "QUALITYRAD", default=True, key="--RADQUA1--"),
        sg.Radio("Best size", "QUALITYRAD", default=False, key="--RADQUA2--"),
        sg.Radio("Balanced", "QUALITYRAD", default=False, key="--RADQUA3--")
    ],
    # Row 5
    [
        sg.Button("Download", key="--DOWNBUT--")
    ]
]

if saveLocation == "":
    newSaveLocation = sg.popup_get_folder("It seems like you didn't set a save folder, select where to save your downloads.", "No save folder set")
    if newSaveLocation == None or newSaveLocation == "":
        quit()
    setSaveLocation(newSaveLocation)
    print(saveLocation)

mainWindow = sg.Window("Youtube Video Downloader", layouts["main"])

# Main loop
while True:
    winEvent, winEventValues = mainWindow.read()

    # Event handling
    if winEvent == sg.WIN_CLOSED:
        print("App terminated, close button.")
        break

    if winEvent == "--DOWNBUT--":
        urlToDownload = winEventValues["--VIDURL--"]
        print("Video URL: " + urlToDownload)
        if winEventValues["--RADTYP1--"] == True:
            print("Type: Video and Audio")
            if winEventValues["--RADQUA1--"] == True:
                download(downVideoFormat, urlToDownload)
        
        print("Downloading process complete")
        break

# End app
mainWindow.close()