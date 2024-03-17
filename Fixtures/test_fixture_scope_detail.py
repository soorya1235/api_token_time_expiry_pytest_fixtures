"""
Fixture Scopes:

Fixtures are created when first requested by a test and are destroyed based on there scope.
function : the default scope, the fixture is destroyed at the end of test
class : the fixture is destroyed during teardown of the last test in the class
module : the fixture is destroyed during teardown of the last test in the module
package : the fixture is destroyed during teardown of the last test in the package
session : the fixture is destroyed at the end of test session
https://docs.pytest.org/en/stable/explanation/fixtures.html

"""