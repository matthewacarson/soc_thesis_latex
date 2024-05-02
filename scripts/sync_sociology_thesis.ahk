#SingleInstance Force
#Persistent

Run, auto_commit.bat, , Hide

SetTimer, SyncSociologyThesis, 300000
return

SyncSociologyThesis:
RunWait, auto_commit.bat, , Hide
return

