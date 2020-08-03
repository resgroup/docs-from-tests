from typing import List
import base64

class CallHierarchy:
    def __init__(
            self,
            function_name: str,
            return_value: str):
        self._function_name = function_name
        self._return_value = return_value
        self._times_called = 1
        self._functions_called = dict()

    def add_called_function(self, function_called): # function_called is a CallHierarchy
        if function_called._function_name in self._functions_called:
            self._functions_called[function_called._function_name]._times_called += 1
        else:
            self._functions_called[function_called._function_name] = function_called

    def sequence_diagram(
            self, 
            show_private_functions: bool,
            excluded_functions: List[str]):
        mermaid_sequence_diagram = 'sequenceDiagram\n' + self._sequence_diagram(show_private_functions, excluded_functions)
        mermaid_sequence_diagram_base64 = base64.b64encode(mermaid_sequence_diagram.encode('utf-8')).decode('utf-8')

        plugin_links = 'This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension)'
        plugin_links += ' or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.'
        svg_link = f'You can also [view it full screen as an SVG](https://mermaid.ink/svg/{mermaid_sequence_diagram_base64})'

        return f"""{plugin_links}

{svg_link}        

```mermaid
{mermaid_sequence_diagram}
```
"""

    def _sequence_diagram(
            self, 
            show_private_functions: bool,
            excluded_functions: List[str]):
        functions_after_exclusions = dict(filter(lambda function_called: function_called[0] not in excluded_functions, self._functions_called.items()))
        
        if show_private_functions:
            functions_after_exclusions_and_private = functions_after_exclusions
        else:
            functions_after_exclusions_and_private = dict(filter(self._is_public_function, functions_after_exclusions.items()))
        
        result = ''
        for function_name in functions_after_exclusions_and_private:
            result += f'  {self._function_name}->>{function_name}: calls x{functions_after_exclusions_and_private[function_name]._times_called}\n'
            result += functions_after_exclusions_and_private[function_name]._sequence_diagram(show_private_functions, excluded_functions)
            result += f'  {function_name}-->>{self._function_name}: returns {functions_after_exclusions_and_private[function_name]._return_value}\n'

        return result

    def _is_public_function(self, function_name_and_value):
        function_name = function_name_and_value[0]
        if ".__init__" in function_name:
            return True

        if function_name.startswith('_'):
            return False

        if "._" in function_name:
            return False

        return True
