@echo off

start cmd /k "py -3.12 duplicate.py & timeout /t 1 & exit"

@echo on