@echo off

set "out_file=%~dp0\models\%~n1.json"
python %~dp0\build.py < %1 > %out_file% || del %out_file%
