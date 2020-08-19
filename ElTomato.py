import sys
import pygame
import random
import math
import hashlib

pygame.init()
clock = pygame.time.Clock()
largura, altura = 800, 600
canvas = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("El Tomato")
font = pygame.font.SysFont("papyrus", 50)
font2 = pygame.font.Font("./Data/Fonte/Pixeled.ttf", 30)
BestScore = 0
#Get BestScore:
def GetBestScore():
    arquivo = open("./Data/Score/BestScore.txt")
    x = arquivo.read()
    arquivo.close
    if x =='':
        return 0

    i = 0
    while i < 25000 and x != '':
        Crypt = hashlib.md5(str(i).encode("utf-8")).hexdigest()
        if x == Crypt:
            return i
        i +=1
    
    return 0
    
BestScore = GetBestScore()

# bottoms
#region
StartBottom = pygame.Rect(315, 141, 169, 46)
ExitBottom = pygame.Rect(315, 431, 169, 56)
VolumeUp = pygame.Rect(428, 215, 47, 29)
VolumeDown = pygame.Rect(428, 262, 47, 29)
EffectsUp = pygame.Rect(428, 319, 47, 29)
EffectsDown = pygame.Rect(428, 365, 47, 29)

ContBottom = pygame.Rect(231,140,329,47)
MenuPauseBottom = pygame.Rect(306,236,179,47)
VolumeUpPause = pygame.Rect(315,309,47,29)
VolumeDownPause = pygame.Rect(315,347,47,29)
EffectsUpPause = pygame.Rect(494,309,47,29)
EffectsDownPause = pygame.Rect(494,347,47,29)
ExitPauseBottom = pygame.Rect(315,413,160,47)
#endregion

# Imagens
#region
BackGround = pygame.image.load("./Data/Background/Default/000.png")
Barney = pygame.image.load("./Data/Images/michaelbarney.png")
Menu = pygame.image.load("./Data/Background/Default/MENU.png")
pause_back = pygame.image.load("./Data/Background/Default/pause_back.png")
BackGround = pygame.transform.scale(BackGround, (largura, altura))


# self
PlayerR = [pygame.image.load("./Data/Player/walking/000.png"), pygame.image.load("./Data/Player/walking/001.png"),
           pygame.image.load(
               "./Data/Player/walking/002.png"), pygame.image.load("./Data/Player/walking/003.png"),
           pygame.image.load(
               "./Data/Player/walking/004.png"), pygame.image.load("./Data/Player/walking/005.png"),
           pygame.image.load("./Data/Player/walking/006.png"), pygame.image.load("./Data/Player/walking/007.png")]
PlayerL = [pygame.image.load("./Data/Player/walkingleft/000.png"), pygame.image.load("./Data/Player/walkingleft/001.png"),
           pygame.image.load(
               "./Data/Player/walkingleft/002.png"), pygame.image.load("./Data/Player/walkingleft/003.png"),
           pygame.image.load(
               "./Data/Player/walkingleft/004.png"), pygame.image.load("./Data/Player/walkingleft/005.png"),
           pygame.image.load("./Data/Player/walkingleft/006.png"), pygame.image.load("./Data/Player/walkingleft/007.png")]
for x in range(0, 8):
    PlayerR[x] = pygame.transform.scale(PlayerR[x], (64, 64))
    PlayerL[x] = pygame.transform.scale(PlayerL[x], (64, 64))

# Inimigos
EnemieImage = pygame.image.load("./Data/Images/inimigo.png")
EnemieImage2 = pygame.image.load("./Data/Images/inimigo2.png")
BossImage = pygame.image.load("./Data/Images/boss.png")
BossImageTransp = BossImage.convert()
BossImageTransp.set_alpha(0)
SuperBoss = pygame.image.load("./Data/Images/cabage.png")
SuperBossBolado = pygame.image.load("./Data/Images/cabagefullpistola.png")

# Gadgets/Ações
lifeBox = pygame.image.load("./Data/Images/lifebox.png")
lifeBox = pygame.transform.scale(lifeBox, (32, 32))

TestosteronaImg = pygame.image.load("./Data/Images/testosterona.png")
TestosteronaImg = pygame.transform.scale(TestosteronaImg, (16, 32))

HitMark = pygame.image.load("./Data/Images/xplogion.png")

Tiro = pygame.image.load("./Data/Images/laser.png")
Tiro = pygame.transform.scale(Tiro, (20, 5))
# - | / \
DirecaoDisparo = [pygame.transform.rotate(
    Tiro, 0), pygame.transform.rotate(Tiro, 90), pygame.transform.rotate(Tiro, 45), pygame.transform.rotate(Tiro, -45),
     pygame.transform.rotate(Tiro, 22.5), pygame.transform.rotate(Tiro, 67.5),
    pygame.transform.rotate(Tiro, 112.5), pygame.transform.rotate(Tiro, 157.5), pygame.transform.rotate(Tiro, 202.5),
     pygame.transform.rotate(Tiro, 247.5), pygame.transform.rotate(Tiro, 292.5),
    pygame.transform.rotate(Tiro, 337.5)]

