@echo off

set "out_file=%~dp0\pictures\%~n1.png"
python %~dp0\draw.py < %1 > %out_file%