from flask import Flask
app = Flask(__name__)

@app.rout("/")
def test():
    import cv2

    print("Hi, Daniel! Benvenuto al mondo dell'IA!")

    im = cv2.imread("./banana1.jpg")
    window_name  = 'image'
    cv2.imshow(window_name,im)
    cv.waitKey(0)
