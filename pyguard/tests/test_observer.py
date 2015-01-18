from pyguard.observer import GuardianObserver

class TestGuardianObserver(object):
    def test_guardian_notification(self):
        """Do we braodcast updates correctly?"""
        observer = GuardianObserver()
        observer.notify(file_list=['a_file.txt', 'foo.py', ])
        # No error, yay