# Use an official Python runtime as a parent image
FROM python:3.11.11

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file to the container at /app
COPY routes /app
COPY schemas /app
COPY services /app
COPY utils /app
COPY main.py /app 
COPY chart_info.json /app
COPY requirements.txt /app

# Install pip dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]