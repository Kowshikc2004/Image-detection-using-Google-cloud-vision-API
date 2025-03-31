from google.cloud import vision
import io
client=vision.ImageAnnotatorClient.from_service_account_file('API_key.json')
image_path="car3.png"

with io.open(image_path,'rb') as image_file:
    content= image_file.read()
image=vision.Image(content=content)

response=client.label_detection(image=image)
labels=response.label_annotations 

for label in labels:
    print(label.description, label.score)