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

; Example usage
folderSize := GetFolderSize()
;~ MsgBox, The size of the folder is %folderSize% bytes.

gosub Sync

timeInterval := 15 * 60 * 1000

SetTimer, Sync, %timeInterval%
return

Sync:
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
RunWait, git add soc_honors_thesis.tex soc_honors_thesis.pdf,, Hide
RunWait, git commit -m "Auto commit",, Hide
;~ ; RunWait, git push,, Hide
return