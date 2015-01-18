from filewatch import file_updated_subject, Watcher

from pyguard.core import guardian
from pyguard.observer import GuardianObserver
from pyguard.rules import RuleManager, RegexRule

manager = RuleManager(cmd='py.test pyguard -s')
manager.register_rules(
        RegexRule(regex=r'.*/pyguard/.*'),
    )

guardian.register_manager(manager)

# Set up our file observer
file_updated_subject.register_observer(GuardianObserver())

# Get our watcher going
watcher = Watcher()
watcher.run()
