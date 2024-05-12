#SingleInstance Force
#Persistent

GetFolderSize() {
    totalSize := 0
    Loop, Files, *, FDR
    {
		totalSize += A_LoopFileSize
    }
    return totalSize
}

folderSize := GetFolderSize()

gosub SendCommands

timeInterval := 3 * 60 * 1000
gitInterval := 10 * 60 * 1000

Run, auto_git_push.ahk %gitInterval%

SetTimer, CommitFiles, %timeInterval%
return

CommitFiles:
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
RunWait, git add soc_honors_thesis.tex soc_honors_thesis.pdf soc_honors_thesis.ist 1_SOC_Honors.bib auto_git.ahk auto_git_push.ahk .gitignore, , Hide
RunWait, git commit -m "Auto commit",, Hide
return


