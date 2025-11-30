# 1. Base Image: Use an official Python runtime
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first (for caching)
COPY requirements.txt .

# 4. Install dependencies
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Command to run the application
CMD ["python", "main.py"]
