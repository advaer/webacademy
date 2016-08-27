class ClientProcessing(object):
    """
    Client Processing Logic
    """
    def __init__(self):
        self.is_login = False

    def process(self, data):
        # Parsing commands and args
        data = data.decode('UTF-8').split()
        self.command, self.args = data[0], data[1:]

        # Switch commands
        known_commands = {
            'login': self._login,
            'logout': self._logout,
            'square': self._square,
            'exit': self._exit,
        }

        if self.command in known_commands:
            return known_commands[self.command](*self.args)
        else:
            return 'ERROR! Unknown command!'

    def _login(self, *args):
        if not self.is_login:
            self.is_login = True
            return 'OK! User logged in'
        else:
            return 'ERROR! User is already logged in. Log out first!'

    def _logout(self):
        if self.is_login:
            self.is_login = False
            return 'OK! User logged out'
        else:
            return 'ERROR! User is not logged in. Log in first!'

    @staticmethod
    def _square(*args):
        if args:
            return "OK! {0}**2 = {1}".format(args[0], int(args[0])**2)
        else:
            return 'ERROR! No arguments to square'

    def _exit(self):
        pass
