# Logger Application

A simple Python-based logging application that generates timestamped log entries at configurable intervals. This application is designed to run in a Docker container and is useful for testing log collection, monitoring systems, and generating sample log data.

## Features

- Configurable logging duration and frequency
- Writes logs to both stdout and file
- Timestamped log files with unique names
- Graceful shutdown with Ctrl+C
- Configurable log directory location

## Building the Docker Image

```bash
docker build -t logger .
```

## Running the Container

### Basic Usage

```bash
docker run logger
```

### With Custom Configuration

```bash
docker run -e DURATION_MINUTES=30 -e LOGS_PER_MINUTE=5 logger
```

### With Volume Mount for Log Persistence

```bash
docker run -v /host/logs:/logs logger
```

### Complete Example with All Options

```bash
docker run \
  -e DURATION_MINUTES=60 \
  -e LOGS_PER_MINUTE=10 \
  -e LOG_DIRECTORY=/custom/logs \
  -v /host/logs:/custom/logs \
  logger
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DURATION_MINUTES` | `20` | How long the logger should run (in minutes) |
| `LOGS_PER_MINUTE` | `2` | Number of log entries to generate per minute |
| `LOG_DIRECTORY` | `/logs` | Directory where log files will be written |

### Environment Variable Details

#### DURATION_MINUTES
- **Type**: Integer
- **Default**: 20
- **Purpose**: Controls how long the application will run before automatically stopping
- **Example**: `DURATION_MINUTES=60` runs for 1 hour

#### LOGS_PER_MINUTE
- **Type**: Integer  
- **Default**: 2
- **Purpose**: Controls the frequency of log generation
- **Calculation**: Sleep interval = 60 seconds / LOGS_PER_MINUTE
- **Examples**: 
  - `LOGS_PER_MINUTE=1` = 1 log every 60 seconds
  - `LOGS_PER_MINUTE=6` = 1 log every 10 seconds
  - `LOGS_PER_MINUTE=60` = 1 log every second

#### LOG_DIRECTORY
- **Type**: String (file path)
- **Default**: `/logs`
- **Purpose**: Specifies where log files are written inside the container
- **Note**: Directory is created automatically if it doesn't exist
- **Example**: `LOG_DIRECTORY=/app/logs` writes logs to `/app/logs/`

## Log File Format

Log files are created with timestamps in their names:
```
application_log_YYYYMMDD_HHMMSS.log
```

Example: `application_log_20241207_143022.log`

Each log entry follows this format:
```
[2024-12-07T14:30:22.123456] Log entry #1: Application is running
```

## Volume Mounting

To persist logs outside the container, mount a volume to the log directory:

```bash
# Mount host directory to default log location
docker run -v /host/path/to/logs:/logs logger

# Mount to custom log directory
docker run -e LOG_DIRECTORY=/custom/logs -v /host/path/to/logs:/custom/logs logger
```

## Stopping the Application

The application can be stopped in two ways:

1. **Automatic**: Runs for the configured `DURATION_MINUTES` and stops
2. **Manual**: Press `Ctrl+C` to stop immediately

Both methods will log the final count and close files gracefully.

## Example Output

```
Starting logger. Will run for 20 minutes, logging 2 times per minute.
Logs will be written to: /logs/application_log_20241207_143022.log
Press Ctrl+C to stop.
[2024-12-07T14:30:22.123456] Log entry #1: Application is running
[2024-12-07T14:30:52.234567] Log entry #2: Application is running
[2024-12-07T14:31:22.345678] Log entry #3: Application is running
...
Logger completed after 20 minutes with 40 log entries.
```