from pyguard.rules import RegexRule, RuleManager

class TestRegexRule(object):
    def test_match1(self):
        """Does simple matching work?"""
        rule = RegexRule(regex='foo.txt')

        assert rule.match('foo.txt')[0]
        assert not rule.match('bar.txt')[0]

    def test_match2(self):
        """Does an actual regex work?"""
        rule = RegexRule(regex=r'(foo|bar).txt')

        assert rule.match('foo.txt')[0]
        assert rule.match('bar.txt')[0]
        assert not rule.match('foobar.txt')[0]

    def test_compiled_file(self):
        """Do we correctly ignore compiled python files?"""
        rule = RegexRule('foo.pyc')
        assert not rule.match('foo.pyc')[0]

class TestRuleManager(object):
    def test_rule_registration(self):
        """Can we register rules correctly?"""
        manager = RuleManager(cmd='echo {phrase}')

        rule1 = RegexRule('foo.txt', {'phrase': 'hello, world!'})
        rule2 = RegexRule('bar.txt', {'phrase': 'goodbye, world!'})

        manager.register_rule(rule1)
        manager.register_rule(rule2)

        result = manager.apply_rules('bar.txt')
        assert 'goodbye, world!' in result

        result = manager.apply_rules('foo.txt')
        assert 'hello, world!' in result

    def test_multiple_rule_matching(self):
        """What happens if multiple rules match?"""
        manager = RuleManager(cmd='echo {phrase}')

        rule1 = RegexRule('foo.txt', {'phrase': 'hello, world!'})
        rule2 = RegexRule('foo.txt', {'phrase': 'goodbye, world!'})

        manager.register_rule(rule1)
        manager.register_rule(rule2)

        result = manager.apply_rules('foo.txt')

        # The first filter that matches should be applied
        assert 'hello, world!' in result

    def test_multiple_rule_registratoin(self):
        """Can we register multiple rules simultaneously?"""
        manager = RuleManager(cmd='echo {phrase}')

        manager.register_rules(
                RegexRule('foo.txt', {'phrase': 'hello, world!'}),
                RegexRule('foo.txt', {'phrase': 'goodbye, world!'}),
            )

        assert len(manager.rules) == 2
