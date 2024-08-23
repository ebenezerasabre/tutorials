clear;
clc;
Fs = 4000; % Sampling frequency
window_duration = 0.1;  % Window size in seconds (100 ms)
window_length = window_duration * Fs;  % Window length in samples
 
% 1. Load the ECG Data from the PCB and MATLAB
sig_pcb = readmatrix("exp_aug12_4k_vmv_pcb_d1_sub3.csv"); % signal from PCB
sig_pwrlb =  load("exp_aug12_4k_vmv_pwrlb_d1_sub3.mat"); % signal from PowerLAB
sig_pwrlb = sig_pwrlb.data; % get the data from powerLAB

time_pwrlb = (1:length(sig_pwrlb))/Fs;
time_pcb = (1:length(sig_pcb))/Fs;

% Define the vertical line times
vertical_lines = [30, 50, 80, 100];

% Figure 1: ECG signals
figure
p1 = subplot(2, 1, 1);
plot(time_pcb, sig_pcb)
title("ECG pcb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off

p2 = subplot(2, 1, 2);
plot(time_pwrlb, sig_pwrlb)
title("ECG pwrlb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off
linkaxes([p1, p2], 'x')

% Preprocess the signals
sig_pcb(isnan(sig_pcb)) = 0;
sig_pcb(sig_pcb > 3*mean(sig_pcb)) = 0;
sig_pwrlb(sig_pwrlb > 3*mean(sig_pwrlb)) = 0;

skna_pcb = bandpass(sig_pcb, [500, 1000], Fs);
skna_pwrlb = bandpass(sig_pwrlb, [500, 1000], Fs);

skna_pcb = skna_pcb(1*Fs:end-1*Fs);
skna_pwrlb = skna_pwrlb(1*Fs:end-1*Fs);

time_pwrlb = time_pwrlb(1*Fs:end-1*Fs);
time_pcb = time_pcb(1*Fs:end-1*Fs);

% Figure 2: SKNA signals
figure
p1 = subplot(2, 1, 1);
plot(time_pcb, skna_pcb)
title("SKNA pcb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off

p2 = subplot(2, 1, 2);
plot(time_pwrlb, skna_pwrlb)
title("SKNA pwrlb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off
linkaxes([p1, p2], 'x')

% Calculate integrated SKNA
iSKNA_pcb = movmean(abs(skna_pcb), [window_length/2 window_length/2]);
iSKNA_pwrlb = movmean(abs(skna_pwrlb), [window_length/2 window_length/2]);

% Figure 3: Integrated SKNA signals
figure
p1 = subplot(2, 1, 1);
plot(time_pcb, iSKNA_pcb)
title("iSKNA pcb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off

p2 = subplot(2, 1, 2);
plot(time_pwrlb, iSKNA_pwrlb)
title("iSKNA pwrlb")
hold on
for i = 1:length(vertical_lines)
    xline(vertical_lines(i), '--r');
end
hold off
linkaxes([p1, p2], 'x')

