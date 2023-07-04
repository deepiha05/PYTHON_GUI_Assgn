# Imports


class RescaleImage(object):
    """
        Rescales the image to a given size.
    """

    def __init__(self, output_size):
        """
            Arguments:
            output_size (tuple or int): Desired output size.
            If tuple, output is matched to output_size.
            If int, smaller of image edges is matched to output_size keeping aspect ratio the same.
        """

        # Write your code here
        self.output_size = output_size

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        """

        # Write your code here
        # syntax : isinstance(object, type)
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False
        if isinstance(self.output_size, tuple):
            return image.resize(self.output_size)
        else:
            x, y = image.size
            if x < y:
                # image.resize() Returns a resized copy of this image.
                # Syntax: Image.resize(size, resample=0)
                # size – The requested size in pixels, as a 2-tuple: (width, height).
                return image.resize((self.output_size, int((self.output_size * y) / x)))
            else:
                return image.resize((int((self.output_size * x) / y), self.output_size))
