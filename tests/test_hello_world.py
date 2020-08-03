import os
from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import instrument_and_import_package, instrument_and_import_module, initialise_call_hierarchy, finalise_call_hierarchy
from samples.hello_world_combiner import HelloWorldCombiner

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

def _test_hello_world():
    assert HelloWorldCombiner().combine() == 'Hello world'




