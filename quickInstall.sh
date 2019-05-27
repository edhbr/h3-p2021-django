virtualenv . -p python

echo "Windows (win) or Linux/Mac (lin): "
read os
if [ $os -eq "win"];
then
"Scripts/activate.bat"
else
source bin/activate
fi
pip install -r requirements.txt
mv settings.sample.ini settings.ini
mv db.sample.sqlite3 db.sqlite3
python manage.py collectstatic --no-input
echo "Install done"
echo ""
echo "Edit settings.ini with your values"
echo "$ vim settings.ini"
echo ""
echo "Run server with :"
read "$ python manage.py runserver"
echo ""
read "Press enter to quit"