from tasks import hsvTask, pointCamTask

# Task 1
hsvTask.HsvTask(input_path='data/picture.jpeg',
                output_path='data/picture_hsv.jpeg').run()

# Task 2 & 3
pointCamTask.VideoCaptureTask(
    source=0, target_image_path='data/ref-point.jpg').run()
