import matplotlib.pyplot as plt
import numpy as np


f = open("current_logs.txt", "r")
data = f.read()
data = eval(data)

# Used Memory Plot

# data = {'Total': data['total'], 'Used': data['used']}
# names = list(data.keys())
# values = list(data.values())

# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('System Used Memory plot')
# plt.savefig("system_memory_graph.png")


# Disk Plot

# data = {'Total': data['totalDisk'], 'Used': data['usedDisk']}
# names = list(data.keys())
# values = list(data.values())
# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('System Disk plot')
# plt.savefig("disk_graph.png")


# CPU Plot

total_cpu = data['cpu']
data = {'CPU1': total_cpu[0], 'CPU2': total_cpu[1], 'CPU3' : total_cpu[2], 'CPU4': total_cpu[3]}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('CPU plots')
plt.savefig("cpu_graph.png")