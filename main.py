import cv2

class Video:
    def __init__(self, path):
        self.cap = cv2.VideoCapture(path)

        while True:
            success, img = self.cap.read()
            cv2.imshow('Video', img)

            if cv2.waitKey(15) & 0xFF == ord('q'):
                break


def main():
    capture = Video(0)
    print(capture)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Finished")
