from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
    author="weizart",
    description="A package for detecting emotions in text using Watson NLP",
    keywords="emotion detection, nlp, watson",
    python_requires='>=3.11',
) 