LifeBar = [pygame.image.load("./Data/life/life-0.png"), pygame.image.load("./Data/life/life-10.png"),
           pygame.image.load(
               "./Data/life/life-20.png"), pygame.image.load("./Data/life/life-30.png"),
           pygame.image.load(
               "./Data/life/life-40.png"), pygame.image.load("./Data/life/life-50.png"),
           pygame.image.load(
               "./Data/life/life-60.png"), pygame.image.load("./Data/life/life-70.png"),
           pygame.image.load(
               "./Data/life/life-80.png"), pygame.image.load("./Data/life/life-90.png"),
           pygame.image.load("./Data/life/life-100.png")]
for x in range(0, 11):
    LifeBar[x] = pygame.transform.scale(LifeBar[x], (158, 24))

AmmoBar = [pygame.image.load("./Data/ammo/ammo0.png"),pygame.image.load("./Data/ammo/ammo1.png"),pygame.image.load("./Data/ammo/ammo2.png"),
            pygame.image.load("./Data/ammo/ammo3.png"),pygame.image.load("./Data/ammo/ammo4.png"),pygame.image.load("./Data/ammo/ammo5.png"),
            pygame.image.load("./Data/ammo/ammo6.png"),pygame.image.load("./Data/ammo/ammo7.png")]
for x in range(0,8):
    AmmoBar[x] = pygame.transform.scale(AmmoBar[x], (76, 24))

TestosteronaBar = [pygame.image.load("./Data/testosterona/testosterona0.png"),pygame.image.load("./Data/testosterona/testosterona1.png"),pygame.image.load("./Data/testosterona/testosterona2.png"),
                    pygame.image.load("./Data/testosterona/testosterona3.png"),pygame.image.load("./Data/testosterona/testosterona4.png"),pygame.image.load("./Data/testosterona/testosterona5.png"),
                    pygame.image.load("./Data/testosterona/testosterona6.png"),pygame.image.load("./Data/testosterona/testosterona7.png")]
for x in range(0,8):
    TestosteronaBar[x] = pygame.transform.scale(TestosteronaBar[x], (24,76))

ScoreSquare = pygame.image.load("./Data/Images/scoresquare.png")
ScoreSquare = pygame.transform.scale(ScoreSquare, (140,40))

instruction = pygame.image.load("./Data/Images/instructions.png")
press_i = pygame.image.load("./Data/Images/press_i.png")

# endregion

# Sons
#region

pygame.mixer.music.load('./Data/sounds/el tomato theme mastered.wav')
MusicVolume = 0.3
EffectsVolume = 0.3
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(MusicVolume)
Sounds = []
Sounds.append(pygame.mixer.Sound('./Data/sounds/pewpew.wav'))
#heal
Sounds.append(pygame.mixer.Sound('./Data/sounds/Heal.wav'))
# gemido
Sounds.append(pygame.mixer.Sound('./Data/sounds/ein.wav'))
# Atropelado
Sounds.append(pygame.mixer.Sound('./Data/sounds/einra.wav'))
#reload
Sounds.append(pygame.mixer.Sound('./Data/sounds/reload.wav'))
#especial
Sounds.append(pygame.mixer.Sound('./Data/sounds/bium.wav'))
#tururu
Sounds.append(pygame.mixer.Sound('./Data/sounds/turururu.wav'))

for x in range(0,7):
    Sounds[x].set_volume(EffectsVolume)
#endregion

# Classes
#region
class Model():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 64
        self.altura = 64
        self.health = 100
        self.rect = self.get_rect()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def DrawModel(self):
        pass


