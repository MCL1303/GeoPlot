@echo off

where /q python3 && python3 extract.py %* || python extract.py %*
