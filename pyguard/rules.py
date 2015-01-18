import re
from subprocess import check_output

class RuleManager(object):
    """Primary object responsible for managing and executing commands.
    """
    def __init__(self, cmd):
        self.cmd = cmd
        self.rules = []

    def register_rule(self, rule):
        """Keep track of the applied rules"""
        if rule not in self.rules:
            self.rules.append(rule)

    def register_rules(self, *args):
        """Register multiple rules at once"""
        for rule in args:
            self.register_rule(rule)

    def apply_rules(self, filepath):
        """Check file path against our rules, breaking on the first match"""
        result = None
        for rule in self.rules:
            matches, dynamic_augmentations = rule.match(filepath)
            if matches:
                augmentation = rule.cmd_augmentation
                augmentation.update(dynamic_augmentations)
                result = self.execute_command(augmentation)
                break
        return result

    def execute_command(self, cmd_augmentation):
        """Execute the given command applying an augmentation"""
        cmd = self.cmd.format(**cmd_augmentation)
        res = check_output(cmd.split(' '))
        return res

class RegexRule(object):
    """Use regular expressions to match file paths."""
    def __init__(self, regex, cmd_augmentation=None):
        self.cmd_augmentation = cmd_augmentation if cmd_augmentation else {}
        self.regex_raw = regex
        self.regex = re.compile(regex)

    def match(self, filepath):
        """Applies the rule."""
        if filepath.endswith('.pyc'):
            # Don't bother with compiled python files.
            return False, {}
        match = self.regex.match(filepath)
        dynamic_augmentations = match.groupdict() if match else {}
        return bool(match), dynamic_augmentations
