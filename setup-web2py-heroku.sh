read -p "Choose your admin password?" passwd
sudo pip install virtualenv
virtualenv venv --distribute
source venv/bin/activate
sudo pip install psycopg2
echo "web: python web2py.py -a '$passwd' -i 0.0.0.0 -p \$PORT" > Procfile
git init
git add .
git add Procfile
git commit -a -m "Initial Commit"
read -p "Choose your project name?" pname
heroku create $pname
git push heroku master
