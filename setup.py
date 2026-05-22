from setuptools import find_namespace_packages, setup

setup(
    packages=find_namespace_packages(include=["libero*", "scripts*"]),
    include_package_data=True,
    package_data={
        "libero": [
            "libero/bddl_files/**/*",
            "libero/assets/**/*",
            "libero/init_files/**/*",
        ]
    },
)
