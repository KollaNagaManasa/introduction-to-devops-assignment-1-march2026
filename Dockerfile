# Use official Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install flask

# Expose application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]