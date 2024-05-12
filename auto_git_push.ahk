#Persistent
#SingleInstance Force

; MsgBox %1%
gitInterval := A_Args[1]
; MsgBox % gitInterval

; If gitInterval is not set, set a default value
If (gitInterval < 1000)
    ;~ gitInterval := 60000  ; Default interval of 1 minute
	MsgBox Set a time interval of at least one second`, mothafucka.

Sleep, 30 * 1000

gosub, PushGit

SetTimer, PushGit, %gitInterval%
return

PushGit:
    RunWait, git push,, Hide
return
