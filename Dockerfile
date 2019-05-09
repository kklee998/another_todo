# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /todo

# Copy the current directory contents into the container at /app
COPY . /todo

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run database migration
RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade

# Run app.py when the container launches
CMD ["gunicorn" ,"-b" ,"0.0.0.0:4000" ,"run:app"]
