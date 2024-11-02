import psutil
import platform

def get_cpu_info():
    # Get basic CPU info
    cpu_info = {
        "Architecture": platform.architecture()[0],
        "CPU count": psutil.cpu_count(logical=True),
        "Physical cores": psutil.cpu_count(logical=False),
        "CPU frequency": psutil.cpu_freq().current,
        "CPU usage": psutil.cpu_percent(interval=1),
        "CPU model": platform.processor(),
        "CPU details": platform.uname()
    }

    return cpu_info

def display_cpu_info(cpu_info):
    print("CPU Information:")
    print(f"Architecture: {cpu_info['Architecture']}")
    print(f"Logical CPU(s): {cpu_info['CPU count']}")
    print(f"Physical Core(s): {cpu_info['Physical cores']}")
    print(f"Current CPU Frequency (MHz): {cpu_info['CPU frequency']:.2f}")
    print(f"CPU Usage (%): {cpu_info['CPU usage']:.2f}")
    print(f"Model Name: {cpu_info['CPU model']}")
    
    # Display detailed system information
    print("nDetailed System Information:")
    print(f"System: {cpu_info['CPU details'].system}")
    print(f"Node Name: {cpu_info['CPU details'].node}")
    print(f"Release: {cpu_info['CPU details'].release}")
    print(f"Version: {cpu_info['CPU details'].version}")
    print(f"Machine: {cpu_info['CPU details'].machine}")
    print(f"Processor: {cpu_info['CPU details'].processor}")

if __name__ == "__main__":
    cpu_info = get_cpu_info()
    display_cpu_info(cpu_info)
