import os
from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import instrument_and_import_package, instrument_and_import_module, initialise_call_hierarchy, finalise_call_hierarchy
from samples.hello_world_combiner import HelloWorldCombiner # is this import required?

# you can import and instrument entire packages / folders at once like this
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'samples'), 'samples')
# You can instrument individual modules like this
# instrument_and_import_module('tests.blah')

# this is a wrapper around the test that also outputs the documentation / sequence diagram
def test_hello_world():
    # the initialises the recording of the call hierarchy
    initialise_call_hierarchy('start')

    # This runs the actual test
    _test_hello_world()
    
    # this finalises the call hierarchy and returns the root
    root_call = finalise_call_hierarchy()

    # this returns a sequence diagram of the call hierarchy
    sequence_diagram = root_call.sequence_diagram(
        show_private_functions=False,
        excluded_functions=[
            'HelloWorldCombiner.__init__',
        ]
    )

    # this writes out the markdown to disk    
    sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'top-level-sequence-diagram.md')
    Path(sequence_diagram_filename).write_text(sequence_diagram)

    # this wouldn't be required as a user of this package, but is helpful here, 
    # to test that the generated markdown is correct
    assert sequence_diagram == """This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension) or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.

You can also [view it full screen as an SVG](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5IZWxsb1dvcmxkQ29tYmluZXIuY29tYmluZTogY2FsbHMgeDEKICBIZWxsb1dvcmxkQ29tYmluZXIuY29tYmluZS0+PmhlbGxvOiBjYWxscyB4MQogIGhlbGxvLS0+PkhlbGxvV29ybGRDb21iaW5lci5jb21iaW5lOiByZXR1cm5zIHN0cgogIEhlbGxvV29ybGRDb21iaW5lci5jb21iaW5lLT4+d29ybGQ6IGNhbGxzIHgxCiAgd29ybGQtLT4+SGVsbG9Xb3JsZENvbWJpbmVyLmNvbWJpbmU6IHJldHVybnMgc3RyCiAgSGVsbG9Xb3JsZENvbWJpbmVyLmNvbWJpbmUtLT4+c3RhcnQ6IHJldHVybnMgc3RyCg==)        

```mermaid
sequenceDiagram
  start->>HelloWorldCombiner.combine: calls x1
  HelloWorldCombiner.combine->>hello: calls x1
  hello-->>HelloWorldCombiner.combine: returns str
  HelloWorldCombiner.combine->>world: calls x1
  world-->>HelloWorldCombiner.combine: returns str
  HelloWorldCombiner.combine-->>start: returns str

```
"""

# this is the original / source test
def _test_hello_world():
    assert HelloWorldCombiner().combine() == 'Hello world'




