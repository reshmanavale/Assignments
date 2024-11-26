import psutil
import time
import sys

# Set a threshold for CPU usage (in percentage)
CPU_THRESHOLD = 80  # You can change this threshold to any value you prefer

def monitor_cpu():
    """
    Continuously monitors CPU usage and prints an alert if the usage exceeds the threshold.
    """
    try:
        while True:
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)  # interval=1 means wait for 1 second

            print(f"Monitoring CPU usage... Current CPU usage: {cpu_usage}%")

            # Check if CPU usage exceeds the threshold
            if cpu_usage > CPU_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            time.sleep(1)  # Pause for a short time before checking again

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C (interrupt) to stop the monitoring
        print("\nMonitoring stopped by user.")
        sys.exit(0)

    except Exception as e:
        # Catch any other unexpected exceptions and display an error message
        print(f"Error occurred while monitoring CPU usage: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()
