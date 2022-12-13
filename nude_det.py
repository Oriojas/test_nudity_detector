from nudenet import NudeClassifier


class nudeDet:
    """
    this class detect if a picture contain nude content
    """

    def __init__(self, image):
        """
        parameters to init class
        :param image: str, direction local of image
        """

        self.image = image
        self.classifier = NudeClassifier()

    def is_nude(self, threshold=0.8):
        """
        this funtion return True if image content nude
        :param threshold: float, sensibiliti of detection in rage 0, 1
        :return:
        """

        nude = self.classifier(self.image)

        clas = list(nude.values())[0].get("unsafe")

        if clas < threshold:
            nude_clas = True
        else:
            nude_clas = False

        return nude_clas
