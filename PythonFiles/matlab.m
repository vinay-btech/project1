# Define the sampling rate (frequency), which has units of Hz (samples per second)
Fs = # TODO

# Calculate the time interval (the rate of change), which as units of seconds per sample.
dt = 1/Fs;

# Get the number of samples.
N = length(samples);

# Calculate the total time in seconds.
tt = N/Fs;

# Generate a time vector, starting at time 0, incrementing in intervals of dt,
# and ending at time tt (subtract one unit of time, dt, from the ending value
# to match the length of the sample vector).
t = (0 : dt : tt - dt)';

# Get the length of the time vector.
L = size(t, 1);

# Convert the time vector into a frequency vector,
# for the purposes of plotting it.
dF = Fs/L;                       # change in frequency (Hz)
f = (-Fs/2 : dF : Fs/2 - dF);    # frequency vector (like time vector above)

# Calculate the FFT of your sample vector.
x = fftshift(fft(samples));

# Generate a vector of amplitudes (voltages).
y = abs(x)/L;

# Plot it, with the frequency vector as the x-axis
# and the amplitude (voltage) as the y-axis.
plot(f, y);
