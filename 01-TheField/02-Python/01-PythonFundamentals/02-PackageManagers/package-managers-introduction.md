
# Package Managers and Virtual Environments

A package manager is a programming language’s tool to create project environments and easily import external dependencies. When working on a project or library, you may package your project and publish it for others.

If you’re using Python in the world of data science or scientific computing, you will soon discover that Python has two main different packaging systems: ```pip``` and ```conda```. 

## Package Management And Virtual Environments

One confusing aspect of installing packages is that often times they are installed into you global Python environment by default. Therefore all the new installed packages become available globally on your system, which is great for convenience. But it also causes issues if you're working with multiple projects that require different version of the same package.

The solution of these problems is to create multiple Python environments each catered to specific needs. Each of these Python environments is totally independent of other environments. In Python world, each of these environments is called *virtual environment*.

Here we will discuss VirtualEnv, Miniconda, and Anaconda as a way create and manage environments. 

## Using pip and VirtualEnv

So, what exactly does `pip` do? `pip` is a package manager for Python. That means it’s a tool that allows you to install and manage libraries and dependencies that aren’t distributed as part of the standard library. You can find some of the most common ```pip``` commands [here](https://www.geeksforgeeks.org/12-pip-commands-for-python-developers/).

### What is VirtualEnv?
VirtualEnv provide you separate Python environement where you can install independently all your dependencies without having conflicts.

### Why should I use it?
Let's say that you want to use Flask, but for a first project you have to use an old version of it and a more recent the second one. You can't install both versions on the same enviroment. You will have conflicts and only the last installation will be kept. 
With VirtalEnv, you can create two (or more) Python enviroments and install a different version of it.

### Installation
To install it, you can simply use pip in the terminal.

```pip install virtualenv```

You can also install it using your OS package manager. For example on Ubuntu/Debian you can use:

```sudo apt-get install virtualenv```

### Usage
When it will be installed, you can create a new enviroment and then activate it so you can use it.

* To create a new one, type in you terminal:
```bash
virtualenv env
```
It will create it **in your current directory** and will be nammed `env` it's a convention but you can of course change the name if you'd like. 
Just think to use a transparent name so anyone can guess what it is.

It's possible that your terminal doesn't recognize `virtualenv`. In this case, you can use python (as it's a Python package) as follow:

```bash
python -m virtualenv env
```

* To activate it:
```bash
source env/bin/activate
```

If you changed the name `env` you have to change it in this command too.

If you successfully activated the environemennt you should see it between parenthesis in your terminal. See screenshot below.

![virtualenv](assets/screen-virtualenv-activated.png)

Now you should be all good! Congratulations, you can now install any dependencies without caring of the conflicts. 

To install dependencies use `pip` even if you normally use `pip3`. Virtualenv rebind *(create an alias)* `pip` to suit your environement.

### Check the dependencies installed in your enviroment
To check which dependencies are installed, you can type:

```pip freeze```

And if you want to write thoses in a text file. (So you can easly install them back in a new enviroment afterward)
You can use this command that will create a `requirements.txt` file and save the list of all you dependencies and versions of it in it.

```pip freeze > requirements.txt```

If you have to re-install them, you just have to do:

```pip install -r requirements.txt```

## Using conda and Anaconda

```Conda``` is an open source package management system and environment management system that runs on Windows, macOS, Linux and z/OS. The conda package and environment manager is included in all versions of Anaconda and Miniconda. We'll see this later in more detail.

The package and environment manager program bundled with Anaconda that installs and updates conda packages and their dependencies. Conda also lets you easily switch between conda environments on your local computer.

### Miniconda
A free minimal installer for conda. [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib, and a few others. Use the conda install command to install 7,500+ additional conda packages from the Anaconda repository.

Miniconda is a Python distribution that can make installing Python quick and easy even for new users.

### Anaconda
A downloadable, free, open-source, high-performance, and optimized Python and R distribution. [Anaconda](https://www.anaconda.com/) includes conda, conda-build, Python, and 250+ automatically installed, open-source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy, and many others. Use the conda install command to easily install 7,500+ popular open-source packages for data science--including advanced and scientific analytics--from the Anaconda repository. Use the conda command to install thousands more open-source packages.

Because Anaconda is a Python distribution, it can make installing Python quick and easy even for new users.

Available for Windows, macOS, and Linux, all versions of Anaconda are supported by the community.

## Well done!

You can now install an infinity of Python environement with differents version of your packages!

Note: A key difference between conda and pip is that pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.

Nothing can stop you now! *Except typos. Typos are always gonna stop you...*

![Inception!](assets/inception.gif)

## Additional Resources
- [Understanding conda and pip](https://www.anaconda.com/blog/understanding-conda-and-pip)
- [How to Use virtualenv in Python](https://learnpython.com/blog/how-to-use-virtualenv-python/)
- [Pip vs Conda: an in-depth comparison of Python’s two packaging systems](https://pythonspeed.com/articles/conda-vs-pip/)
