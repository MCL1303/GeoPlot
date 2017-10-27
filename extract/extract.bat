@echo off
setlocal EnableDelayedExpansion

where /q python3 && python3 extract.py %* || where /q python && (
	for /F "tokens=* USEBACKQ" %%F in (`python --version`) do set ver=%%F
	set ver=!ver:~7,1!
	if "!ver!" neq "3" (
		echo Wrong python version ^(!ver!, requested: 3^)^!
		exit /b 5
	)
	python %~p0\extract.py %*
)
