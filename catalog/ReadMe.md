# Fullstack Nanodegree P3 - Item Catalog
```
catalog/   
|---- __init__.py
|---- database_setup.py    
|---- database_populate.py    
|---- catalog.py
|---- client_secret.json
|---- readme.md
|---- static/
      |---- catalog.css
      |---- body.png
      |---- top.png
      |---- content_1.png
      |---- content_2.png
|---- templates/
      |---- base.html
      |---- header.html
      |---- login.html
      |---- catalog.html
      |---- itemDetails.html
      |---- addItem.html
      |---- editItem.html
      |---- deleteItem.html
|---- uploads/
      <this folder contains item image files>
```
### Dependencies  
1. PostgreSQL 9.3 database  
2. SQLAlchemy 0.8.4 or later  
3. Flask version 0.10.1 or later  
4. Python version 2.7 or later  

### Quick Start  
1. After setting up the web app to be served up by a web server like Apache2  
on Ubuntu, launch a web browser like Chrome and enter the web app's URL:  
   For instance, http://ec2-52-37-244-171.us-west-2.compute.amazonaws.com
2. Explore the 'Sports Catalog App' by viewing the various pre-populated  
catalog items under the different sports categories  
3. Click the 'Home' link at top left to view the app's home page  
4. Click the 'Login' link and sign-in using your Google+ account  
5. Click the 'Add Item' link to add a new catalog item  
6. Fill the 'Add Item' form and click the 'Submit' button  
7. Verify that your item was successfully added to the catalog  
8. Edit the item you added by clicking on the item and then on the 'Edit' link  
    **Note**: The Edit and Delete links in 'Item Details' page appear only for  
    items that are created by you. You cannot edit/delete items created by  
    other users  
9. In the 'Edit Item' form, make changes to the item description, associated  
    image etc and 'Submit'  
10. Verify that the changes were successfully applied in the catalog  
11. Next, try deleting the item you created and verify that the item removal  
was successful  
12. Click the 'Logout' link on the title bar to sign-out out of Sports Catalog app  
13. To test the JSON endpoint, type it's URL in browser address bar:  
    For instance, http://ec2-52-37-244-171.us-west-2.compute.amazonaws.com/catalog.json  
14. To test the Atom end point, type the below in the browser's address bar:  
    For instance, http://ec2-52-37-244-171.us-west-2.compute.amazonaws.com/recent.atom  
    **Note**: You can also look for the RSS icon on your browser if it supports  
    it. If it does, notice that the RSS feed icon is enabled because our  
    Sports Catalog App website offers a RSS feed. You can click on it to  
    subscribe to that feed.  

###Documentation
* \_\__init_\_\_.py - python package initialization code
* _database_setup.py_ - python module that declares classes needed to perform  
our CRUD operations with SQLAlchemy on an Postgresql database (Model)  
* _database_populate.py_ - python module to create and populate database tables  
with sample catalog items (for use by dbadmin only)
* _catalog.py_ - python module implementing the server functionality for our  
Sports Catalog web application (Routes and Controller actions)
* _client_secret.json_ - JSON formatted file containing client ID, client secret  
and other OAuth 2.0 parameters of our Sports Catalog web application  
* _templates/_ - Folder containing the Flask html templates to render the user  
requested page (Views)
* _static/_ - Folder containing static files consumed by our web application.  
These include CSS file and other image files used to format and embellish  
our Catalog App's web pages
* _uploads/_ - Folder containing user uploaded image files that are associated  
with individual catalog items. The name of the image files are stored in  
database for file retrieval later when item details are rendered on a web page  


###Features
* Implements a JSON endpoint returning catalog contents
* Implements Atom endpoint for subscribing to RSS feed on updated content  
* Has page with form allowing logged-in user to add new items  
* Has page with form allowing logged-in user to edit item created only by that  
user  
* Has page with form allowing logged-in user to delete item created only by  
that user using POST request and nonces prevent CSRF
* Implements 3rd party authentication and authorization service. CRUD  
operations check authorization status prior to executing database modifications  


