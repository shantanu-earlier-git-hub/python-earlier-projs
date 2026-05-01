# Use an official Python runtime as a parent image
FROM python:3.13.2

# Set the working directory in the container
WORKDIR /proj1

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .


# Command to run the application
CMD ["python","proj1.py"]
