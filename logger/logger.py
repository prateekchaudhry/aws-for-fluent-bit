import time
import datetime
import sys
import os
import pathlib

# Configuration from environment variables with defaults
DURATION_MINUTES = int(os.environ.get('DURATION_MINUTES', 20))
LOGS_PER_MINUTE = int(os.environ.get('LOGS_PER_MINUTE', 2))
LOG_DIRECTORY = os.environ.get('LOG_DIRECTORY', '/logs')
SLEEP_SECONDS = 60 / LOGS_PER_MINUTE

# Create log directory if it doesn't exist
pathlib.Path(LOG_DIRECTORY).mkdir(parents=True, exist_ok=True)

# Create a log file with timestamp in the name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = os.path.join(LOG_DIRECTORY, f"application_log_{timestamp}.log")
log_file = open(log_file_path, "w")

print(f"Starting logger. Will run for {DURATION_MINUTES} minutes, logging {LOGS_PER_MINUTE} times per minute.")
print(f"Logs will be written to: {log_file_path}")
print(f"Press Ctrl+C to stop.")

# Write the same information to the log file
log_file.write(f"Starting logger. Will run for {DURATION_MINUTES} minutes, logging {LOGS_PER_MINUTE} times per minute.\n")
log_file.write(f"Logs will be written to: {log_file_path}\n")
log_file.flush()

start_time = time.time()
end_time = start_time + (DURATION_MINUTES * 60)
log_count = 0

try:
    while time.time() < end_time:
        log_count += 1
        timestamp = datetime.datetime.now().isoformat()
        message = f"[{timestamp}] Log entry #{log_count}: Application is running"
        
        # Write to stdout
        print(message)
        sys.stdout.flush()  # Ensure logs are flushed immediately
        
        # Write to log file
        log_file.write(message + "\n")
        log_file.flush()
        
        # Sleep until next log interval
        time.sleep(SLEEP_SECONDS)
        
    print(f"Logger completed after {DURATION_MINUTES} minutes with {log_count} log entries.")
    log_file.write(f"Logger completed after {DURATION_MINUTES} minutes with {log_count} log entries.\n")
    
except KeyboardInterrupt:
    print(f"Logger stopped manually after {log_count} log entries.")
    log_file.write(f"Logger stopped manually after {log_count} log entries.\n")
finally:
    log_file.close()
