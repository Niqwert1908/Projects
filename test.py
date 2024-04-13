from random import randint
from time import sleep
from pyautogui import prompt, alert, confirm
import pygame

pygame.init()
clock = pygame.time.Clock()

screenSize = (400, 400)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("DnD")

White = (255, 255, 255)  
Black = (0, 0, 0)

fontStyle = pygame.font.SysFont('Verdana', 15) 

class Human:
    def __init__(self):
        print("Вы теперь человек")

class Elf:
    def __init__(self):
        print("Вы теперь эльф")

class Lizard:
    def __init__(self):
        print("Вы теперь ящер")

class Gnome:
    def __init__(self):
        print("Вы теперь гном")

class Undead:
    def __init__(self):
        print("Вы теперь нежить")

class Species(Human, Elf, Lizard, Gnome, Undead):
    def __init__(self, spec):
        listSpec = [Human.__init__, Elf.__init__, Lizard.__init__, Gnome.__init__, Undead.__init__]
        listSpec[spec](self)
        
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Black)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        
    def update(self):
        self.rect.x +=5
        
class Character(Species, Sprite):
    def __init__(self, hp, mana, attack, spec):
        self.spec = super().__init__(spec)
        # Sprite.__init__(self)
        self.hp = hp
        self.powAttack = attack
        self.mana = mana
    
    def dealDamage(self, char, bool = True):
        if bool:
            char.hp -= randint(self.powAttack - 5, self.powAttack + 5)
          
class Archer(Character):
    def __init__(self, hp = 100, mana = 100, attack = 20, spec = 0):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь лучник")
        
    def super(self):
        self.invise = True

class Wizard(Character):
    def __init__(self, hp = 100, mana = 150, attack = 10, spec = 0):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь волшебник")
        
    def super(self):
        pass  
  
class Warrior(Character):
    def __init__(self, hp = 150, mana = 50, attack = 30, spec = 0):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь воин")
        
    def super(self):
        pass

class Barbarian(Character):
    def __init__(self, hp = 150, mana = 0, attack = 40, spec = 0):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь варвар")
        
    def super(self):
        pass        
    
class Zombi(Character):
    def __init__(self, hp = 150, mana = 0, attack = 40, spec = 4):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь зомби")
        
    def super(self):
        pass


class Skeleton(Character):
    def __init__(self, hp = 150, mana = 0, attack = 40, spec = 4):
        super().__init__(hp, mana, attack, spec)
        print("Вы теперь нежить")
        
    def super(self):
        pass    
    
# def message(text):
#     for i in  text:
#         print(i, end="")
#         sleep(0.03)
#     print()

def message(inpText):
    output = ""
    y = 5
    for i in  inpText:
        if len(output) > 40:
            y += 15
            output = ""
        output += i
        text = fontStyle.render(output, True, Black)
        screen.blit(text, (5, y))
        pygame.display.flip()
        sleep(0.03)
            
def persStart():
    classPers = ["Лучник", "Волшебник", "Воин", "Варвар"]
    historyOfCharacter = {
    "Лучник" : "Элиана Сумрачный ВетерЭлиана, выросшая в глухих лесах, известна своим непревзойденным мастерством в стрельбе из лука. Она — последняя из древнего клана лесных стражей, обученная искусству скрытности и точности. Её стрелы всегда находят цель, а её умение оставаться незамеченной в лесу делает её ценным союзником в любом квесте.",
    "Волшебник" : "Мерлинус СветозарМерлинус — ученик забытых магических искусств, обладающий глубокими знаниями древних заклинаний. Он посвятил свою жизнь изучению арканы и поиску потерянных магических артефактов. С его магической силой, способной управлять стихиями, он стал одним из самых уважаемых магов в земле.",
    "Воин" : "Торгард Железный ЩитТоргард, непоколебимый воин из высокогорных кланов, вооруженный мечом и щитом, известен своей несокрушимой волей и стойкостью в бою. Он сражался в бесчисленных битвах и всегда стоял на передовой, защищая своих товарищей и отражая атаки врагов.",
    "Варвар" : "Гримнор Дикая БуряГримнор, варвар с северных пустошей, известен своей дикой силой и берсеркерской яростью в бою. Отвергнутый своим племенем за непокорность, он путешествует по миру в поисках новых испытаний и возможности доказать свою силу и отвагу."}   
        
    flag = 0
    while flag == 0:
        choiseClass = 0
        while choiseClass == 0:
            try:
                choiseClass = int(prompt("Давайте выберем подходящего вам героя: \n1. Лучник \n2. Волшебник \n3. Воин \n4. Варвар"))
            except:
                choiseClass = 0
                alert("Нужно ввести цифру от 1 до 4")
            if choiseClass < 5 and choiseClass > 0:
                break
            choiseClass = 0
        alert(f"{historyOfCharacter[classPers[choiseClass-1]]}") 
        flag = 1 if confirm(f"Ваш выбор {classPers[choiseClass-1]}. Вы уверены?") == "OK" else 0
    flag = 0
    while flag == 0:
        choiseRasa = 0
        while choiseRasa == 0:
            try:
                choiseRasa = int(prompt("Теперь укажем расу для вашего персонаж: \n1. Человек \n2. Эльф \n3. Ящер \n4. Гном \n5. Нежить") )
            except:
                choiseRasa = 0
                alert("Нужно ввести цифру от 1 до 5")
            if choiseRasa < 6 and choiseRasa > 0:
                break
            choiseRasa = 0
        flag = 1 if confirm("Подтвердить?") == "OK" else 0
    return (choiseClass, choiseRasa)
        

hero = persStart()
hero = Archer(spec = hero[1])

screen.fill(Black)    

# message("Добро пожаловать, благородные искатели приключений, в мир, где фантазия оживает, и каждый выбор может привести к славе или погибели.\
# Соберитесь, герои, ведь перед вами раскинулся мир Dungeons & Dragons, полный тайн и чудес, опасностей и вознаграждений.\
# Сегодня вы начнете путешествие, которое испытает вашу смекалку, мужество и верность товарищам.\
# Ваши персонажи станут живыми легендами, чьи истории будут пересказывать веками.\
# Отважные воины, мудрые маги, хитрые разбойники и благородные паладины — каждый из вас играет роль в этой эпической саге.\
# Пусть ваши кости ложатся удачно, ваш интеллект направляет вас к правильным решениям, а ваше сердце ведет вас к истинной доблести.\
# Поднимите свои мечи, разверните свитки и приготовьтесь к приключениям, которые останутся с вами навсегда.\
# Так начнется ваша история. Пусть она будет полна героизма и величия. Приключения ждут!")     

# Ожидание нажатия мышки\ Можно будет вынести в отдельную функцию и юзать в диалогах
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONDOWN:
        break



frameImages = []
for i in range(6):
    frameImages.append(pygame.image.load(f"Warrior_Idle{i}.png"))
currentFrame = 0    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # hero.update()        
    screen.fill(White)
    screen.blit(frameImages[currentFrame], (20, 20))
    sleep(0.1)
    # Всплывающее окно с кнопкой окей
    # if currentFrame == 3:
    #    pyautogui.confirm("you have done this")
    # pyautogui.prompt("")
    # pyautogui.alert("")
    if currentFrame < 4:
        currentFrame += 1
    else:
        currentFrame = 0
    pygame.display.flip()
            
    clock.tick(60)
    
