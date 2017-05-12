from Config import Config

class Admin:
    def __init__(self):
        if Config.debug:
            self.credentialsConfig = mockCredentialsConfig()
        else:
            from CredentialsConfig import CredentialsConfig
            self.credentialsConfig = CredentialsConfig()

    def checkSuperAdminAuth(self):
        import ipaddress
        from flask import request
        pwString = request.values.get('pw')

        if pwString == self.credentialsConfig.superAdminPassword and \
                (ipaddress.ip_address(request.remote_addr) in ipaddress.ip_network('144.122.154.64/27') or
                 ipaddress.ip_address(request.remote_addr) in ipaddress.ip_network('10.143.3.55/32') or
                         ipaddress.ip_address(request.remote_addr) in ipaddress.ip_network('127.0.0.1/32')):
            return True
        else:
            raise Exception

class mockCredentialsConfig:
    superAdminPassword = "3"