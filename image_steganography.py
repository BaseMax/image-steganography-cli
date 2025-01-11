# python image_steganography.py encode input_image.png "Hello, World!" output_image.png
# python image_steganography.py decode output_image.png
from PIL import Image
import sys

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        raise ValueError("The image should be in RGB mode")
    
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'
    
    img_data = list(img.getdata())
    new_img_data = []

    message_index = 0
    for pixel in img_data:
        if message_index < len(binary_message):
            pixel = list(pixel)
            for i in range(3):
                if message_index < len(binary_message):
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[message_index])
                    message_index += 1
            new_img_data.append(tuple(pixel))
        else:
            new_img_data.append(pixel)

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_img_data)
    new_img.save(output_path)
    print(f"Message hidden successfully! Output image saved as {output_path}")

def decode_image(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        raise ValueError("The image should be in RGB mode")
    
    img_data = list(img.getdata())
    binary_message = ''

    for pixel in img_data:
        for i in range(3):
            binary_message += str(pixel[i] & 1)

    end_index = binary_message.find('1111111111111110')
    if end_index != -1:
        binary_message = binary_message[:end_index]
    else:
        print("No hidden message found!")
        return ""

    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return message

def main():
    if len(sys.argv) < 3:
        print("Usage: python image_steganography.py encode <image_path> <message> <output_path>")
        print("or")
        print("Usage: python image_steganography.py decode <image_path>")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == 'encode':
        if len(sys.argv) != 5:
            print("Usage: python image_steganography.py encode <image_path> <message> <output_path>")
            sys.exit(1)

        image_path = sys.argv[2]
        message = sys.argv[3]
        output_path = sys.argv[4]
        encode_image(image_path, message, output_path)

    elif operation == 'decode':
        if len(sys.argv) != 3:
            print("Usage: python image_steganography.py decode <image_path>")
            sys.exit(1)

        image_path = sys.argv[2]
        message = decode_image(image_path)
        print(f"Hidden message: {message}")

    else:
        print("Invalid operation! Use 'encode' or 'decode'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
