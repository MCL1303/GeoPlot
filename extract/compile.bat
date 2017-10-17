@echo off

python ..\python\compile\Compiler.py prims\%1 %~n1.proto ..\python\geometry\%~n1.py
