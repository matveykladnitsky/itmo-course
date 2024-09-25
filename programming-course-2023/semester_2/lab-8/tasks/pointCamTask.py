import cv2
import numpy as np


class VideoCaptureTask:
    def __init__(self, source=0, target_image_path='data/target_image.jpeg'):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise ValueError("Не удалось открыть вебку")

        self.target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)
        if self.target_image is None:
            raise ValueError("Не удалось загрузить изображение")

        self.sift = cv2.SIFT_create()
        self.target_keypoints, self.target_descriptors = self.sift.detectAndCompute(
            self.target_image, None)
        self.flann = cv2.FlannBasedMatcher(
            dict(algorithm=1, trees=5), dict(checks=50))

    def detect_target(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = self.sift.detectAndCompute(gray_frame, None)
        if descriptors is None:
            return False, None

        matches = self.flann.knnMatch(
            self.target_descriptors, descriptors, k=2)
        good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]

        if len(good_matches) > 10:
            src_pts = np.float32(
                [self.target_keypoints[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32(
                [keypoints[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

            if M is not None:
                h, w = self.target_image.shape
                pts = np.float32(
                    [[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                try:
                    dst = cv2.perspectiveTransform(pts, M)
                    return True, np.mean(dst, axis=0).flatten()
                except cv2.error:
                    print("Что-то пошло не так...")
        return False, None

    def is_in_center_area(self, point, frame_shape):
        height, width = frame_shape[:2]
        center_x, center_y = width // 2, height // 2
        area_size = 200
        return (abs(point[0] - center_x) < area_size // 2 and
                abs(point[1] - center_y) < area_size // 2)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Не удалось получить кадр")
                break

            detected, center = self.detect_target(frame)
            if detected:
                cv2.putText(frame, 'Image detected', (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if self.is_in_center_area(center, frame.shape):
                    cv2.putText(frame, 'Image in the center!!', (50, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            h, w = frame.shape[:2]
            cv2.rectangle(frame, (w//2 - 100, h//2 - 100),
                          (w//2 + 100, h//2 + 100), (255, 0, 0), 2)
            cv2.imshow('Video Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
