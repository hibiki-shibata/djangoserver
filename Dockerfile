FROM python:3.14
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory inside the container
WORKDIR /app
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr - it will log in VM in real time
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip3 install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
COPY . /app/
 
# Expose the Django port
EXPOSE 8000
 
# Run Django’s development server
CMD ["gunicorn", "drfBackend.manage.py", "runserver", "0.0.0.0:8000"]

# FOR PRODUCTION
# CMD ["gunicorn", "drfBackend..wsgi:application", "--bind", "0.0.0.0:8000"]