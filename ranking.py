
import os, sys, shutil

def gr():
    c = 1
    class Classement :
        def __init__(self, name, points):
            self.name = name
            self.points = points
        def __repr__(self):
            return self.name + ' : ' + str(self.points) + 'pts'
    if __name__ == '__main__':
        epis = [
            Classement('BadHater', 0),
            Classement('Isaac', 0),
            Classement('Vaillant Heros', 0),
            Classement('Nameless', 0),
            Classement('Smada', 0),
            Classement('Jean Robert', 0),
            Classement('Said Mohamed', 0),
            Classement('Insmane', 0),
            Classement('Imrane', 0),
            Classement('Abdel', 0),
            Classement('Cindy', 0),
            Classement('Patrick', 0),
            Classement('Ange Monkam', 0),
            Classement('Maxime Ktms', 0),
            Classement('Lorenzo', 0),
            Classement('Best-Boy', 0),
            Classement('Le Prometteur', 0),
            Classement('Kitambala', 0),
            Classement('Zender', 0)
            ]
        epis.sort(key = lambda x: (-x.points, x.name)
        for x in epis:
            print(c, x)
            c += 1
        print('\n')
        choix = int(input('''\n-->1 - Retour à l'accueil.(home)\n-->2 - Quit\n\nchoisissez une option (1/2) : '''))
        if choix == 1:
             home()
        elif choix == 2:
             sys.exit()
def dr():
    c = 1
    class Classement :
        def __init__(self, name, points):
            self.name = name
            self.points = points
        def __repr__(self):
            return self.name + ' : ' + str(self.points) 
    if __name__ == '__main__':
        epis = [
            Classement('BadHater', 0),
            Classement('Isaac', 0),
            Classement('Vaillant Heros', 0),
            Classement('Nameless', 0),
            Classement('Smada', 0),
            Classement('Jean Robert', 0),
            Classement('Said Mohamed', 0),
            Classement('Insmane', 0),
            Classement('Imrane', 0),
            Classement('Abdel', 0),
            Classement('Cindy', 0),
            Classement('Patrick', 0),
            Classement('Ange Monkam', 0),
            Classement('Maxime Ktms', 0),
            Classement('Lorenzo', 0),
            Classement('Best-Boy', 0),
            Classement('Le Prometteur', 0),
            Classement('Kitambala', 0),
            Classement('Zender', 0)
            ]
        epis.sort(key = lambda x: x.name)#, reverse = True)
        for x in epis:
            print(c, x)
            c += 1
        print ('\n')
        choix = int(input('''\n-->1 - Retour à l'accueil (home)\n-->2 - Quit\n\nchoisissez une option (1/2) : '''))
        if choix == 1:
             home()
        elif choix == 2:
             sys.exit()

def upd():
    os.chdir('/data/data/com.termux/files/home')
    shutil.rmtree('ranking')
    os.system('git clone https://github.com/ZarguiJack/ranking')
    os.chdir('/data/data/com.termux/files/home/ranking')
    os.system('python ranking.py')
    sys.exit()

def home():
 os.system('clear')
 print('''
╔═══╗╔═══╗╔═╗─╔╗╔╗╔═╗╔══╗╔═╗─╔╗╔═══╗
║╔═╗║║╔═╗║║║╚╗║║║║║╔╝╚╣─╝║║╚╗║║║╔═╗║
║╚═╝║║║─║║║╔╗╚╝║║╚╝╝──║║─║╔╗╚╝║║║─╚╝
║╔╗╔╝║╚═╝║║║╚╗║║║╔╗║──║║─║║╚╗║║║║╔═╗
║║║╚╗║╔═╗║║║─║║║║║║╚╗╔╣─╗║║─║║║║╚╩═║
╚╝╚═╝╚╝─╚╝╚╝─╚═╝╚╝╚═╝╚══╝╚╝─╚═╝╚═══╝
''')
 option = int(input('''
1- Classement Général (General Ranking)
2- Classement Du Jour (Ranking of de day)
3- Mise à jour (update)
4- Quit

choose an option: '''))
 print('\n')
 if option == 1:
     gr()
 elif option == 2:
     dr()
 elif option == 3:
     upd()
 elif option == 4:
     sys.exit()
home()
