@echo off

tomitaparser config.proto < ..\test\data\input\%1 > ..\test\data\output\%~n1.xml
