clock_rate = 5 # MHz
num_bus_cycles = 3
num_bytes = 1
num_wait_states = 2

transfer_time = (num_bus_cycles + num_wait_states) * (1 / clock_rate)
actual_data_transfer_rate = num_bytes / transfer_time

print("Actual Data Transfer Rate: %.2f MB/s" % actual_data_transfer_rate)
