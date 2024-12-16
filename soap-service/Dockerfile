# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 8001

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"]
