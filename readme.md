# Django Example Backend Server

To start the server, first clone the repository to your computer.
We recommend Linux platforms. Full project is on Python3 and Pip usually reffered to pip3 and can be changed as configuration of your PC.

Make sure MySQL is installed in your system. Then log into your mysql server with `$ mysql -u root -p` and enter password. If your wish to login with other username, change root to your preffered username.

In MySQL CLI, create a database with:
```
create database Django_Example_Database;
```

Next exit the console with `exit`.

Now back to the cloned repository in your PC, open the directory and initiate a new terminal in that tab.
Now turn on the virtual environment. For this, inside the project root directory your will find `venv` folder, this contains the virtual environment. From terminal with project root directory open terminal and run the command 
`$ source venv/bin/activate` and this should activate the virutal environment. And to revert back to your original environment, use '$ source ~/.bashrc' or `$source ~/.profile.d` as per configuration.

Now back in project root directory, run `python manage.py check` to check the system.
If it asks for `mysqlclient` or such errors, run following commands:
```
sudo apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient==2.0.1
```

Now rerun check command and see whether any error appears.

Now you need to configure the database and migrate changes.
For this, run:
```
python manage.py makemigrations
python manage.py migrate
```

Now it should be alright to start the server. Finally to run the server, use:
```
python manage.py runserver
```

This should start the server in http://localhost:8000 you can tweak with host and ports too.

For any clarifications, contact me directly at WhatsApp @ `+91-977-547-9892`

Subhrangshu Adhikary

B.Tech @ Dr. B.C. Roy Engineering College, Durgapur

Managing Director @ Spiraldevs Automation Industries Pvt. Ltd., Raiganj

West Bengal, India