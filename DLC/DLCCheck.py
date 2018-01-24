import os.path

class DLCCheck():

    @classmethod
    def CheckDLC(self):
        path = "DLCKeys/dlckey.key"
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)

        if os.path.isfile(canonicalized_path):
            return True
        else:
            return False
