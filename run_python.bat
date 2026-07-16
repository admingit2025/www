@echo off
call "d:\ProgramData\miniconda3\Scripts\activate.bat" "d:\ProgramData\miniconda3\envs\pyqt5"
python --version
python -c "print('hi')"
python "d:\git2\www\dedup_vcf.py"
