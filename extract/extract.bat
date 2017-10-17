@echo off

tomitaparser config.proto < ..\test\data\input\%1 > ..\test\data\intermediate_output\%~n1.xml
