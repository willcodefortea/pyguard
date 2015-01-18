from filewatch.observer import ObserverBase
from pyguard.core import guardian

class GuardianObserver(ObserverBase):
    def notify(self, file_list):
        for filepath in file_list:
            guardian.apply_managers(filepath)
