import serial
import re

def read_serial(port, baudrate):
    # Open the serial port
    ser = serial.Serial(port, baudrate, timeout=1)
    
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Print the raw received line (for debugging)
            print(f"Received: {line}")
            
            # Use regular expressions to extract CH1 and CH2 values
            match = re.match(r"CH1= (\d+)\tCH2 = (\d+)", line)
            if match:
                ch1_value = int(match.group(1))
                ch2_value = int(match.group(2))
                
                # Print the extracted values
                print(f"CH1 Value: {ch1_value}, CH2 Value: {ch2_value}")
            else:
                print("No match found or invalid data format.")
                #print(line) # if we send other data
                
    except KeyboardInterrupt:
        print("Exiting...")
        
    finally:
        ser.close()

if __name__ == "__main__":
    # Change 'COM3' and 9600 to your serial port and baudrate
    port = '/dev/ttyACM0'
    baudrate = 115200
    
    read_serial(port, baudrate)