class Player(Model):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.team = "ALLY"
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.cont = 0
        self.lado = 1
        self.rect = self.get_rect()

        self.health = 100
        self.AmmoClip = []
        self.MaxAmmo = 7
        self.Ammo = 7

        self.TestosteronaCont = 0

    # HitBox Otimizada
    def get_rect(self):
        return pygame.Rect(self.x + 20, self.y + 8, self.largura-40, self.altura - 16)

    def DrawModel(self):
        self.rect = self.get_rect()

        if self.x <= -20:
            self.left = False
        elif self.x >= largura - self.largura + 20:
            self.right = False
        if self.y <= -8:
            self.up = False
        elif self.y >= altura - self.altura + 4:
            self.down = False

        if self.left:
            self.lado = -1
        elif self.right:
            self.lado = 1

        # Passa pelas animações
        if self.cont + 1 > 8:
            self.cont = 0

        # Todas as direções de caminhada
        if self.left and self.down:
            self.x -= 6
            self.y += 6
            canvas.blit(PlayerL[self.cont], (self.x, self.y))
        elif self.right and self.down:
            self.x += 6
            self.y += 6
            canvas.blit(PlayerR[self.cont], (self.x, self.y))
        elif self.left and self.up:
            self.x -= 6
            self.y -= 6
            canvas.blit(PlayerL[self.cont], (self.x, self.y))
        elif self.right and self.up:
            self.x += 6
            self.y -= 6
            canvas.blit(PlayerR[self.cont], (self.x, self.y))
        elif self.left:
            self.x -= 8
            canvas.blit(PlayerL[self.cont], (self.x, self.y))
        elif self.right:
            self.x += 8
            canvas.blit(PlayerR[self.cont], (self.x, self.y))
        elif self.up:
            self.y -= 8
            if self.lado == 1:
                canvas.blit(PlayerR[self.cont], (self.x, self.y))
            else:
                canvas.blit(PlayerL[self.cont], (self.x, self.y))
        elif self.down:
            self.y += 8
            if self.lado == 1:
                canvas.blit(PlayerR[self.cont], (self.x, self.y))
            else:
                canvas.blit(PlayerL[self.cont], (self.x, self.y))
        else:
            if self.lado == 1:
                canvas.blit(PlayerR[0], (self.x, self.y))
            else:
                canvas.blit(PlayerL[0], (self.x, self.y))

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.cont += 1

    def DrawLife(self):
        if self.health > 90:
            canvas.blit(LifeBar[10], (10, altura - 45))
        elif self.health <= 90 and self.health > 80:
            canvas.blit(LifeBar[9], (10, altura - 45))
        elif self.health <= 80 and self.health > 70:
            canvas.blit(LifeBar[8], (10, altura - 45))
        elif self.health <= 70 and self.health > 60:
            canvas.blit(LifeBar[7], (10, altura - 45))
        elif self.health <= 60 and self.health > 50:
            canvas.blit(LifeBar[6], (10, altura - 45))
        elif self.health <= 50 and self.health > 40:
            canvas.blit(LifeBar[5], (10, altura - 45))
        elif self.health <= 40 and self.health > 30:
            canvas.blit(LifeBar[4], (10, altura - 45))
        elif self.health <= 30 and self.health > 20:
            canvas.blit(LifeBar[3], (10, altura - 45))
        elif self.health <= 20 and self.health > 10:
            canvas.blit(LifeBar[2], (10, altura - 45))
        elif self.health <= 10 and self.health > 0:
            canvas.blit(LifeBar[1], (10, altura - 45))
        elif self.health <= 0:
            canvas.blit(LifeBar[0], (10, altura - 45))

    def DrawAmmo(self):
        if self.Ammo == 7:
            canvas.blit(AmmoBar[7], (200, altura - 45))
        elif self.Ammo == 6:
            canvas.blit(AmmoBar[6], (200, altura - 45))
        elif self.Ammo == 5:
            canvas.blit(AmmoBar[5], (200, altura - 45))
        elif self.Ammo == 4:
            canvas.blit(AmmoBar[4], (200, altura - 45))
        elif self.Ammo == 3:
            canvas.blit(AmmoBar[3], (200, altura - 45))
        elif self.Ammo == 2:
            canvas.blit(AmmoBar[2], (200, altura - 45))
        elif self.Ammo == 1:
            canvas.blit(AmmoBar[1], (200, altura - 45))
        elif self.Ammo == 0:
            canvas.blit(AmmoBar[0], (200, altura - 45))

    def DrawTestosterona(self):
        if int(self.TestosteronaCont/4) >= 3:
            canvas.blit(TestosteronaBar[7], (12, altura - 125))
        elif int(self.TestosteronaCont/4) == 2:
            canvas.blit(TestosteronaBar[6], (12, altura - 125))
        elif int(self.TestosteronaCont/4) == 1:
            canvas.blit(TestosteronaBar[5], (12, altura - 125))
        elif self.TestosteronaCont == 0:
            canvas.blit(TestosteronaBar[0], (12, altura - 125))
        elif self.TestosteronaCont == 1:
            canvas.blit(TestosteronaBar[1], (12, altura - 125))
        elif self.TestosteronaCont == 2:
            canvas.blit(TestosteronaBar[2], (12, altura - 125))
        elif self.TestosteronaCont == 3:
            canvas.blit(TestosteronaBar[3], (12, altura - 125))
        elif self.TestosteronaCont >= 4:
            canvas.blit(TestosteronaBar[4], (12, altura - 125))


class Enemie1(Model):
    def __init__(self):
        self.Proper = self.ProperXY()
        super().__init__(self.Proper[0], self.Proper[1])
        self.health = 10
        self.team = "ENEMIE"
    

    def ProperXY(self):
        self.x = random.randrange(0, largura - 64)
        self.y = random.randrange(0, altura - 64)
        while self.x > Astronauta.x - 128 and self.x < Astronauta.x + Astronauta.largura + 64 and self.y > Astronauta.y - 128 and self.y < Astronauta.y + Astronauta.altura + 64:
            self.x = random.randrange(0, largura - 64)
            self.y = random.randrange(0, altura - 64)
        return [self.x, self.y]
    #  HitBox Otimizada
    def get_rect(self):
        return [pygame.Rect(self.x + 8, self.y + 20, self.largura - 16, self.altura - 24),
                pygame.Rect(self.x + 20, self.y, self.largura - 40, self.altura - 36)]

    def DrawModel(self):
        self.rect = self.get_rect()

        if self.rect[0].colliderect(Astronauta.rect) or self.rect[1].colliderect(Astronauta.rect):
            Sounds[3].play()
            Astronauta.health -= 10
            Enemies.pop(Enemies.index(self))

        if self.x < Astronauta.x:
            self.x += Speed
        elif self.x > Astronauta.x:
            self.x -= Speed
        if self.y < Astronauta.y:
            self.y += Speed
        elif self.y > Astronauta.y:
            self.y -= Speed
        canvas.blit(EnemieImage, (self.x, self.y))


