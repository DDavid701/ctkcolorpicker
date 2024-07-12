from setuptools import setup, find_packages

setup(
    name='CustomTkinter-ColorPicker',
    version='1.0',
    packages=find_packages(),
    install_requires=['customtkinter'],
    author='DDavid701',
    author_email='ddavid701@gmail.com',
    description="Simple color picker for customtkinter :)",
    url='https://github.com/DDavid701/ctkcolorpicker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)