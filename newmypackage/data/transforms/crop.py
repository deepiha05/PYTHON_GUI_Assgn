# import
import numpy as np


class CropImage(object):
    """
    Performs either random cropping or center cropping.
    """

    def __init__(self, shape, crop_type='center'):
        """
        Arguments:
        shape: output shape of the crop (h, w)
        crop_type: center crop or random crop. Default: center
        """

        # Write your code here
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        """
        Arguments:
        image (numpy array or PIL image)
        Returns:
        image (numpy array or PIL image)
        """

        # Write your code here
        # extracts width, height of the image
        x, y = image.size
        if self.crop_type == 'center':
            x = int(x / 2)
            y = int(y / 2)
            # assigning half of width of required final output image
            left = right = int(self.shape[1] / 2)
            if self.shape[1] % 2:
                right += 1
            # assigning half of height of required final output image
            upper = lower = int(self.shape[0] / 2)
            if self.shape[0] % 2:
                lower += 1
            # cropping the image.
            # image.crop() method is used to crop a rectangular portion of any image.
            return image.crop((x - left, y - upper, x + right, y + lower))

        else:
            left = np.random.randint(0, x - self.shape[1])
            upper = np.random.randint(0, y - self.shape[0])
            return image.crop((left, upper, left + self.shape[1], upper + self.shape[0]))
