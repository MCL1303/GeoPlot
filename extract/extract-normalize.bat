@echo off

if not defined tomita for %%i in (tomitaparser tomita-win32 tomita-win64) do where /Q %%i && set tomita="%%i"&& goto :breakp
:breakp
if [%tomita%]==[] (
	echo Error: tomita parser not found!
	exit /b 1
)

set "last_dir=%cd%"

cd "%~dp0"
%tomita% config\config.proto < %last_dir%\%1 | python normalize.py > ..\test\data\facts\%~n1.xml

cd "%last_dir%"
