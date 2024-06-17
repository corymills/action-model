FROM alpine:latest

# Install system dependencies
RUN apk add --no-cache \
    curl \
    gcc \
    libressl-dev \
    musl-dev \
    libffi-dev \
    make \
    python3 \
    python3-dev

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install Python dependencies with Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only code

# Copy the application code
COPY . .

# Run the application
CMD ["uvicorn", "src.code_executor.code_executor:app", "--host", "0.0.0.0", "--port", "80"]