# Food Zone
This app can help the owners of the restaurant make their menu items go live among the customers.
Owners can manage their Restaurant name and edit the menu items in every way to present it best to their customers.

## Requirements:
1. Linux based virtual machine. You can learn the installation of the virtual machine using [Vagrant](https://www.vagrantup.com/) and [Virtual box](https://www.virtualbox.org/wiki/Downloads) [here](http://www.bogotobogo.com/DevOps/Vagrant/Vagrant_VirtualBox.php).
2. Download and install [git](https://git-scm.com/downloads)

## How to run the Twitter-clone app.
1. Clone the repository in your vagrant shared folder directory.
2. Open git bash
3. Go to the directory where your **vagrantfile** exists.
4. Install the virtual machine by using the command `vagrant up`.
5. After the succesfull installation of the linux os. Run the command `vagrant ssh` to start the machine.
6. Now `cd` into the repository **Food-Zone**.
7. Activate the virtual environment by using the command `source venv/bin/activate`.
8. Open postgresql with `psql postgres` or `psql`
9. Create a database for the app by the command `CREATE DATABASE restaurant` then quit postgresql using `\q`
10. Now open python shell by using `python`
11. Use to command `from restaurant import db` to import the sqlalchemy database object.
12. Now create all the tables in the database using the command `db.create_all()` and quit python shell by `exit()`
13. Use the command `python manage.py runserver` to run the app
14. Open your browser and go to `localhost:5000` to start using the Food Zone app.
15. Enjoy!