class Enemie2(Model):
    def __init__(self):
        super().__init__(0, 0)
        self.health = 40
        self.velocidade = 3
        self.position = 0
        self.EnemieAmmoClip = []
        self.team = "ENEMIE"
        self.timer = 60
        self.rect = self.get_rect()
        self.get_position(int(random.randrange(0, 4)))
    # HitBox Otimizada

    def get_rect(self):
        return pygame.Rect(self.x, self.y + 8, self.largura, self.altura - 8)

    def get_position(self, X):
        if X == 0:
            self.x = 0
            self.y = 0
            self.position = 0
        elif X == 1:
            self.x = largura - self.largura
            self.y = 0
            self.position = 1
        elif X == 2:
            self.x = 0
            self.y = altura - self.altura
            self.position = 2
        elif X == 3:
            self.x = largura - self.largura
            self.y = altura - self.altura
            self.position = 3

    def DrawModel(self):
        self.rect = self.get_rect()
        self.timer -= 2

        if self.position == 0:
            self.x += self.velocidade
            if self.x < 0:
                self.velocidade = -1 * self.velocidade
            elif self.x > largura - self.largura:
                self.velocidade = -1 * self.velocidade
            if self.timer <= 0:
                self.EnemieAmmoClip.append(
                    Disparo(self.x + self.largura/2, self.y + self.altura/2, 2, self.team))
                self.timer = 60

        elif self.position == 1:
            self.y += self.velocidade
            if self.y < 0:
                self.velocidade = -1 * self.velocidade
            elif self.y > altura - self.altura:
                self.velocidade = -1 * self.velocidade
            if self.timer <= 0:
                self.EnemieAmmoClip.append(
                    Disparo(self.x + self.largura/2, self.y + self.altura/2, 3, self.team))
                self.timer = 60

        elif self.position == 2:
            self.y -= self.velocidade
            if self.y < 0:
                self.velocidade = -1 * self.velocidade
            elif self.y > altura - self.altura:
                self.velocidade = -1 * self.velocidade
            if self.timer <= 0:
                self.EnemieAmmoClip.append(
                    Disparo(self.x + self.largura/2, self.y + self.altura/2, 1, self.team))
                self.timer = 60

        elif self.position == 3:
            self.x -= self.velocidade
            if self.x < 0:
                self.velocidade = -1 * self.velocidade
            elif self.x > largura - self.largura:
                self.velocidade = -1 * self.velocidade
            if self.timer <= 0:
                self.EnemieAmmoClip.append(
                    Disparo(self.x + self.largura/2, self.y + self.altura/2, 0, self.team))
                self.timer = 60

        if self.rect.colliderect(Astronauta.rect):
            Sounds[3].play()
            self.health -= 10
            Astronauta.health -= 10
            if self.health <= 0:
                Enemies.pop(Enemies.index(self))

        canvas.blit(EnemieImage2, (self.x, self.y))


class MiniBoss(Model):
    def __init__(self):
        super().__init__(10, 10)
        self.health = 70
        self.team = "ENEMIE"
        self.rect = self.get_rect()
        self.spawn = True
        self.BossAmmoClip = []
        self.image = BossImageTransp
    
    #  HitBox Otimizada
    def get_rect(self):
        return [pygame.Rect(self.x + 12, self.y, self.largura - 24, self.altura),
                pygame.Rect(self.x , self.y + 12, self.largura, self.altura - 24)]

    def ProperXY(self):
        self.x = random.randrange(0, largura - 64)
        self.y = random.randrange(0, altura - 64)
        while self.x > Astronauta.x - 128 and self.x < Astronauta.x + Astronauta.largura + 64 and self.y > Astronauta.y - 128 and self.y < Astronauta.y + Astronauta.altura + 64:
            self.x = random.randrange(0, largura - 64)
            self.y = random.randrange(0, altura - 64)

    def DrawModel(self):
        self.rect = self.get_rect()
        
        if self.spawn:
            self.ProperXY()

        if self.rect[0].colliderect(Astronauta.rect) or self.rect[1].colliderect(Astronauta.rect):
            Sounds[3].play()
            Astronauta.health -= 1
            if self.health <= 0:
                Enemies.pop(Enemies.index(self))
        
        canvas.blit(self.image, (self.x, self.y))


