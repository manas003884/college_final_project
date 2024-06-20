class Steganalysis():

  def __init__(self, image_path):
    import numpy as np
    import cv2 as cv
    self.np = np
    self.cv = cv
    self.img = cv.imread(image_path)

  def binaryToInteger(self, binary):  
      binary1 = binary  
      decimal, i, n = 0, 0, 0
      while(binary != 0):  
          dec = binary % 10
          decimal = decimal + dec * pow(2, i)  
          binary = binary//10
          i += 1
      return (decimal)     

  def decode_data(self):
    binary_data = ""
    for i in self.img:
        for pixel in i:
            r, g, b = pixel
            binary_data += (format(r, "08b")[-1])
            binary_data += (format(g, "08b")[-1])
            binary_data += (format(b, "08b")[-1])

    # split by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "*****": # check if we have reached the delimeter which is "*****"
            break

    return decoded_data[:-5] #remove the delimeter to show the original hidden message

  def decode(self):
    text = self.decode_data()
    return text


steganalysis = Steganalysis('D:\image stego using github\Image-Steganalysis-using-Deep-Neural-Networks\EncryptedImages\Encrypted1.png')
hidden_message = steganalysis.decode()
print("The hidden message is:", hidden_message)
