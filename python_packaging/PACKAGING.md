# Python Package Guidance

Creating some code that does cool stuff is good. But creating code that allows other to do cool stuff too is better!

Creating python packages is fairly straight forward, also seems to be an evolving landscape, below are some 
guidelines to help steer through these uncharted waters. 

### Examples

- `res_your_package_name` is an example of a basic package. 
- `resgroup` is an example of a name space package. (see below)

### Environment Management

Environment management will now get more confusing and easier to get wrong. Not only do you have your develop and 
production enviroments to manage you now have to manage you package dependencies. These are managed in 
`setup.py` in the `install_requires` list.

- `setup.py` specifies how to build and install your package. So it's the thing you use to let package-install tools 
know what dependencies your package has that must be installed in order for it to function at all.

- `requirements.txt` specifies how to recreate a known-working environment to run your code in. 
So it's the thing you use to let a deployment tool know about the specific setup you want to use when actually running 
your application.

For example, you might have a package which requires the foolib library, and can use any version from 2.3 onwards; you 
could specify foolib>=2.3 in your setup.py as a dependency, and any time someone installed your package, their install 
tool would know to go grab a compatible version of foolib and install it.

But your production environment at work may be using specifically foolib 2.3.5, and so whenever you deploy that's the 
at work version you want. In that case your requirements.txt can specify foolib==2.3.5 to guarantee that's the specific 
version you get when deploying.

### setup.py

The `setup.py` file should be copied into the root of the package repo. This file is used for packaging your code. 
`setup.py` makes use of the [setuptools](https://setuptools.readthedocs.io/en/latest/) library to package your code 
so it is consumable by other projects. Your code must be structured as as a 
[python package](https://packaging.python.org/tutorials/packaging-projects/). 

It should be noted that `setup.py` will need to be modified before use. Pay close attention to: 
- Use the naming conventions below
- [Semantic Versioning](https://semver.org/) should be used
- Install requirements must be passed if your package has specific dependencies

### Python Package Name Conventions

#### A note on package naming

There are two different names that are very important to consider. 

1. The name of your package in setup.py
2. The name of the package folder in your repo

It is worth noting that these two names do not have to be the same. The standard for setup.py is to use dashes for word 
separators rather than underscore. However, the convention for folder names is to use underscore.

#### Basic convention

- The prefix 'res_' should be used for all res packages.
- After 'res_', short, all-lowercase names, preferably one word, should be used. If the name is multiple words 
underscores (_) as word separators should be used.
- Singular nouns should be used. (e.g. res_turbine_layout instead of res_turbine_layouts)
- US English instead of UK English should be used. (e.g. optimization instead of optimisation)

#### Name Space packages

Name space packages are a very interesting concepts. An example of the structure needed can be found 
[here](https://packaging.python.org/guides/packaging-namespace-packages/). 

This has not been adopted at RES, however, it looks like a good idea. 