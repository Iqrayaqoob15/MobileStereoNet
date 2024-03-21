import matplotlib.pyplot as plt

f = open("logs.txt", "r")
data = f.read()
data = eval(data)
# print(data)

# Used Memory Plot
# usedMemory = data['used']
# names = ['Total']
# for i in range(len(usedMemory)):
#     names.append(f"used {i+1}")
#
# usedMemory.insert(0, data['total'][0])
# plt.bar(names,usedMemory)
# plt.title("Used Memory plot")
# plt.savefig("used_memory_graph.png")

# usedMemory = data['used']
# def used_memory():
#     my_list = {}
#     for i in range(len(usedMemory)):
#         my_list[f"Used{i}"] = usedMemory[i]
#     return my_list

# data = used_memory()
# names = list(data.keys())
# values = list(data.values())
# fig, axs = plt.subplots(1, 3, figsize=(20, 6), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Used Memory plots')
# plt.savefig("used_memory_plot.png")

# Total Memory Plot
# totalMemory = data['total']
# totalUsedMemory = data['used']
# totalAvaliableMemory = data['available']
# totalFreeMemory = data['free']
# totalActiveMemory = data['active']
# totalMemoryNames = ['Total', 'Used', 'Avaliable', 'Free', 'Active']
# totalMemoryValues = [totalMemory[len(totalMemory)-1],
#                      totalUsedMemory[len(totalUsedMemory) - 1],
#                      totalAvaliableMemory[len(totalAvaliableMemory)-1],
#                      totalFreeMemory[len(totalFreeMemory)-1],
#                      totalActiveMemory[len(totalActiveMemory) - 1]]
# plt.bar(totalMemoryNames, totalMemoryValues)
# plt.title("Total Memory plot")
# plt.savefig("total_memory_plot.png")

# totalMemory = data['total']
# totalUsedMemory = data['used']
# totalAvaliableMemory = data['available']
# totalFreeMemory = data['free']
# totalActiveMemory = data['active']

# data = {'Total': totalMemory[len(totalMemory)-1] , 'Used': totalUsedMemory[len(totalUsedMemory) - 1], 'Available' : totalAvaliableMemory[len(totalAvaliableMemory)-1], 'Free': totalFreeMemory[len(totalFreeMemory)-1], 'Active': totalActiveMemory[len(totalActiveMemory) - 1]}
# names = list(data.keys())
# values = list(data.values())
# fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Memory plots')
# plt.savefig("total_memory_plot.png")

# Total Disk Usage
# totalDisk = data['totalDisk']
# usedDisk = data['usedDisk']
# freeDisk = data['freeDisk']

# totalDiskNames = ['Total Disk', 'Used Disk', 'Free Disk']
# totalDiskValues = [totalDisk[len(totalDisk)-1],
#                    usedDisk[len(usedDisk)-1],
#                    freeDisk[len(freeDisk)-1]]
# plt.bar(totalDiskNames, totalDiskValues)
# plt.title("Total Disk plot")
# plt.savefig("total_disk_plot.png")

# total_disk = data['totalDisk']
# used_disk = data['usedDisk']
# free_disk = data['freeDisk']

# data = {'Total': total_disk[len(total_disk)-1] , 'Used': used_disk[len(used_disk)-1], 'Free' : free_disk[len(free_disk)-1]}
# names = list(data.keys())
# values = list(data.values())
# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Disk plots')
# plt.savefig("total_disk_plot.png")
    

# Total CPU usage
# total_cpu = data['cpu']
# cpu_names = ['CPU 1', 'CPU 2', 'CPU 3', 'CPU 4']
# for i in range(len(total_cpu)):
#     cpu_values = [total_cpu[i][0], total_cpu[i][1], total_cpu[i][2], total_cpu[i][3]]
#     # plt.bar(cpu_names, cpu_values)
#     plt.title("Total CPU plot")
#     colors = ['green', 'brown', 'blue', 'red']
#     plt.pie(cpu_values, labels=cpu_names, colors=colors)
#     plt.axis('equal')
#     plt.savefig(f"total_cpu_plot{i}.png")
#     plt.close()

# total_cpu = data['cpu']
# for i in range(len(total_cpu)):
#     data = {'CPU1': total_cpu[i][0], 'CPU2': total_cpu[i][1], 'CPU3' : total_cpu[i][2], 'CPU4': total_cpu[i][3]}
#     names = list(data.keys())
#     values = list(data.values())

#     fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
#     axs[0].bar(names, values)
#     axs[1].scatter(names, values)
#     axs[2].plot(names, values)
#     fig.suptitle('CPU plots')
#     plt.savefig(f"total_cpu_plot{i}.png")
