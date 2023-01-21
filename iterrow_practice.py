import pandas as pd

# Exercise 1: Create a dataframe that contains information about different cars (e.g. make, model, year, color).
# Use iterrows() to create a dictionary that maps the make of the car to the model.
car_df = pd.DataFrame({'make': ['Toyota', 'Ford', 'Honda'], 'model': ['Camry', 'Mustang', 'Civic'], 'year': [2020, 2019, 2018], 'color': ['white', 'red', 'black']})

# Use iterrows() to create a dictionary that maps the make of the car to the model
# ...
car_and_model = {data.make: data.model for (_, data) in car_df.iterrows()}

# print(car_and_model)
# Exercise 2: Create a dataframe that contains information about different employees (e.g. name, salary, department).
# Use iterrows() to create a dictionary that maps the department to the average salary of its employees.
employee_df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'salary': [50000, 60000, 70000], 'department': ['IT', 'Finance', 'HR']})

# Use iterrows() to create a dictionary that maps the department to the average salary of its employees
# ...
salary_dict = {data.department:data.salary for _,data in employee_df.iterrows()}

# print(salary_dict)
# Exercise 3: Create a dataframe that contains information about different fruits (e.g. name, price, quantity in stock).
# Use iterrows() to create a list of dictionaries that contain the name, price, and the total value of each fruit.
fruit_df = pd.DataFrame({'name': ['Apple', 'Banana', 'Orange'], 'price': [1.5, 0.5, 2], 'quantity': [20, 30, 10]})

# Use iterrows() to create a list of dictionaries that contain the name, price, and total value of each fruit
# ...
fruit_dict = [{"name": data.name, "price": data.price, "total": data.price * data.quantity} for _,data in fruit_df.iterrows()]

# Exercise 4: Create a dataframe that contains information about different books (e.g. title, author, genre, rating).
# Use iterrows() to create a dictionary that maps the genre to the highest-rated book of that genre.
book_df = pd.DataFrame({'title': ['Harry Potter', 'The Hunger Games', 'To Kill a Mockingbird', 'The Lord of the Rings', 'The Hobbit', 'The Catcher in the Rye'], 'author': ['J.K. Rowling', 'Suzanne Collins', 'Harper Lee', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.D. Salinger'], 'genre': ['Fantasy', 'Dystopian', 'Novel', 'Fantasy', 'Fantasy', 'Novel'], 'rating': [4.8, 4.5, 4.7, 4.9, 4.7, 4.5]})

# Use iterrows() to create a dictionary that maps the genre to the highest-rated book of that genre
# create a dictionary that has  a list of books from just one genre
# dictionary of books organized by genre

# titles = [title for title in book_df.title if (book_df[book_df.genre==data.genre]["title"]==title) ]

books_by_genre = {data.genre: {"title":book_df[book_df.genre==data.genre].title.to_list(), "rating":book_df[book_df.rating==data.rating].rating.to_list()} for _,data in book_df.iterrows()}

hrb = {genre:title for genre,title,rating in books_by_genre if book_df[book_df.rating ==books_by_genre[genre][rating]]["title"] == title}

print(books_by_genre)

highest_rated_books = {data.genre: data.title for _,data in book_df.iterrows() if data.rating == book_df.rating.max()}
# highest_rated_books = {data[] for _,data in book_df.iterrows()}


# Exercise 5: Create a dataframe that contains information about different movies (e.g. title, director, release year, box office revenue).
# Use iterrows() to create a list of dictionaries that contain the title, release year, and revenue of all the movies that were released before 2010.
movie_df = pd.DataFrame({'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight'], 'director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan'], 'release_year': [1994, 1972, 2008], 'box_office_revenue': [28341469, 134821952, 533404752]})

# Use iterrows() to create a list of dictionaries that contain the title, release year, and revenue of all the movies that were released before 2010
# ...
