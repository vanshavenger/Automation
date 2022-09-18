from PIL import Image
import glob

print(glob.glob("*.png"))

str = input("Which Formart you want your file to be convertd in: ")
quality = int(input("Quality of the image should be (100 for max) :  "))
if str == "jpg":
    for file in glob.glob("*.png"):
        img = Image.open(file)
        rgb_im =img.convert('RGB')
        rgb_im.save(file.replace("png","jpg"),quality=quality)
        print("Converted to ",str," Format")
elif str == "jpeg":
    for file in glob.glob("*.png"):
        img = Image.open(file)
        rgb_im =img.convert('RGB')
        rgb_im.save(file.replace("png","jpeg"),quality=quality)
        print("Converted to ",str," Format")
else:
    print("Conversion not supported as of now!!")
