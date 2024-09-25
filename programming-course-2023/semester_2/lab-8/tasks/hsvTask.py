import cv2


class HsvTask:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def convert_to_hsv(self):
        image = cv2.imread(self.input_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imwrite(self.output_path, hsv_image)

    def run(self):
        self.convert_to_hsv()
