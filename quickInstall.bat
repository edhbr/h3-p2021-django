virtualenv . -p python && "Scripts/activate.bat"
echo "Virtualenv installed"
pip install -r requirements.txt
echo "PIP dependencies installed"
mv settings.sample.ini settings.ini
mv db.sample.sqlite3 db.sqlite3
python manage.py collectstatic --no-input
echo ""
echo "Install done"
echo ""
echo "Edit settings.ini with your values"
echo "$ vim settings.ini"
echo ""
echo "Run server with :"
echo "$ python manage.py runserver"
echo ""
pause