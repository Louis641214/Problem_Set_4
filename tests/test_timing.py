import matplotlib.pyplot as plt
from src.rsa import generate_keys, encrypt, attack

bit_lengths = [i for i in range (8,18)]
average_times = []

for bits in bit_lengths:
    start = 2**bits
    end = 2**(bits + 1)
    trials = 5
    total_time = 0
    print(f"Testing prime size ~{bits} bits (range {start}-{end})...")
    for _ in range(trials):
        e, d, n = generate_keys(start, end)
        message = 77
        ciphertext = encrypt(message, e, n)
        _, duration = attack(e, n, ciphertext)
        if duration is not None:
            total_time += duration
    average = total_time / trials
    average_times.append(average)

# Plot results
plt.figure()
plt.plot(bit_lengths, average_times, marker='o')
plt.title("Average Time to Break RSA via Factorization")
plt.xlabel("Prime Size (bits)")
plt.ylabel("Average Time (seconds)")
plt.grid(True)
plt.show()