class Boss(Model):
    def __init__(self):
        super().__init__(10, 10)
        self.altura = 96
        self.largura = 96
        self.health = 300
        self.right = True
        self.down = False
        self.left = False
        self.up = False
        self.team = "ENEMIE"
        self.CabageAmmoClip = []
        self.rect = self.get_rect()
        self.puto = False
        self.timer = 30
        self.hitcont = 0
        self.image = SuperBoss

    def get_rect(self):
        return [pygame.Rect(self.x, self.y, self.largura, self.altura - 16),
                pygame.Rect(self.x + 16 , self.y + 80, self.largura - 32, self.altura - 80)]

    def DrawModel(self):
        self.rect = self.get_rect()
        self.timer -= 2
        if self.right == True and not self.puto:
            if self.timer <= 0:
                self.CabageAmmoClip.append(Disparo(self.x + 48, self.y + 48, 2, self.team))
                self.timer = 30
            self.x += 5
            if self.x + self.largura >= largura:
                self.right = False
                self.down = True
        elif self.down == True and not self.puto:
            if self.timer <= 0:
                self.CabageAmmoClip.append(Disparo(self.x + 48, self.y + 48, 3, self.team))
                self.timer = 30
            self.y += 5
            if self.y + self.altura >= altura:
                self.down = False
                self.left = True
        elif self.left == True and not self.puto:
            if self.timer <= 0:
                self.CabageAmmoClip.append(Disparo(self.x + 48, self.y + 48, 0, self.team))
                self.timer = 30
            self.x -= 5
            if self.x <= 0:
                self.left = False
                self.up = True
        elif self.up == True and not self.puto:
            if self.timer <= 0:
                self.CabageAmmoClip.append(Disparo(self.x + 48, self.y + 48, 1, self.team))
                self.timer = 30
            self.y -= 5
            if self.y <= 0:
                self.up = False
                self.right = True

        if random.randint(0,100) == 59 and self.image == SuperBoss:
            self.image = SuperBossBolado
            self.puto = True
            self.right = False
            self.up = False
            self.left = False
            self.down = False

        if self.puto:
            if self.x < Astronauta.x:
                self.x += 5
            elif self.x > Astronauta.x:
                self.x -= 5
            if self.y < Astronauta.y:
                self.y += 5
            elif self.y > Astronauta.y:
                self.y -= 5

        if self.rect[0].colliderect(Astronauta.rect) or self.rect[1].colliderect(Astronauta.rect):
            Astronauta.health -= 1


        canvas.blit(self.image, (self.x, self.y))


class Disparo():
    def __init__(self, x, y, direction, team):
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = self.get_rect()
        self.team = team
        self.image = Tiro
    # HitBox Otimizada
    def get_rect(self):
        if self.direction == 1 or self.direction == 3:
            return pygame.Rect(int(self.x), int(self.y), 5, 5)
        else:
            return pygame.Rect(int(self.x), int(self.y), 5, 5)

    def Collided(self):
        global Score
        global ContKillEnemie1
        if self.team == "ALLY" and not EasterEgg:
            for enemie in Enemies:
                if enemie.__class__ == Enemie1 or enemie.__class__ == MiniBoss and not enemie.image == BossImageTransp:
                    if self.rect.colliderect(enemie.rect[0]) or self.rect.colliderect(enemie.rect[1]):
                        Score += 1*Speed
                        if enemie.__class__ == MiniBoss and not enemie.image == BossImageTransp or enemie.__class__ == Enemie1:
                            enemie.health -= 10
                            canvas.blit(HitMark, (self.x - 32, self.y - 32))
                            pygame.display.update()
                        ContKillEnemie1 += 1
                        if enemie.health <= 0:
                            Enemies.pop(Enemies.index(enemie))
                        if self in Astronauta.AmmoClip:
                            Astronauta.AmmoClip.pop(
                                Astronauta.AmmoClip.index(self))
                        
                elif enemie.__class__ == Enemie2:
                    if self.rect.colliderect(enemie.rect):
                        Score += 2*Speed
                        canvas.blit(HitMark, (self.x - 32, self.y - 32))
                        pygame.display.update()
                        enemie.health -= 10
                        if self in Astronauta.AmmoClip:
                            Astronauta.AmmoClip.pop(
                                Astronauta.AmmoClip.index(self))
                    if enemie.health <= 0:
                        Enemies.pop(Enemies.index(enemie))
                
                elif enemie.__class__ == Boss:
                    if self.rect.colliderect(enemie.rect[0]) or self.rect.colliderect(enemie.rect[1]) and enemie.puto:
                        Score += 1*Speed
                        enemie.hitcont += 1
                        if enemie.hitcont == 3:
                            enemie.puto = False
                            enemie.image = SuperBoss
                            enemie.up = True
                            enemie.hitcont = 0
                            enemie.CabageAmmoClip.append(Disparo(enemie.x + 48, enemie.y + 48, 0, enemie.team))
                            enemie.CabageAmmoClip.append(Disparo(enemie.x + 48, enemie.y + 48, 1, enemie.team))
                            enemie.CabageAmmoClip.append(Disparo(enemie.x + 48, enemie.y + 48, 2, enemie.team))
                            enemie.CabageAmmoClip.append(Disparo(enemie.x + 48, enemie.y + 48, 3, enemie.team))

                        enemie.health -= 10
                        canvas.blit(HitMark, (self.x - 32, self.y - 32))
                        pygame.display.update()
                        if enemie.health <= 0:
                                Enemies.pop(Enemies.index(enemie))
                        if self in Astronauta.AmmoClip:
                            Astronauta.AmmoClip.pop(Astronauta.AmmoClip.index(self))
                    if self.rect.colliderect(enemie.rect[0]) or self.rect.colliderect(enemie.rect[1]) and not enemie.puto:
                        enemie.health -= 2

        if self.team == "ENEMIE":
            if self.rect.colliderect(Astronauta.rect):
                Sounds[2].play()
                Astronauta.health -= 10
                for enemie in Enemies:
                    if enemie.__class__ == Enemie2:
                        if self in enemie.EnemieAmmoClip:
                            enemie.EnemieAmmoClip.pop(
                                enemie.EnemieAmmoClip.index(self))
                    if enemie.__class__ == Boss:
                        if self in enemie.CabageAmmoClip:
                            enemie.CabageAmmoClip.pop(
                                enemie.CabageAmmoClip.index(self))

    def DrawDisparo(self):
        self.rect = self.get_rect()
        # U, R, D, L, /, \, /, \
        if self.direction == 0:
            self.y -= 20
            self.image = DirecaoDisparo[1]
        elif self.direction == 1:
            self.x += 20
            self.image = DirecaoDisparo[0]
        elif self.direction == 2:
            self.y += 20
            self.image = DirecaoDisparo[1]
        elif self.direction == 3:
            self.x -= 20
            self.image = DirecaoDisparo[0]
        elif self.direction == 4:
            self.x += 20
            self.y -= 20
            self.image = DirecaoDisparo[2]
        elif self.direction == 5:
            self.x += 20
            self.y += 20
            self.image = DirecaoDisparo[3]
        elif self.direction == 6:
            self.x -= 20
            self.y += 20
            self.image = DirecaoDisparo[2]
        elif self.direction == 7:
            self.x -= 20
            self.y -= 20
            self.image = DirecaoDisparo[3]
        elif self.direction == 8:
            self.x -= 10
            self.y -= 20
            self.image = DirecaoDisparo[10]
        elif self.direction == 9:
            self.x -= 20
            self.y -= 10
            self.image = DirecaoDisparo[11]
        elif self.direction == 10:
            self.x += 10
            self.y += 20
            self.image = DirecaoDisparo[6]
        elif self.direction == 11:
            self.x += 20
            self.y += 10
            self.image = DirecaoDisparo[7]
        elif self.direction == 12:
            self.x -= 10
            self.y += 20
            self.image = DirecaoDisparo[9]
        elif self.direction == 13:
            self.x -= 20
            self.y += 10
            self.image = DirecaoDisparo[8]
        elif self.direction == 14:
            self.x += 10
            self.y -= 20
            self.image = DirecaoDisparo[5]
        elif self.direction == 15:
            self.x += 20
            self.y -= 10      
            self.image = DirecaoDisparo[4]
            
        
        self.Collided()
        if self.x < -20 or self.x > largura + 20 or self.y < -20 or self.y > altura + 20:
            if self.team == "ALLY":
                if self in Astronauta.AmmoClip:
                    Astronauta.AmmoClip.pop(Astronauta.AmmoClip.index(self))

        else:
            canvas.blit(self.image, (int(self.x), int(self.y)))


