from src.classifiers.filename import FilenameClassifier

def classify(classifier: FilenameClassifier):
    """A service to classify a file.

    Args:
        classifier (FilenameClassifier): Some classifier object.

    Returns:
        str: The classification of the file.
    """
    
    return classifier.classify()