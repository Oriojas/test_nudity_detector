from nudenet import NudeClassifier

classifier = NudeClassifier()

p1 = classifier.classify("/home/oscar/GitHub/test_nudity_detector/img/images.jpeg")
p2 = classifier.classify("/home/oscar/GitHub/test_nudity_detector/img/ella.jpg")

print(p1)
print(p2)

