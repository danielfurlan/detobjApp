import requests, http.client, pprint, flask, shutil
import cv2, json, base64

url = "http://192.168.1.105:5000/";

path = "/var/www/danielfurlan.com/immaggine/"
fileJPG = "AIimage.jpeg"
filePng = "upsud.png"

im = cv2.imread("/home/daniel/detectron/detectron2/banana1.jpg")

myfiles = {'image': open("/home/daniel/detectron/detectron2/banana1.jpg",'rb')}

print("Files : ", myfiles)
########## POST THE FILE
s = requests.post(url,files = myfiles)
print("s.text :  ", s.text)
print("s.content : ", s.content)
print("s.headers : ", s.headers)

########### RECEIVE THE URL RESPONSE TO DOWNLOAD
js = s.json()
print("js : ", js)
########### MAKE THE GET REQUEST

full_path = url + js.get("image_url")
getR = requests.get(full_path)
open("./received/received.jpeg", "wb").write(getR.content)

#imgdata = base64.b64decode(js.get("image"))
#filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
#with open(filename, 'wb') as f:
    #f.write(imgdata)
#if s.status_code == 200:
    #print("Status OK")
    ##r.post(url,files)
    #with open("proc.jpg","wb") as outF:
        ##for chunk in s.iter_content():
        #for chunk in by:
            #outF.write(chunk)
            #"""
        #r.raw.decode_content = True
        #shutil.copyfileobj(r.raw, outF)

#head = r.headers


#https://www.baeldung.com/java-read-lines-large-file
#https://www.baeldung.com/java-write-to-file
#https://square.github.io/okhttp/3.x/okhttp/index.html?okhttp3/Response.html
