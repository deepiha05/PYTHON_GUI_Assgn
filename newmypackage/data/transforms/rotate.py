# Imports


class RotateImage(object):
    """
        Rotates the image about the centre of the image.
    """

    def __init__(self, degrees):
        """
            Arguments:
            degrees: rotation degree.
        """

        # Write your code here
        self.degrees = degrees

    def __call__(self, sample):
        """
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        """

        # Write your code here
        # Rotate Image By self.degreess Degree
        return sample.rotate(self.degrees)
