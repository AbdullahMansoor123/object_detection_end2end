from setuptools import find_packages, setup


def get_requirements(filepath:str) -> list[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n','') for i in requirements]


setup(
    name="object_detection_end2end",
    description= "Machine learning end to end project pipeline" ,
    version="0.0.1",
    author="Abdullah",
    author_email="abdullahmansoor123@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

