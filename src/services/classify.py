from classifiers.filename import FilenameClassifier
from classifiers.contents import FileContentsClassifier
from werkzeug.datastructures import FileStorage


async def classify_file(file: FileStorage):
    """A service to classify a file.

    Args:
        file (FileStorage): A file-like object.

    Returns:
        str: The classification of the file.
    """

    classifier = FilenameClassifier(file)
    file_class = await classifier.classify()

    if file_class:
        return file_class

    classifier = FileContentsClassifier(file)
    file_class = await classifier.classify()

    if file_class:
        return file_class

    # classifier = OpenAIClassifier(file)
    # file_class = await classifier.classify()

    # if file_class:
    #     return file_class

    return "unknown"
