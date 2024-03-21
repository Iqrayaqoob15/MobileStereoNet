import psutil

f = open("current_logs.txt", "w+")

logs = {
	"total": psutil.virtual_memory().total,
	"available":  psutil.virtual_memory(). available,
	"percent": psutil.virtual_memory().percent,
	"used": psutil.virtual_memory().used,
	"free": psutil.virtual_memory().free,
	"active": psutil.virtual_memory().active,
	"inactive": psutil.virtual_memory().inactive,
	"buffers": psutil.virtual_memory().buffers,
	"cached": psutil.virtual_memory().cached,
	"shared": psutil.virtual_memory().shared,
	"slab": psutil.virtual_memory().slab,
	"totalDisk": psutil.disk_usage('/').total,
	"usedDisk": psutil.disk_usage('/').used,
	"freeDisk": psutil.disk_usage('/').free,
	"percentDisk": psutil.disk_usage('/').percent,
	'cpu': psutil.cpu_percent(percpu=True, interval=2)
}
f.write(f"{logs}")
f.close()