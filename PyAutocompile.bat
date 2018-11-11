@echo off
set /P fileToCompile= File to compile:
cd %cd%
call pyinstaller.exe --onefile %fileToCompile%