# BooksAPI
Books API for CRUD operations

# Requirements

 - Interpreter = Python 3.7  
 - Frameworks = Django(2.2.2), Django Rest Frame Work(3.9.4)
 - Libraries = django-mysql(3.2),requests(2.22) , coverage(4.5.3)
 - Database = MySQL
 - IDE = Pydev (Eclipse)

  
# Code Setup
  Install above mentioned libraries as below i.e

     pip install django
     pip install djangorestramework
     pip install django-mysql
     pip install requests
     pip install coverage

  Configure Eclipse with Pydev.
  Clone the code and import into Pydev
  
 # DB Setup

 - Install MySQL 
 - Create a schema booksdb    
 - In settings.py change the database username and password to your db credentials.

   
 # Run Configurations
  Before Running, make the database miration  i.e 

    manage.py migrate 

  
  Once changes are migrated, run the application in local (default port 8000)
  
  
  # API
  
  Get book details from Ice and Fire API

      GET: http://localhost:<port>/api/external-books?name=:bookname

  
  Get a particular book details from DB by passing id

      GET : http://localhost:<port>/api/v1/books/:id

  
  Get list of all books from DB

      GET : http://localhost:<port>/api/v1/books

  
  Create a book

      POST : http://localhost:<port>/api/v1/books

  Sample Data format:

    {
        "name": "A Game of Thrones",
        "isbn": "978-0553103540",
        "authors": [
            "George R. R. Martin"
        ],
        "country": "United States",
        "number_of_pages": 694,
        "publisher": "Bantam Books",
        "release_date": "1996-08-01"
    }

  
  Update a book of a particular id

      PATCH: http://localhost:<port>/api/v1/books/:id

    
  Any following form data to be used:
       

 - name
 - isbn
 - authors
 - country
 - number_of_pages
 - publisher
 - release_date

        
  Delete a book of a particular id:

      DELETE: http://localhost:<port>/api/v1/books/:id
