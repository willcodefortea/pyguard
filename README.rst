.. image:: https://travis-ci.org/benemery/pyguard.svg?branch=master
    :target: https://travis-ci.org/benemery/pyguard

.. image:: https://coveralls.io/repos/benemery/pyguard/badge.svg?branch=master
  :target: https://coveralls.io/r/benemery/pyguard?branch=master

PyGuard
=======

A python auto test runner inspired by the `guard <https://github.com/guard/guard>`_ project.

A simple example that runs all the tests when a file is modified would look something like this:

.. code-block:: python

    from filewatch import file_updated_subject, Watcher

    from pyguard import guardian, GuardianObserver, RegexRule, RuleManager

    manager = RuleManager(cmd='py.test pyguard')
    manager.register_rules(
            RegexRule(regex=r'.*/pyguard/.*'),
        )

    guardian.register_manager(manager)

    # Set up our file observer
    file_updated_subject.register_observer(GuardianObserver())

    # Get our watcher going
    watcher = Watcher()
    watcher.run()

Any ``RuleManager`` that you create will execute the given command whenever a registered rule matches a supplied file path.

To make things a little more granular, we can register a different set of rules. i.e.

.. code-block:: python

    ...

    manager = RuleManager(cmd='py.test pyguard/tests/test_{test_name}.py')
    manager.register_rules(
            RegexRule(regex=r'.*/rules.py', cmd_augmentation={'test_name' : 'rules'}),
            RegexRule(regex=r'.*/core.py', cmd_augmentation={'test_name' : 'guardian'}),
        )

    guardian.register_manager(manager)

    ...


To enforce a particular naming convention we can take things even further using named groups within the regex itself. If we have say a ``views.py`` and we know that the tests for said views exist in ``test_views.py``, then we can simple use:

.. code-block:: python

    ...

    manager = RuleManager(cmd='py.test pyguard/tests/test_{test_name}.py')
    manager.register_rules(
            RegexRule(regex=r'.*/(?P<test_name>views).py'),
        )

    guardian.register_manager(manager)

    ...
