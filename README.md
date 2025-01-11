# Image Steganography in Python

This program allows you to hide a secret message in an image using steganography techniques. The message is encoded in the least significant bits of the image's pixels and can be decoded later by extracting the hidden data.

## Features

- **Encode**: Hide a secret message in an image.
- **Decode**: Extract the hidden message from an image.

## Prerequisites

- Python 3.x
- Pillow (Python Imaging Library)

You can install Pillow using the following command:

```bash
pip install pillow
```

## Usage

### Encoding a Message

To hide a message in an image, use the encode operation. This will encode the given message into the image and save the result as a new image.

```
python image_steganography.py encode <image_path> <message> <output_path>
```

- `<image_path>`: The path to the image where you want to hide the message.
- `<message>`: The secret message you want to hide in the image.
- `<output_path>`: The path where the new image with the hidden message will be saved.

**Example:**

```bash
python image_steganography.py encode input_image.png "Hello, World!" output_image.png
```

### Decoding a Message

To extract the hidden message from an image, use the decode operation. This will decode the hidden message and display it.

```bash
python image_steganography.py decode <image_path>
```

- `<image_path>`: The path to the image containing the hidden message.

**Example:**

```bash
python image_steganography.py decode output_image.png
```

## How It Works

### Encoding

The program converts the secret message into binary.

It appends a delimiter ('1111111111111110') to mark the end of the message.

Each pixel of the image is processed, and the least significant bit (LSB) of each color channel (RGB) is replaced with one bit of the binary message.

The modified pixels are saved to a new image file.

### Decoding

The program reads the LSBs of each pixel's RGB channels.

It collects these bits to form the binary message.

The program looks for the delimiter ('1111111111111110') to determine the end of the hidden message.

The binary message is converted back into text and displayed.

```
python image_steganography.py encode input_image.png "This is a secret message!" output_image.png
and
python image_steganography.py decode output_image.png
```

### Notes

- The program currently supports only RGB images. Ensure the image is in RGB mode before encoding.
- The message is hidden in the least significant bits of each pixel. The more pixels the image has, the more data you can hide.
- The delimiter ('1111111111111110') marks the end of the message to prevent accidental overlaps.

## License

This project is licensed under the MIT License.

Copyright 2025, Max Base
