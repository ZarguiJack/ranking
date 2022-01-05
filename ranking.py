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
            Classement('BadHater', 2),
            Classement('Ie-Tech', 1),
            #Classement('Vaillant Heros', 0),
            Classement('Nameless', 1),
            Classement('Ali Dyna', 5)
            ]
        epis.sort(key = lambda x: (-x.points, x.name))
        non=0
        ni = 0
        for x in epis:
          if x.points ==0:
             epis.remove(x)
        for x in epis:
         non = non+x.points
         ni = ni+1
        print('number of participants: ', ni)
        print('number of victims: ', non)
        print('General ranking:\n')
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
            Classement('BadHater', 1),
            Classement('Ie-Tech', 0),
            Classement('Nameless', 0),
            Classement('Ali Dyna', 0),
            ]
        epis.sort(key = lambda x: (-x.points, x.name))
        print('day ranking:\n')
        
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
