# docs-from-tests

This python package contains functions to instrument your code / tests to create a sequence diagram (in markdown / mermaid) as the tests run.  

The sequence diagram shows the runtime call hierachy of the code. It creates files in the repository, which you should check. 

You can choose to ignore specific functions, and private functions, to make the diagram readable in each context you are interested in. 

The diagram is useful documentation, and will stay up to date as it is automatically generated. Hopefully it will encourage us to have useful diagrams in the repo, with the appropriate levels of detail, which in turn will encourage us to structure the code well so it produces good diagrams, andto  have tests at these levels of detail. 

## Build Status

[![Build status](https://ci.appveyor.com/api/projects/status/h22ya2rrsl8bc4pt?svg=true)](https://ci.appveyor.com/project/RESSoftwareTeam/docs-from-tests)

## Contributing

- Use [PEP-0008](https://www.python.org/dev/peps/pep-0008/)
- Please open up an Issue for new work, where any discussion can take place, and then submit a pull request to fix the issue.

## Usage

You can see an example of instrumenting a test at [tests\test_hello_world.py](tests\test_hello_world.py)

## Running tests

- `set pythonpath=<path to root of this repo>`
- `pytest`

## Project Champion

The champion for this a repo is [Cedd Burge](cedd.burge@res-group.com) who is accountable for:

- The usability of the repo, and ensuring user guides and READMEs are up to date
- The code quality of the repo (CODEOWNERS, pull requests, tests, and builds all help here)
- The usability of the code for other developers (retrospectives, code quality, architecture, 
and documentation all help here)