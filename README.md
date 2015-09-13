# Event Manager(evm)
A web application for GDG Events management based on Django Framework. 

## Instructions to setup the project on local machine

Setting up the project on your local machine is very easy. Just three step installation after cloning the repository. 

1. Create virtual environment by using following command: 
    
        virtualenv env

2. If you dont have virtualenv the install using the command 
    
        pip install virtualenv
    
3. Run the virtaulenv by 

        source env/bin/activate
    
4. Install the dependencies using the command: 

        pip install -r requirements.txt
    
5. Run migrations using the command: 

        python manage.py migrate
    
6. Run the development server: 

        python manage.py runserver

Note: make sure your 8000 port is free. If not, then use the following command: 

    python manage.py runserver port_number

Finally open http://127.0.0.1:8000(default) or http://127.0.0.1:port_number to see the magic into action. 

If you want to contribute to this project, then simply:

    * Fork the repository
    * Clone on your machine 
    * Make changes
    * Send Pull requests
