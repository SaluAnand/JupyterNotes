import matplotlib.pyplot as plt
# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y')
print(plt.show())