@echo off
set /P commitMessage= Enter your commit message here:
call git.exe add --all
call git.exe commit -m "%commitMessage%"
call git.exe push
