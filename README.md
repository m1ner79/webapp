# Webapp
A Flask-based Webapp with Jinja2.

## Requirements:
##Part 1
I need to build a multi-page webapp using Flask/Jinja2 which provides details about me, my interests, and the computing technologies I like.  
### The following pages are required:
- A home page providing links to the various sections of my website.
- A personal page providing all the usual details.
- A CV page providing details of interest to potential employers.
- A computing technologies page which has at least 3 sub-pages providing details on my favourite computing technologies.
- An interests page which provides details on your interests outside of my course and computers.

I need to provide a mechanism which lets a visitor to my site return to my home page from any other page on my site. Where necessary, provide links to external sites on the web (as needed).  

External links need to open in a new tab.  

My site is to include a small form which lets visitors post a short message. Two pieces of information should be posted: my visitors’ email address as well as their message.  

These data are to be stored on my server in a file called **comments.txt**.
##Part 2
I need to replace the text-based data storage code with code which saves visitor comments to an SQL database/table.

The webapp will display the contents of visitor information on a new page, most-recent visitor comment first.
This display should also include the date/time the comment was submitted to the website.

I need to write a series of tests to exercise new database code as well as updated webapp. 

I will use pytest to write tests, and ensure that the code coverage for the webapp and database code is 100%. 
Tests need to ensure that all the webapp URLs are tested for (at least) a 200 status code on success.

Once the webapp is working as it should, I will deploy it to PythonAnywhere remotely.