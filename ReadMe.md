# Fullstack Nanodegree P5 - Linux Server Configuration
```
This README file documents how a virtual Linux server instance running on Amazon
AWS was configured to deploy a data driven, Python based web application.  
This web application is the Sports Item Catalog app that was implemented by me  
as part of Project P3 for this Fullstack Nanodegree (albeit with some changes).  
The server setup process included securing server from common attack vectors,
configuring Firewall to allow specific incoming remote connections such as SSH,
installing and configuring PostgreSQL database server, installing and 
configuring Apache2 web server to serve a Python mod_wsgi web application.

```
## IP Address of Server instance:  
**52.37.244.171**
## Port for SSH access:  
**2200**
## URL of 'Sports Item Catalog' Web Application:  
**http://ec2-52-37-244-171.us-west-2.compute.amazonaws.com/**

## Summary of Software installed:
First, updated the list of available packages and their versions:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get update*  
Next, upgraded to newer versions of the packages currently installed:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get upgrade*  
Then, installed the following software on the server:  
**1. Apache web server**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install apache2*  
**2. mod_wsgi Apache module**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install libapache2-mod-wsgi*  
**3. Flask Python mini web framework**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install python-flask*  
**4. PostgreSQL DBMS, Python database adapter, SQLAlchemy toolkit and ORM**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install postgresql*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install python-psycopg2*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install python-sqlalchemy*  
**5. pip Python Package Manager**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install python-pip*  
**6. OAuth 2.0 Client library**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pip install oauth2client*  
**7. Git version control system**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo apt-get install git*  
**8. Sports Catalog App**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cloned my [Sports Catalog App](https://github.com/ashokkris/Catalog-Flask-App/blob/master/catalog/ReadMe.md) from Github  

## Summary of configurations made:  
1. Created two new users named 'grader' and 'dbadmin' with strong passwords  
2. Gave *sudo* permissions to both these users by adding them to sudoers  
3. To give remote SSH access to user 'grader', created a new private/public  
rsa key pair on my Windows PC and copied the public key contents  
to */home/grader/.ssh/authorized_keys* on the server.  
4. Edited OpenSSH server configuration file, */etc/ssh/sshd_config*, to:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Disable password based login (*PasswordAuthentication no*)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Change SSH port from 22 to 2200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Disable logging in as 'root' (*PermitRootLogin no*)  
and restarted SSH service (*sudo service ssh restart*)  
5. Configured and turned on 'Uncomplicated Firewall' (*ufw*) to allow incoming  
connections only for SSH (port 2200), HTTP (port 80) and NTP (port 123)  
(all other incoming connections are disabled)  
6. Configured local time zone to UTC by running:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo dpkg-reconfigure tzdata*  
7. Cloned my Sports Catalog Item project from Github under */var/www/catalog/* directory  
8. Gave Apache process user write access to */var/www/catalog/* to allow users of  
our app to upload image files for catalog items (by configuring a new group):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo groupadd catgroup*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo usermod -a -G catgroup www-data*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo chown -vR :catgroup /var/www/catalog/*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo chmod -vR g+w /var/www/catalog*  
9. Configured PostgreSQL DBMS:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Set password for 'postgres' role  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Edited */etc/postgresql/9.3/main/pg_hba.conf* to change the  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication method from peer to md5 for role 'postgres' and restarted database server  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Created new database user (role) named 'dbadmin' with database creation privilege:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo -u postgres createuser -d -P dbadmin*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Created new database user (role) named 'catalog' with limited privileges:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo -u postgres createuser -D -P catalog*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Created new database named 'catalog' with 'dbadmin' as its owner  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo -u dbadmin createdb -O dbadmin catalog*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Populated catalog database with some sports items  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*cd /var/www/catalog/catalog; python database_populate.py*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Granted privileges to postgresql user named 'catalog' to perform only the required CRUD  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operations when the 'catalog' database is accessed from the web application:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*REVOKE CONNECT ON DATABASE catalog FROM PUBLIC;*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*GRANT CONNECT ON DATABASE catalog TO catalog;*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public;*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TO catalog;*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO catalog;*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Restarted database server  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo /etc/init.d/postgresql restart*  
10. Configured Apache server:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Enabled wsgi module  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo a2enmod wsgi*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Configured wsgi to serve up my Sports Catalog appplication from the default web server URL:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo nano /etc/apache2/sites-available/000-default.conf*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) Set the ServerName directive to *ec2-52-37-244-171.us-west-2.compute.amazonaws.com*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Added *WSGIScriptAlias* directive inside the *<VirtualHost *:80> block and set to  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*/var/www/catalog/catalog.wsgi*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) Added *Directory* directive and entered rules to control access to our web app's resources  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d) Added *DirectoryMatch* directive to make *.git* directory web inaccessible  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Restarted apache after saving the above configuration chnages  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*sudo service apache2 restart*  
11. Configured Oauth2 credentials to add URL of Catalog web app to JavaScript origins for my  
'Sports Catalog App' project at [Google developer's console](https://console.developers.google.com)

## Third party resources referenced:  
[How To Add and Delete Users](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-an-ubuntu-14-04-vps)  
[AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)  
[apt get install vs pip install](http://askubuntu.com/questions/431780/apt-get-install-vs-pip-install)    
[SSH key authentication](https://wiki.archlinux.org/index.php/SSH_keys)  
[Setting timezone from terminal](http://askubuntu.com/questions/323131/setting-timezone-from-terminal/323163)  
[How To Install and Use PostgreSQL on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)  
[How To Secure PostgreSQL on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps)  
[GRANT - Define access privileges in PostgreSQL](https://www.postgresql.org/docs/8.1/static/sql-grant.html)  
[The pg_hba.conf File](https://www.postgresql.org/docs/9.1/static/auth-pg-hba-conf.html)  
[Apache Documentation](https://httpd.apache.org/docs/2.2/configuring.html)  
[How To Deploy a Flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)  
[Setting up a web-server for flask-app deployment in mod_wsgi](https://subhoworld.wordpress.com/2014/10/11/setting-up-a-web-server-for-flask-app-deployment-in-mod_wsgi-part-2/)  
.... and, of course, looked up many posts at stackoverflow.com










