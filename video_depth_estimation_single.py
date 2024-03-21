import cv2
import pafy
import numpy as np
import glob
import psutil

from mobilestereonet import MobileStereoNet, CameraConfig
from mobilestereonet.utils import draw_depth

# Initialize video
# cap = cv2.VideoCapture("video.mp4")

# videoUrl = 'https://youtu.be/Yui48w71SG0'
# videoPafy = pafy.new(videoUrl)
# print(videoPafy.streams)
# cap = cv2.VideoCapture(videoPafy.getbestvideo().url)

cap = cv2.VideoCapture(0)
model_path = "models/model_528_240_float32.onnx"

# Store baseline (m) and focal length (pixel)
input_width = 528
camera_config = CameraConfig(0.1, 0.5*input_width) # 90 deg. FOV
max_distance = 5

# Initialize model
mobile_depth_estimator = MobileStereoNet(model_path, camera_config)
f = open("logs.txt", "w+")

cv2.namedWindow("Estimated depth", cv2.WINDOW_NORMAL)
total,available,percent,used,free,active,inactive,buffers,cached,shared,slab,totalDisk,usedDisk,freeDisk,percentDisk,cpu = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

while cap.isOpened():
	# print('psutil.cpu_times()', psutil.cpu_percent())
	# print('psutil.virtual_memory()', psutil.virtual_memory())
	try:
		# Read frame from the video
		ret, frame = cap.read()
		if not ret:
			break
	except:
		continue

	# Extract the left and right images
	left_img  = frame
	right_img = frame
	color_real_depth = frame

	# Estimate the depth
	disparity_map = mobile_depth_estimator(left_img, right_img)
	depth_map = mobile_depth_estimator.get_depth()

	color_depth = draw_depth(depth_map, max_distance)
	color_depth = cv2.resize(color_depth, (left_img.shape[1],left_img.shape[0]))
	cobined_image = np.hstack((left_img,color_real_depth, color_depth))

	# x, y, w, h = 0, 0, 175, 75

	total.append(psutil.virtual_memory().total)
	available.append(psutil.virtual_memory(). available)
	percent.append(psutil.virtual_memory().percent)
	used.append(psutil.virtual_memory().used)
	free.append(psutil.virtual_memory().free)
	active.append(psutil.virtual_memory().active)
	inactive.append(psutil.virtual_memory().inactive)
	buffers.append(psutil.virtual_memory().buffers)
	cached.append(psutil.virtual_memory().cached)
	shared.append(psutil.virtual_memory().shared)
	slab.append(psutil.virtual_memory().slab)

	totalDisk.append(psutil.disk_usage('/').total),
	usedDisk.append(psutil.disk_usage('/').used),
	freeDisk.append(psutil.disk_usage('/').free),
	percentDisk.append(psutil.disk_usage('/').percent)

	cpu.append(psutil.cpu_percent(percpu=True,interval=2))

	# f.write(f"{total}\n")
	# cv2.putText(cobined_image, str(psutil.virtual_memory()), (x + int(w / 10), y + int(h / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	# 			(255, 255, 255), 2)
	cv2.imshow("Estimated depth", cobined_image)

	# Press key q to stop
	if cv2.waitKey(1) == ord('q'):
		monetoring = {
			"total": total,
			"available":  available,
			"percent": percent,
			"used": used,
			"free": free,
			"active": active,
			"inactive": inactive,
			"buffers": buffers,
			"cached": cached,
			"shared": shared,
			"slab": slab,
			"totalDisk": totalDisk,
			"usedDisk": usedDisk,
			"freeDisk": freeDisk,
			"percentDisk": percentDisk,
			'cpu': cpu
		}
		# f.write(f"{memoryUsage}\n{diskUsage}\n{cpu}")
		f.write(f"{monetoring}")
		break

cap.release()
cv2.destroyAllWindows()
f.close()