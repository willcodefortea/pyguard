class PyGuard(object):
    def __init__(self):
        self.managers = []

    def register_manager(self, manager):
        """Record a manger to test against"""
        if manager not in self.managers:
            self.managers.append(manager)

    def apply_managers(self, file_path):
        """Apply our managers to the file path, breaking at the first match"""
        for manager in self.managers:
            result = manager.apply_rules(file_path)
            if result:
                # If we have a result, then simply print to console.
                # TODO: logging!
                print result

# Primary hook for the rest of the app
guardian = PyGuard()