class LifeBox(Model):
    def __init__(self):
        super().__init__(random.randrange(0, largura-32), random.randrange(0, altura-32))
        self.largura = 32
        self.altura = 32

    def DrawItem(self):
        self.rect = self.get_rect()
        if self.rect.colliderect(Astronauta.rect):
            Sounds[1].play()
            Astronauta.health += 33
            if Astronauta.health > 100:
                Astronauta.health = 100
            Gadgets.pop(Gadgets.index(self))
        canvas.blit(lifeBox, (self.x, self.y))


class Testosterona(Model):
    def __init__(self):
        super().__init__(random.randrange(0, largura-16), random.randrange(0, altura-32))
        self.largura = 16
        self.altura = 32

    def DrawItem(self):
        self.rect = self.get_rect()
        if self.rect.colliderect(Astronauta.rect):
            Astronauta.TestosteronaCont += 1
            Gadgets.pop(Gadgets.index(self))
        canvas.blit(TestosteronaImg, (self.x, self.y))

#endregion

# Functions
#region

def DrawInstruction():
    if commands:
        canvas.blit(instruction, (600,10))
    else:
        canvas.blit(press_i, (600,10))

def drawmenu():
    global BestScore
    canvas.blit(Menu, (0, 0))
    DrawInstruction()
    
    canvas.blit(font2.render("Best Score: " + str(BestScore).rjust(4,'0'), 1, (255, 255, 255)),
                (220, 520))
    pygame.display.update()

def drawesc():
    canvas.blit(pause_back, (0,0))
    DrawInstruction()
    pygame.display.update()

def draw():
    canvas.blit(BackGround, (0, 0))
    DrawInstruction()
    canvas.blit(font.render(str(Score).rjust(4,'0'), 1, (255, 255, 255)),
                (int(largura/2)-57, 0))
    Astronauta.DrawLife()
    Astronauta.DrawAmmo()
    Astronauta.DrawTestosterona()
    canvas.blit(ScoreSquare, (int(largura/2) - 70 , 20))

    if EasterEgg:
        canvas.blit(Barney, (0, 0))
        Astronauta.DrawModel()

        for Ammo in Astronauta.AmmoClip:
            Ammo.DrawDisparo()

    if Astronauta.health > 0 and EasterEgg == False:
        Astronauta.DrawModel()

        for Ammo in Astronauta.AmmoClip:
            Ammo.DrawDisparo()
        for Enemie in Enemies:
            if Enemie.__class__ == Enemie2:
                for Bala in Enemie.EnemieAmmoClip:
                    Bala.DrawDisparo()
            elif Enemie.__class__ == MiniBoss:
                for Bala in Enemie.BossAmmoClip:
                    Bala.DrawDisparo()
            elif Enemie.__class__ == Boss:
                for Bala in Enemie.CabageAmmoClip:
                    Bala.DrawDisparo()
            Enemie.DrawModel()

        for gadgets in Gadgets:
            gadgets.DrawItem()

    

    pygame.display.update()
#endregion

# Setup
#region
Astronauta = Player(370, 270)
Gadgets = []
Enemies = []

