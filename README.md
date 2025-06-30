Python script simulates the performance of BCH error-correcting codes in a Binary Symmetric Channel (BSC). It compares the bit error rates after decoding using:

BCH(15, 7) — encodes 7 bits into 15

BCH(31, 11) — encodes 11 bits into 31

No encoding — for baseline comparison

The simulation evaluates how effectively each scheme corrects errors under different bit error probabilities. It uses the commpy library to:

Encode random binary messages using BCH codes

Introduce noise using BSC (bit flipping with probability p)

Decode the received data

Calculate and plot the error rates

The result is a log-log plot that visually compares the robustness of each method under increasing channel noise.

📈 Output:
A PNG plot file showing error rate vs. channel noise.

Clear insight into the advantage of BCH coding in noisy environments.

💡 Use Cases:
Digital communication simulation

Error correction learning

BCH code performance analysis

Channel coding coursework or research
