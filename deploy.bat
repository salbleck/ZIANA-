@echo off
REM === 1. Kumpulkan semua static files ===
echo Collecting static files...
python manage.py collectstatic --noinput

REM === 2. Tambahkan semua perubahan ke git ===
echo Adding files to git...
git add .

REM === 3. Commit perubahan ===
set /p COMMIT_MSG="Enter commit message: "
git commit -m "%COMMIT_MSG%"

REM === 4. Push ke GitHub ===
echo Pushing to GitHub...
git push origin main

echo Deployment script finished!
pause
