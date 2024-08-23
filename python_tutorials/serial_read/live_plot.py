import serial
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to read and parse the serial data
def read_serial_data(ser):
    line = ser.readline().decode('utf-8').strip()
    match = re.match(r"CH1= (\d+)\tCH2 = (\d+)", line)
    if match:
        ch1_value = int(match.group(1))
        ch2_value = int(match.group(2))
        return ch1_value, ch2_value
    return None, None

def update_plot(frame, ser, lines, xs, ys1, ys2):
    ch1_value, ch2_value = read_serial_data(ser)
    if ch1_value is not None and ch2_value is not None:
        # Append the new data to the lists
        xs.append(frame)
        ys1.append(ch1_value)
        ys2.append(ch2_value)

        # Keep only the latest 100 data points
        xs = xs[-100:]
        ys1 = ys1[-100:]
        ys2 = ys2[-100:]

        # Update the lines with new data
        lines[0].set_data(xs, ys1)
        lines[1].set_data(xs, ys2)

        # Adjust the x-axis and y-axis limits
        ax.set_xlim(max(0, frame-100), frame)
        ax.set_ylim(0, max(max(ys1), max(ys2)) + 10)
    return lines

if __name__ == "__main__":
    # Set up the serial connection
    port = '/dev/ttyACM0'  # Replace with your port
    baudrate = 9600  # Replace with your baud rate
    ser = serial.Serial(port, baudrate, timeout=1)

    # Set up the plot
    fig, ax = plt.subplots()
    xs = []
    ys1 = []
    ys2 = []

    line1, = ax.plot([], [], label='CH1')
    line2, = ax.plot([], [], label='CH2')
    lines = [line1, line2]

    ax.set_title('Live Serial Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    ax.legend(loc='upper left')
    ax.grid(True)

    # Set up the animation
    ani = animation.FuncAnimation(
        fig, update_plot, fargs=(ser, lines, xs, ys1, ys2),
        interval=100, blit=True, cache_frame_data=False)

    plt.show()

    # Close the serial connection when done
    ser.close()

