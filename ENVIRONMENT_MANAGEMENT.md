# Environment Management

There are two different environments you will need to manage. 

1. development - This is the environment that you use to develop your code.
2. production - This specifies how to recreate a known-working environment to run your code in. 

The development environment will include some packages that the production code doesn't need (such as pytest) 

One very common problem occurs when code is modified using an updated version of a package in the development 
environment. The code is then published and the production environment is built. As this does not include the 
updated package information the code does not work. 

One strategy for combating this problem is to have your build refer to your production environment. 

A good convention if using anaconda for your development environment is to use pip as your production incitement as it 
is more varsities, however, conda is more user friendly.  

### Conda vs. PiP

There are two options for environment management present at RES with benefits and drawbacks. 
- **[Anaconda](https://www.anaconda.com/products/individual)** 
[conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 
defined in the `enviroment.yml` file 
  - **Advantages**:
    - Anaconda makes getting started with python and environments easier as it comes pre-populated with libraries aimed
    at doing scientific data analysis and data science.
  - **Disadvantages**
    - Anaconda can be very picky about how environments are created and due to the pre-populated libraries can cause 
    confusion as they may be needed for your tool to run however are not specified in the environment.yml 
- [PiP virtual environments](https://docs.python.org/3/tutorial/venv.html) defined in `requirements.txt`
  - **Advantages**:
    - virtual environments are the most explicit way of defining the libraries that need to be installed for your 
    project to work correctly. 
  - **Disadvantages**
    - virtual environments have a slightly steeper learning curve than conda environments.  