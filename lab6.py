import numpy as np
import matplotlib.pyplot as plt
from commpy.channelcoding import bch_encode, bch_decode
from commpy.channels import bsc
from commpy.utilities import bitarray2dec, dec2bitarray

# Параметры BCH кодов
n1, k1 = 15, 7
n2, k2 = 31, 11

s1 = f"BCH code ({n1}, {k1})"
s2 = f"BCH code ({n2}, {k2})"
s3 = "Without coding"

p0 = [1e-1, 1.2e-1, 1.5e-1, 2e-1, 2.5e-1]
stat = np.zeros((3, len(p0)))

# Создание случайных сообщений
msg1 = np.random.randint(0, 2, (1000, k1))
msg2 = np.random.randint(0, 2, (1000, k2))

# Кодирование BCH
menc1 = np.array([bch_encode(msg, n1, k1) for msg in msg1])
menc2 = np.array([bch_encode(msg, n2, k2) for msg in msg2])

for i, p in enumerate(p0):
    # Канал с двоичными симметричными ошибками (BSC)
    mrec1 = bsc(menc1, p)
    mdec1 = np.array([bch_decode(msg, n1, k1) for msg in mrec1])
    num, rate = bitarray2dec(msg1) - bitarray2dec(mdec1)
    stat[0, i] = rate.mean()
    
    mrec2 = bsc(menc2, p)
    mdec2 = np.array([bch_decode(msg, n2, k2) for msg in mrec2])
    num, rate = bitarray2dec(msg2) - bitarray2dec(mdec2)
    stat[1, i] = rate.mean()
    
    mrec3 = bsc(msg1, p)
    num, rate = bitarray2dec(msg1) - bitarray2dec(mrec3)
    stat[2, i] = rate.mean()

# Построение графиков
plt.figure()

L3, = plt.loglog(p0, stat[2, :], 'r', linewidth=3, label=s3)
L1, = plt.loglog(p0, stat[0, :], 'k', linewidth=1, label=s1)
L2, = plt.loglog(p0, stat[1, :], 'b', linewidth=3, label=s2)

plt.title(f"BCH codes ({n1}, {k1}) and ({n2}, {k2}) in BSC channel")
plt.xlabel("BER in BSC channel, p0")
plt.ylabel("Error rate after decoding")
plt.legend()
plt.grid(True)
plt.savefig(f"bch-{n1}-{k1}_cycl-{n2}-{k2}_bsc_err_rate.png")
plt.show()
