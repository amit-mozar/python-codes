n = [5, 6, 7, 7, 1, 2, 111, 1, 1, 5, 6, 9]
num = n
freq_counter = dict()
for i in num:
  freq_counter[i] = freq_counter.get(i, 0) + 1

total_freq = dict()
for i in num:
  if i in total_freq:
    total_freq[i] += 1
  else:
    total_freq[i] = 1
