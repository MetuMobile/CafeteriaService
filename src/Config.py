from os import path


class Config:
    serverType = "Deployment"
    serverIp = "144.122.156.67"
    serverPort = 1071
    os = 'Linux'
    debug = False

    home = path.dirname(path.abspath(__file__))
    APP_DIR = home
    dynamicFilesFolderPath = path.join(home, 'dynamicFiles')

    # staticFolderPath = path.join(home, "imageUploads")
    # dynamicFolderPath = path.join(home, "dynamicImages")
    # loggerPath = path.join(home, 'log.txt')
    # cafeteriaMenuExcelPath = path.join(home, 'Cafeteria', 'cafeteriaMenu.xlsx')

    staticFolderPath = "/home/ncc-mobileapp/metumobile2/imageUploads/"
    dynamicFolderPath = "/home/ncc-mobileapp/metumobile2/dynamicImages/"
    loggerPath = 'log.txt'
    cafeteriaMenuExcelPath = '/home/ncc-mobileapp/metumobile2/Cafeteria/cafeteriaMenu.xlsx'

    serverRootLink = "http://" + serverIp + ":" + str(serverPort) + "/api"
    servicesLink = serverRootLink + "/"

    services = {}

    services['weather'] = {}
    services['weather']['url'] = serverRootLink + "/services/weather/v1"
    services['weather']['port'] = 1073

    services['cafeteria'] = {}
    services['cafeteria']['url'] = serverRootLink + "/services/cafeteria/v1"
    services['cafeteria']['port'] = 1074

    services['announcement'] = {}
    services['announcement']['url'] = serverRootLink + "/services/announcement/v1"
    services['announcement']['port'] = 1075

    services['phonebook'] = {}
    services['phonebook']['url'] = serverRootLink + "/services/phonebook/v1"
    services['phonebook']['port'] = 1076