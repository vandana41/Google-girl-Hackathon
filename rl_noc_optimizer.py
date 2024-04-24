read_transactions = {}
write_transactions = 0
total_data_transferred = 0
total_cycles = 0

# Monitor output processing
for entry in monitor_output:
    timestamp, txn_type, data = entry

    if txn_type.startswith('Rd'):
        read_transactions[data] = timestamp
    elif txn_type.startswith('Data'):
        address = txn_type.split(' ')[1]
        if address in read_transactions:
            latency = timestamp - read_transactions[address]
            del read_transactions[address]
    elif txn_type.startswith('Wr'):
        write_transactions += 1
        total_data_transferred += 32  
    total_cycles = max(total_cycles, timestamp)

# Calculate average latency and bandwidth
average_latency = calculate_average_latency(read_latencies)  
average_bandwidth = total_data_transferred / total_cycles

# Outputs
print(f"Average Latency: {average_latency} cycles")
print(f"Average Bandwidth: {average_bandwidth} bytes/cycle")
