from pyguard.core import PyGuard
from pyguard.rules import RuleManager, RegexRule

class TestPyGuard(object):
    def test_manager_registration(self):
        """Can we register a manager correctly?"""
        guardian = PyGuard()

        manager = RuleManager(cmd='echo hello world')
        manager.register_rule(
                RegexRule(regex='foo')
            )
        guardian.register_manager(manager)
        guardian.apply_managers(file_path='foo.txt')
