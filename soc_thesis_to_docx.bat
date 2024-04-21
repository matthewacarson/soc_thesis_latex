REM @echo off
REM Change directory to where the .tex file is located
cd C:\Users\madou\soc_thesis_latex

REM Run Pandoc to convert .tex to .docx
pandoc soc_honors_thesis.tex -o soc_honors_thesis.docx

REM Pause to keep the command window open
pause