Dificuldade = 1
ContKillEnemie1 = 0
Score = 0
Speed = 1
Reload = -1
Spawn = True
bosscont = 0
commands = False
flag = True

# menus
start = False
pause = False
menu = True
EasterEgg = False

#endregion

# pygame.draw.rect(canvas,(255,255,255), self.rect)

while True:
    clock.tick(60)
    if Astronauta.x <= -20 and Astronauta.y >= 540 and Score < 15:
        EasterEgg = True
    if Astronauta.x >= 750 and Astronauta.y <= -5:
        EasterEgg = False

    if pygame.event.get(24) and start:
        if not (any(box.__class__ == LifeBox for box in Gadgets)):
            Gadgets.append(LifeBox())
    if pygame.event.get(25) and start:
        Gadgets.append(Testosterona())
    if pygame.event.get(26) and start:
        Dificuldade += 1
    if pygame.event.get(28) and start:
        Enemies.append(Enemie2())
    if pygame.event.get(27) and start:
        for x in Enemies:
            if x.__class__ == MiniBoss:
                x.image = BossImageTransp
                x.spawn = True
    if pygame.event.get(29) and start:
        for x in Enemies:
            if x.__class__ == MiniBoss:
                x.image = BossImage
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 0, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 1, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 2, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 3, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 4, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 5, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 6, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 7, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 8, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 9, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 10, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 11, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 12, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 13, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 14, x.team))
                x.BossAmmoClip.append(
                    Disparo(x.x + x.largura/2, x.y + x.altura/2, 15, x.team))
                x.spawn = False
    if pygame.event.get(30) and start:
        Enemies.append(MiniBoss())
    if pygame.event.get(31) and flag:
        menu = True
        pause = False
        start = False
        flag = False


    if ContKillEnemie1 > 100 and Speed == 1 and not (any(enemie.__class__ == Enemie1 for enemie in Enemies)):
        Enemies.append(MiniBoss())
        Spawn = False
        Dificuldade = 1
        Speed += 1
    elif ContKillEnemie1 > 200 and Speed == 2 and not (any(enemie.__class__ == Enemie1 for enemie in Enemies)):
        Enemies.append(MiniBoss())
        Dificuldade = 1
        Speed += 1
    elif ContKillEnemie1 > 300 and Speed == 3 and not (any(enemie.__class__ == Enemie1 for enemie in Enemies)):
        Enemies.append(MiniBoss())
        Dificuldade = 1
        Speed += 1 
    elif ContKillEnemie1 > 400 and Speed == 4 and not (any(enemie.__class__ == Enemie1 for enemie in Enemies)):
        Enemies.append(MiniBoss())
        Dificuldade = 1
        Speed += 1 
    
    if Enemies == []:
        Spawn = True

    if Score % 500 < 20 and Score > 499:
        if not (any(enemie.__class__ == Boss for enemie in Enemies)):
            for x in range (0,bosscont+1):
                Enemies.append(Boss())
                bosscont += 1

    if not (any(enemie.__class__ == Enemie1 for enemie in Enemies)) and Spawn and not (any(enemie.__class__ == Boss for enemie in Enemies)):
        i = 0
        while i <= Dificuldade:
            Enemies.append(Enemie1())
            i += 1

    if Reload > 0:
        Reload -= 1
    elif Reload == 0:
        Reload= -1
        Astronauta.Ammo = 7
    # Comandos
    # region
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arquivo = open("./Data/Score/BestScore.txt",'w')
            arquivo.write(hashlib.md5(str(BestScore).encode("utf-8")).hexdigest())
            arquivo.close()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if VolumeUp.collidepoint(pos) and MusicVolume >= -0.1 and MusicVolume < 1 and menu:
                MusicVolume += 0.05
                pygame.mixer.music.set_volume(MusicVolume)           
            if VolumeDown.collidepoint(pos) and MusicVolume > 0 and MusicVolume <= 1.1 and menu:
                MusicVolume -= 0.05
                pygame.mixer.music.set_volume(MusicVolume)
            
            if EffectsUp.collidepoint(pos) and EffectsVolume >= -0.1 and EffectsVolume < 1 and menu:
                EffectsVolume += 0.05
                for x in range(0,7):
                    Sounds[x].set_volume(EffectsVolume)
            if EffectsDown.collidepoint(pos) and EffectsVolume > 0 and EffectsVolume <= 1.1 and menu:
                EffectsVolume -= 0.05
                for x in range(0,7):
                    Sounds[x].set_volume(EffectsVolume)

            if StartBottom.collidepoint(pos) and menu:
                
                pygame.time.set_timer(24, 12000)
                pygame.time.set_timer(25, 8000)
                pygame.time.set_timer(26, 10000)
                pygame.time.set_timer(27, 2000)
                pygame.time.set_timer(29, 6000)
                pygame.time.set_timer(28, 20000)
                pygame.time.set_timer(30, 50000)
                menu = False
                pause = False
                start = True
                Gadgets = []
                Enemies = []
                TestosteronaCont = 0
                Dificuldade = 1
                Score = 0
                Speed = 1
                ContKillEnemie1 = 0
                Reload = -1
                Astronauta.health = 100
                Astronauta.Ammo = 7
                Spawn = True
                bosscont = 0

            if ExitBottom.collidepoint(pos) and menu:
                arquivo = open("./Data/Score/BestScore.txt",'w')
                arquivo.write(hashlib.md5(str(BestScore).encode("utf-8")).hexdigest())
                arquivo.close()
                pygame.quit()
                sys.exit()

            #PAUSE

            if VolumeUpPause.collidepoint(pos) and MusicVolume >= -0.1 and MusicVolume < 1 and pause:
                MusicVolume += 0.05
                pygame.mixer.music.set_volume(MusicVolume)           
            if VolumeDownPause.collidepoint(pos) and MusicVolume > 0 and MusicVolume <= 1.1 and pause:
                MusicVolume -= 0.05
                pygame.mixer.music.set_volume(MusicVolume)
            
            if EffectsUpPause.collidepoint(pos) and EffectsVolume >= -0.1 and EffectsVolume < 1 and pause:
                EffectsVolume += 0.05
                for x in range(0,7):
                    Sounds[x].set_volume(EffectsVolume)
            if EffectsDownPause.collidepoint(pos) and EffectsVolume > 0 and EffectsVolume <= 1.1 and pause:
                EffectsVolume -= 0.05
                for x in range(0,7):
                    Sounds[x].set_volume(EffectsVolume)

            if ContBottom.collidepoint(pos) and pause:
                start = True
                pause = False
                menu = False
            if MenuPauseBottom.collidepoint(pos) and pause:
                start = False
                pause = False
                menu = True
            if ExitPauseBottom.collidepoint(pos) and pause:
                pygame.quit()

        if event.type == pygame.KEYDOWN and start:
            if event.key == pygame.K_UP and Reload == -1:
                if Astronauta.Ammo > 0:
                    Sounds[0].play()
                    Astronauta.Ammo -= 1
                    Astronauta.AmmoClip.append(
                        Disparo(Astronauta.x + 32, Astronauta.y + 32, 0, Astronauta.team))
            elif event.key == pygame.K_DOWN and Reload == -1:
                if Astronauta.Ammo > 0:
                    Sounds[0].play()
                    Astronauta.Ammo -= 1
                    Astronauta.AmmoClip.append(
                        Disparo(Astronauta.x + 32, Astronauta.y + 32, 2, Astronauta.team))
            elif event.key == pygame.K_LEFT and Reload == -1:
                if Astronauta.Ammo > 0:
                    Sounds[0].play()
                    Astronauta.Ammo -= 1
                    Astronauta.lado = -1
                    Astronauta.AmmoClip.append(
                        Disparo(Astronauta.x + 32, Astronauta.y + 32, 3, Astronauta.team))
            elif event.key == pygame.K_RIGHT and Reload == -1:
                if Astronauta.Ammo > 0:
                    Sounds[0].play()
                    Astronauta.Ammo -= 1
                    Astronauta.lado = 1
                    Astronauta.AmmoClip.append(
                        Disparo(Astronauta.x + 32, Astronauta.y + 32, 1, Astronauta.team))
            elif event.key == pygame.K_r:
                Sounds[4].play()
                Reload = 30
            elif event.key == pygame.K_ESCAPE and start:
                start = False
                menu = False
                pause = True
            elif event.key == pygame.K_SPACE:
                if Astronauta.TestosteronaCont >= 4:
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 0, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 1, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 2, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 3, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 4, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 5, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 6, Astronauta.team))
                    Astronauta.AmmoClip.append(Disparo(Astronauta.x + 32, Astronauta.y + 32, 7, Astronauta.team))
                    Astronauta.TestosteronaCont -= 4
                    Sounds[5].play()
                    if Astronauta.TestosteronaCont < 0:
                        Astronauta.TestosteronaCont = 0
        

    if pygame.key.get_pressed()[pygame.K_a]:
        Astronauta.left = True
        Astronauta.right = False
        Astronauta.up = False
        Astronauta.down = False
    elif pygame.key.get_pressed()[pygame.K_d]:
        Astronauta.left = False
        Astronauta.right = True
        Astronauta.up = False
        Astronauta.down = False
    elif pygame.key.get_pressed()[pygame.K_w]:
        Astronauta.left = False
        Astronauta.right = False
        Astronauta.up = True
        Astronauta.down = False
    elif pygame.key.get_pressed()[pygame.K_s]:
        Astronauta.left = False
        Astronauta.right = False
        Astronauta.up = False
        Astronauta.down = True
    if pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
        Astronauta.left = True
        Astronauta.right = False
        Astronauta.up = False
        Astronauta.down = True
    elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_d]:
        Astronauta.left = False
        Astronauta.right = True
        Astronauta.up = False
        Astronauta.down = True
    elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
        Astronauta.left = True
        Astronauta.right = False
        Astronauta.up = True
        Astronauta.down = False
    elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
        Astronauta.left = False
        Astronauta.right = True
        Astronauta.up = True
        Astronauta.down = False
    if pygame.key.get_pressed()[pygame.K_i]:
        commands = True
    else :
        commands = False


    # endregion
    if Astronauta.health <= 0 and Astronauta.health > -20:
        if Score > BestScore:
            BestScore = Score
        Sounds[6].set_volume(1)
        Sounds[6].play()
        flag = True
        pygame.time.set_timer(31, 5000)
        Astronauta.health = -25


    if menu:
        drawmenu()
    elif pause:
        drawesc()
    elif start:
        draw()
