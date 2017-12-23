# Food Zone
This app can help the owners of the restaurant make their menu items go live among the customers.
Owners can manage their Restaurat name and edit the menu items in every way to present it best to their customers.

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
8. Use the command `python manage.py runserver` to run the app
9. Open your browser and go to `localhost:9000` to start using the Food Zone app.
10. Enjoy!