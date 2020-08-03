# res-python-project-template

**_This repo is a template to be used for new python repos crated at res. When creating a new repo in GitHub this 
template can be selected._**

**_The folder structure in this repo here is a good starting point for any python project however there are elements 
that are aimed at turning your project into a package as well._**

**_This README is also a template. The headings are standard and should be used when possible. All text that is Bold and 
Italics is intended to be removed._** 

### Build Status

[![Build status](https://ci.appveyor.com/api/projects/status/5uk1h8o5n8a49uk3?svg=true)](https://ci.appveyor.com/project/RESSoftwareTeam/res-python-project-template)

**_You are encouraged to write tests for your code. Test are imperative to know your code is doing what you think it is. 
They become even more important as your project becomes larger._**

**_AppVeyor is a cloud hosted build server we have access to. If you would like to use it and get a cool passing build 
passing badge like the one above get in contact with anyone on any of the Software or Data Science teams._**

**_There are additional tools that can help you delvelop your python package from a code quality point of view. 
Two of these tools that the software teams use are:_**
- **_[CodeCov](https://codecov.io/) - for reporting what portion of your code is covered by tests._**
- **_[CodeClimate](https://codeclimate.com) - a tool for automatically reviewing the maintainability of code._** 

**_It should be noted that these tools come at a cost per user so should be deployed where appropriate. For more 
information reach out to one of the software teams._**  

### Environment Management

**_An environment is a definition of the version of python and all libraries for your code to run. As versions may 
differ from project to project it is important to have a definition of the environment your project needs to work._** 

_**No matter how you manage to control your projects environment (see below) it is imperative that the environment 
definition is kept up to date. e.g. if you pip install a package the correct version must be added to the 
requirements.txt file. (the same is true for conda install)**_

**_To facilitate use of environments and assuming most users will be starting with anaconda an environment.yml file is 
provided for creating a conda environment. Please read more about environment management 
[here](ENVIRONMENT_MANAGEMENT.md)._**

To create a conda environment in your command window:

`conda env create -f your_path\res-python-package-template\environment.yml`

This will create the `res_your_enviroment_name` environment that should be kept up to date as you add to your 
environment. 

A convenient way to add packages to your environment is to add them to your `enviroment.yml` file and run the command:

`conda env update -f your_path\res-python-package-template\environment.yml`

### Contributing

**_It is good to give some guidance about how you would like people to contribute to your project. A very good example of 
this can be found in the 
[GEM Development contribution guide](https://github.com/resgroup/gem-calculation-engine/blob/Release/CONTRIBUTING.md). 
Some simple good house keeping guidelines are suggested below:_**
- Use [PEP-0008](https://www.python.org/dev/peps/pep-0008/) style guidance
- Use branches and reviewed pull requests to add new functionality. 
([extra reading](https://nvie.com/posts/a-successful-git-branching-model/))

**_Establishing a branching strategy can be useful to help organise work when there are multiple contributes to a 
project. Simply creating feature branches and using pull requests and code reviews is very powerful. However, there are
additional branching strategies that can be useful for some projects. More reading can be found 
[here](https://nvie.com/posts/a-successful-git-branching-model/)._**

**_A useful tool for controlling your project is GitHubs ability to protect branches. Essentially a branch can be
protected ageist unwanted contribution. Good practice is to require the master branch only accept reviewed 
pull requests. It is also good to restrict these pull requests to have a passing build._** 

### Usage

[super_cool_tool.py](supper_cool_tool.py) is an end to end example of the code in this repository.

``` python
from your_python_project.the_zen_of_python import the_zen_of_python

chant_iterations = 3

for chant in range(chant_iterations):
    the_zen_of_python()
```

### Running tests

pytest should be used for testing the code during development. A host of tests can be found in the `tests` folder.

**_pytest can be configured in PyCharm or run from the command line by navigating to your project directory and 
typing `pytest`_**

### Creating A Package

**_Python package creation is relatively new at RES and the best practices are still evolving. These can be found in
[PACKAGING.md](python_packaging/PACKAGING.md). Please not the `python_packaging` folder can be removed if you are 
not intending to turn your project into a package._**

### Project Champion

**_Below is an example of the repo champions possible responsibilities. There may be other administrators, but the 
accountability should fall on one person. Its then obvious whose job it is to make sure everything is in order, and its 
obvious what needs to be done when a hand over takes place._**

The champion for this a repo is [your name](your.email@res-group.com) who accountable for:

- The usability of the repo, and ensuring user guides and READMEs are up to date
- The code quality of the repo (CODEOWNERS, pull requests, tests, and builds all help here)
- The usability of the code for other developers (retrospectives, code quality, architecture, 
and documentation all help here)

### Links

Related Repos:

* [other repos](https://github.com/resgroupm) - Description of repo
