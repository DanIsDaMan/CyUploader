@echo off
call git.exe add --all
call git.exe commit -m "Test commit with a batch file"
call git.exe push
