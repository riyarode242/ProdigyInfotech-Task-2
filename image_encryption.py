from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)
    
    # Perform encryption by adding key value to each pixel
    encrypted_pixels = (pixels + key) % 256
    
    # Swap pixel values for added encryption
    encrypted_pixels = np.flip(encrypted_pixels, axis=1)
    
    # Create an encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')
    encrypted_img.save('encrypted_image.png')
    return 'encrypted_image.png'

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img = encrypted_img.convert('RGB')
    encrypted_pixels = np.array(encrypted_img)
    
    # Reverse the pixel value swap
    decrypted_pixels = np.flip(encrypted_pixels, axis=1)
    
    # Perform decryption by subtracting key value from each pixel
    decrypted_pixels = (decrypted_pixels - key) % 256
    
    # Create a decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')
    decrypted_img.save('decrypted_image.png')
    return 'decrypted_image.png'

# Example usage
image_path = 'input_image.png'
key = 50

# Encrypt the image
encrypted_image_path = encrypt_image(image_path, key)
print(f"Encrypted image saved as: {encrypted_image_path}")

# Decrypt the image
decrypted_image_path = decrypt_image(encrypted_image_path, key)
print(f"Decrypted image saved as: {decrypted_image_path}")