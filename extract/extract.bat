@echo off

set all=0
set norm=0

:while
if "%1" neq "" (
    if "%1" equ "-a" ( set all=1
    ) else (
        if "%1" equ "-n" ( set norm=1
        ) else (
            if "%1" neq "-na" if "%1" neq "-an" ( break
            ) else (
                set norm=1
                set all=1
            )
        )
    )
    shift
    goto :while
)

set cmd=

for %%i in (tomitaparser,tomita-win32,tomita-win64) do (
    where /q %%i && (
        set cmd=%%i
        break
    )
)

if "%cmd%" equ "" (
    echo File or tomita parser not found
    exit 1
)

set range=
if %all% equ 1 ( set range=(*)
) else ( set range=(%1) )

for %%i in %range% do
    %cmd% config.proto < ..\test\data\input\%%i > ..\test\data\intermediate_output\%%~ni.xml

if %norm% equ 1
    for %%i in %range% do
        python ..\python\normalize.py ..\test\data\intermediate_output\%%~ni.xml
