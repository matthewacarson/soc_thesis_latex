#SingleInstance Force
#Persistent

GetFolderSize() {
    totalSize := 0
    Loop, Files, ..\*, FDR
    {
        ;~ MsgBox %A_LoopFileSize%
		totalSize += A_LoopFileSize
    }
    return totalSize
}

folderSize := GetFolderSize()
;~ MsgBox, The size of the folder is %folderSize% bytes.

gosub SendCommands

timeInterval := 5 * 60 * 1000

SetTimer, SyncSlides, %timeInterval%
return

SyncSlides:
fileSizeLatest := GetFolderSize()
if(fileSizeLatest != folderSize) {
	folderSize := fileSizeLatest
	gosub, SendCommands
} else {
	Loop {
		Sleep, 60000
		fileSizeLatest := GetFolderSize()
		if(fileSizeLatest != folderSize) {
			folderSize := fileSizeLatest
			gosub, SendCommands
			break
		}
	}
}
return

SendCommands:
RunWait, git add presentation_slides.tex presentation_slides.pdf,, Hide
RunWait, git commit -m "Auto commit",, Hide
RunWait, git push,, Hide
return