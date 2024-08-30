# Databases: Working with ORM

![ORM](./assets/ORM.png)

## What is an ORM?

"O.R.M." stands for **O**bject–**R**elational **M**apping. This a way to interact with your database using a language of your choice (say Python) instead of SQL.

## The good old way

The classical way would be to write a query on the server side (in your API for example) and to send it to the DB.

![good_old_way](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bqGZTkRfkpOvOvKGQ8uoVg.jpeg)

Let's take an example in MySQL:

First, you would write a query in a string or a formatted string, then you would send it to your db:

```python
from mysql.connector import MySQLConnection, Error

def query_with_fetchone():
    # Wrap the query in a try/except to avoid your server to crash
    try:
        db_config = "CONFIG HERE..." # Get the config from the database
        conn = MySQLConnection(**db_config) # Open a connection
        cursor = conn.cursor() # Create a cursor

        query = "SELECT * FROM books" # Create a SQL query
        cursor.execute(query) # Use the cursor to execute the query

        # Loop over the rows and remove them one by one
        row = cursor.fetchone() # This removes it from the cursor
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        # Handle errors
        print(e)
    finally:
        # Error or not, when it's done, close the cursor and the connection with the DB
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query_with_fetchone()
```

## Why using ORM then?

Well, this code will do the job, but here are some disadvantages:

1. As you can see you have to write a lot of code and to handle a lot of errors, to remember to close the cursor for each request, to close the connection when you are done, ...

2. You are exposed to SQL injections if you are using SQL, you have to think about security when you want to handle big queries you will have to have a really good knowledge of the query language you are using, and finally, you have to know every good practice to be sure to write something that is optimized (a bad query can take ages to run!).

3. You could send badly typed data, for example if you insert a row or replace the content of it you could send a string where the DB expects an int. In the case of a SQL database, it will return you an error (you will have to handle it) so it's not a big deal during development. But if you are working with a NoSQL database, it will just execute the query and do it. Great, no error, but when you will need to use this data that you expect to be an int and receive a string, you will have a lot of issues, unclear errors, hours of debugging your code when the problem comes from the data, ... It happens faster than you think and it's a real pain...

## What is ORM exactly?

![ORM](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*rIZsflffWOlHh7DAndYjGQ.jpeg)

Ok, now that we know we want to use something better, how do these ORM work?

1. You declare a schema for your data. Let's say that I have a `Book` table in my database and I want to have an `id` field (int and primary key), a `title` that is a string, and a `number_of_pages` which is an int. I could declare my schema like that:

```python
# Example with mongoDB and SQL alchemy
from sqlalchemy import Column, String, Integer
from base import Base

class Book(Base):# We inherit from Base
    __tablename__ = 'books' # Provide the name of the database table

    id = Column(Integer, primary_key=True) # Set an id field
    title = Column('title', String(32)) # Set a title field
    number_of_pages=Column('number_of_pages', Integer) #Set a number of pages field

    # This init method that will allow you to easily create a new entry later.
    def __init__(self, title: str, number_of_pages: int):
        self.title = title
        self.number_of_pages = number_of_pages
```

_The syntax will, of course, change depending on the ORM library you use._

2. Now that your typed data is defined you can easily add a `Book` in your database:

```python
from base import Session, engine, Base

# 1. generate database schema
Base.metadata.create_all(engine)
# 2. create a new session (a connection with the database)
session = Session()
# 3. create a new book
my_new_book = Book(title="Resilient Management", number_of_page="234")
# 4. Prepare the query and add it to the "commit" (so you can save a lot of queries and execute them all as once)
session.add(my_new_book)
# 5. execute all the operations stored and execute them as one big optimized query.
session.commit()
# 6. Close the session
session.close()
```

Ok, it's still verbose but at least everything will be secured and optimized, and you will see, it's not the only advantage.

3. You want to get all the books in the database? Super simple:

```python
from base import Session
# Create a session
session = Session()
# Create the query (can be heavily tweaked to filter only what you need)
books = session.query(Book).all()
# That's it! All your books are stored in `books`
for book in books:
    print(f{title: {book.title} number of pages: book.number_of_pages})
```

## Complex stuff

Ok, those examples were easy, but those libraries are super powerful, you can manage the relation between two tables, add conditions, auto-format fields, and SOOOOOO much more.

## Do I NEED to know ORMs?

Definitely. First, because it's amazing but mainly because a lot of libraries use it by default (Django, for example) and if you have to work with these, you will need to know how to properly use ORMs.

## Conclusion

The ORM concept is super useful and powerful, you will "lose" some time when you will have to define each schema but when it's done, you will work super fast with the conviction that you can't really do any harm to your database.

## Popular libraries to work with ORMs in Python

- MongoDB: [MongoEngine and PyMongo](https://realpython.com/introduction-to-mongodb-and-python/)
- SQL-based DB: [SQL Alchemy](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- A complete one: [Pony ORM](https://ponyorm.org/)
- Django: [Django ORM](https://docs.djangoproject.com/en/3.1/topics/db/queries/)

## Side notes

To access certain types of databases, the ORM will need a "connector"; a library to connect the ORM and the database. Depending on the database you are using, you will have to install it too. For more information about that, please read the documentation of the ORM you are using.

Some ORMs can be slower than a super well written query (we are talking here about optimization for production). But a lot of big companies use ORMs anyway, because they are already plenty fast, it's rare to need to optimize your code that much!

## Final notes

I hope you have a clear idea of what ORMs are. If not, contact your team and talk about it with them.

To properly use an ORM you will need to do more research, don't limit yourself to what is written in this README, it only shows you the basics.

ORM is amazing and will make you gain **SO** much time once you master them, believe me on this one! ;)

![Get things done](https://media.giphy.com/media/oUkLEfuYSrPOg/giphy.gif)

## Additional resources

- [Full stack Python ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [sqlalchemy documentation](https://www.sqlalchemy.org/)
- [Auth0 tutorial for sqlalchemy](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [Medium: Basics of sqlalchemy (simple, short and clear)](https://medium.com/@haataa/orm-for-python-sqlalchemy-101-with-code-example-60868e65b0c)
