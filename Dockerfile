FROM python:3.9

WORKDIR /app

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli \
    ffmpeg \
    libsm6 \
    libxext6 \
    unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the entrypoint
ENTRYPOINT ["python", "app.py"]
