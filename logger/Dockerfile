FROM python:3.9-slim

WORKDIR /app

COPY logger.py .

# Set default environment variables
ENV DURATION_MINUTES=20
ENV LOGS_PER_MINUTE=2
ENV LOG_DIRECTORY=/logs

# Create the log directory
RUN mkdir -p ${LOG_DIRECTORY}

# Define a volume for logs
VOLUME ${LOG_DIRECTORY}

CMD ["python", "logger.py"]
