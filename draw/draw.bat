@echo off

set "out_file=%~dp0\..\test\data\output\%~n1.png"
python %~dp0\draw.py < %1 > %out_file%
