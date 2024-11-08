# Notes & Thought process

1. Clean up repo
    - There are some design choices that can be improved. The earlier these changes are done the easier they are to implement.
        1. `requirements.txt` -> `pyproject.toml`. Moving to use pyproject allows all configuration for the project to be stored in one central location. This includes linter rules (ruff), dependencies, test config (pytest). It also allows easier splitting of dependencies and dev dependencies, this is valuable as we don't want production servers to install dev dependencies, this will keep it as lightweight as possible. At least the previous 3 python versions should be supported ideally too, this is possible to set in `pyproject.toml`. However I will be using `3.11` and not testing for previous compatibility for time.
        1. Development data (the files in `files` directory) should not be checked into the repo. This bloats the repo and will slow down cloning, builds etc. These should be stored in a shared file location and the directory should be git ignored. Downloading the files from the shared location should be part of an initial repo/project setup step. This setup guide should be contained clearly in the readme.
        1. Move utility functions out of `app.py`. `app.py` should be the top level/HTTP logic and nothing else. Utility functions should be moved to another file. I have created a `utils.py` file FOR NOW. `utils.py` is fine to have but can quickly grow and become a burden. It is very important that as functions get added they are grouped together and pulled into their own better named files.
        1. `classify_file` is not a good name for an endpoint for two main reasons. `_` should be avoided in `URLs`, `-` should be used instead. Also it is widely accepted that endpoints should not be verbs. API endpoints should be nouns representing a resource. In this case it is a POST endpoint (POST = Create), so we are "creating" a file classification. This means we should rename it to `file-classification`. I would also rename the function to `file_classification`, I don't think `_route` is required as we know it's a route with it's decorator. If we were to register the endpoints in a different way it may be preferable in the future.
        1. `ALLOWED_EXTENSIONS` should be a config variable. One reason is due to separating deployment and release, this can then allow this to be used like a feature flag.

1. Overhaul current design to use familiar technologies
    - For a basic RESTAPI I personally prefer using FastAPI. As the application is currently very simple swapping technologies/frameworks is possible. I find FastAPI to be easier. Easier meaning it required less code and knowledge to use. This allows for a faster development velocity. It has other improvements too. It is built on top of Pydantic which allows for easy request and object validation amongst many other things. It also automatically integrates with OpenAPI schema and swagger. All RestAPIs should have an OpenAPI compatible schema and swagger docs, so because FastAPI does that for you. We can spend more developer time building features and adding value. I also find testing FastAPI applications to be easier. And using FastAPI `Depends()` is a great way to comply with separation of concerns and Dependency Injection. Both of which improve testability. Better testing => less bugs (in theory).

# File Classifier

## Overview

A RestAPI to classify files.

## First time project setup

(Assuming Windows)

1. Copy development files from shared location into `local-files` dir
1. Create `.env` file for environment variables. These values can be fetched from the `dev` environment
1. Install project as editable install (include dev dependencies)

    ```shell
    python -m venv venv
    venv\Scripts\activate
    py -m pip install -e .[dev]
    ```

1. Run the app

    ```shell
    py -m uvicorn app:app --reload
    ```

1. Navigate to [swagger docs](http://127.0.0.1:8000/docs)

## Testing

Run tests using pytest

```shell
py -m pytest
```

---
# Heron Coding Challenge - File Classifier

## Overview

At Heron, we’re using AI to automate document processing workflows in financial services and beyond. Each day, we handle over 100,000 documents that need to be quickly identified and categorised before we can kick off the automations.

This repository provides a basic endpoint for classifying files by their filenames. However, the current classifier has limitations when it comes to handling poorly named files, processing larger volumes, and adapting to new industries effectively.

**Your task**: improve this classifier by adding features and optimisations to handle (1) poorly named files, (2) scaling to new industries, and (3) processing larger volumes of documents.

This is a real-world challenge that allows you to demonstrate your approach to building innovative and scalable AI solutions. We’re excited to see what you come up with! Feel free to take it in any direction you like, but we suggest:


### Part 1: Enhancing the Classifier

- What are the limitations in the current classifier that's stopping it from scaling?
- How might you extend the classifier with additional technologies, capabilities, or features?


### Part 2: Productionising the Classifier 

- How can you ensure the classifier is robust and reliable in a production environment?
- How can you deploy the classifier to make it accessible to other services and users?

We encourage you to be creative! Feel free to use any libraries, tools, services, models or frameworks of your choice

### Possible Ideas / Suggestions
- Train a classifier to categorize files based on the text content of a file
- Generate synthetic data to train the classifier on documents from different industries
- Detect file type and handle other file formats (e.g., Word, Excel)
- Set up a CI/CD pipeline for automatic testing and deployment
- Refactor the codebase to make it more maintainable and scalable

## Marking Criteria
- **Functionality**: Does the classifier work as expected?
- **Scalability**: Can the classifier scale to new industries and higher volumes?
- **Maintainability**: Is the codebase well-structured and easy to maintain?
- **Creativity**: Are there any innovative or creative solutions to the problem?
- **Testing**: Are there tests to validate the service's functionality?
- **Deployment**: Is the classifier ready for deployment in a production environment?


## Getting Started
1. Clone the repository:
    ```shell
    git clone <repository_url>
    cd heron_classifier
    ```

2. Install dependencies:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```shell
    python -m src.app
    ```

4. Test the classifier using a tool like curl:
    ```shell
    curl -X POST -F 'file=@path_to_pdf.pdf' http://127.0.0.1:5000/classify_file
    ```

5. Run tests:
   ```shell
    pytest
    ```

## Submission

Please aim to spend 3 hours on this challenge.

Once completed, submit your solution by sharing a link to your forked repository. Please also provide a brief write-up of your ideas, approach, and any instructions needed to run your solution. 
