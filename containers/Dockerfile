FROM alpine:latest

# Install required packages
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    firefox-esr \
    wget \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    libffi-dev

# Set the working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Install Poetry within the virtual environment
RUN pip3 install poetry

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install Python dependencies with Poetry
RUN poetry install --with code

# Copy the application code
COPY /src /src 

# Run the application
CMD ["poetry", "run", "uvicorn", "src.code_executor.code_executor:app", "--host", "0.0.0.0", "--port", "80"]