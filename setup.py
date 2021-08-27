from setuptools import setup


tests_require = [
    "pytest",
    "pytest-env",
    "pytest-cov",
    "pytest-mock",
    "pytest-dependency",
    "pytest-aiohttp",
    "requests",
    "psutil",
    "aioresponses",
]

setup(
    name="dummy-generic",
    version="0.1.1",
    description="Testing installation of Package",
    python_requires="~=3.7",
    install_requires=["jupyter-server-proxy", "aiohttp>=3.7.4", "pytest-runner"],
    # setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={"dev": ["aiohttp-devtools"] + tests_require},
    url="https://github.com/chimmy-changa/dummy-generic",
    author="auth",
    author_email="author@email.com",
    license="MIT",
    packages=["dummy_generic"],
    entry_points={
        "console_scripts": ["say_hi = dummy_generic.get:print_hello"],
    },
    zip_safe=False,
)
