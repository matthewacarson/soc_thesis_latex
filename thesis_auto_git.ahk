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

SetTimer, CommitFiles, %timeInterval%
return

SetTimer, PushGit, %gitInterval%
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
RunWait, git add soc_honors_thesis.tex soc_honors_thesis.pdf soc_honors_thesis.ist 1_SOC_Honors.bib thesis_auto_git.ahk .gitignore, , Hide
RunWait, git commit -m "Auto commit",, Hide
return

PushGit:
	RunWait, git push,, Hide
return