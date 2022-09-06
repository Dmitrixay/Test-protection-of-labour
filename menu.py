import pygame
import sys
import pyganim
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
window = pygame.display.set_mode((1000, 1000)) #Размер экрана
pygame.display.set_caption('Тест по профориентации') #Название окна
screen = pygame.Surface((1000, 1000)) #Размер рабочей области
clock = pygame.time.Clock()
pygame.font.init()

#Заливка кнопок меню
button1 = pygame.image.load("Clipart/menu/test.png") 
button2 = pygame.image.load("Clipart/menu/test1.png")
quit1 = pygame.image.load("Clipart/menu/tren.png")
quit2 = pygame.image.load("Clipart/menu/tren1.png")
vihod1 = pygame.image.load("Clipart/menu/obu.png")
vihod2 = pygame.image.load("Clipart/menu/obu1.png")
#Заливка кнопок меню авторизации
vhod1 = pygame.image.load("Clipart/dannie/vhod.png")
vhod2 = pygame.image.load("Clipart/dannie/vhod1.png")
vvod2 = pygame.image.load("Clipart/dannie/vvod1.png")
vvod1 = pygame.image.load("Clipart/dannie/vvod2.png")
#кнопки завершения теста
menuend1 = pygame.image.load("Clipart/end/test/menu.png")
menuend2 = pygame.image.load("Clipart/end/test/menu1.png")
vih1 = pygame.image.load("Clipart/end/test/viyti.png")
vih2 = pygame.image.load("Clipart/end/test/viyti1.png")
#Кнопки в игре
left1 = pygame.image.load("Clipart/vopros1/left.png")
left2 = pygame.image.load("Clipart/vopros1/left1.png")
rigth1 = pygame.image.load("Clipart/vopros1/rigth.png")
rigth2 = pygame.image.load("Clipart/vopros1/rigth1.png")
otvet1 = pygame.image.load("Clipart/vopros1/otvet1.png")
otvet11 = pygame.image.load("Clipart/vopros1/otvet11.png")
otvet2 = pygame.image.load("Clipart/vopros1/otvet2.png")
otvet21 = pygame.image.load("Clipart/vopros1/otvet21.png")
otvet3 = pygame.image.load("Clipart/vopros1/otvet3.png")
otvet31 = pygame.image.load("Clipart/vopros1/otvet31.png")
otvet4 = pygame.image.load("Clipart/vopros1/otvet4.png")
otvet41 = pygame.image.load("Clipart/vopros1/otvet41.png")
dalee = pygame.image.load("Clipart/vopros1/dalee.png")
dalee1 = pygame.image.load("Clipart/vopros1/dalee1.png")
netotveta = pygame.image.load("Clipart/vopros1/netotveta.png")
netotveta1 = pygame.image.load("Clipart/vopros1/netotveta1.png")

#Фон 
bb = pygame.image.load("Clipart/dannie/obvid1.png") #Авторизация
fonmenu = pygame.image.load('Clipart/menu/obvid.png') #Меню
bb2 = pygame.image.load("Clipart/end/test/obvidend1.png") #Завершение теста
test1 = pygame.image.load("Clipart/vopros1/test1.png")
test2 = pygame.image.load("Clipart/vopros1/test2.png")

#Анимация вопрос 1
#Ходит вперед
boltAnim = pyganim.PygAnimation([('Clipart/vopros1/hoditback2.png', 100),
                                 ('Clipart/vopros1/hoditback3.png', 100),
                                 ('Clipart/vopros1/hoditback4.png', 100),
                                 ('Clipart/vopros1/hoditback5.png', 100),
                                 ('Clipart/vopros1/hoditback6.png', 100),
                                 ('Clipart/vopros1/hoditback7.png', 100),
                                 ('Clipart/vopros1/hoditback8.png', 100)])

#Ходит назад
hoditv1 = pyganim.PygAnimation([('Clipart/vopros1/hodit2.png', 100),
                                ('Clipart/vopros1/hodit3.png', 100),
                                ('Clipart/vopros1/hodit4.png', 100),
                                ('Clipart/vopros1/hodit5.png', 100),
                                ('Clipart/vopros1/hodit6.png', 100),
                                ('Clipart/vopros1/hodit7.png', 100),
                                ('Clipart/vopros1/hodit8.png', 100)])

stayhero = pyganim.PygAnimation([('Clipart/vopros1/hoditback1.png', 10)])
stayherov1dalee = pyganim.PygAnimation([('Clipart/vopros1/hoditback1.png', 10)])
stayhero2 = pyganim.PygAnimation([('Clipart/vopros1/hoditback1.png', 10)])
boltAnim1 = pyganim.PygAnimation([('Clipart/vopros1/walk5.png', 10)])

boltAnim2 = pyganim.PygAnimation([('Clipart/vopros1/walk6.png', 10)])

boltAnim3 = pyganim.PygAnimation([('Clipart/vopros1/hoditback1.png', 10)])
#Верные ответы, вопрос 1,2
verno1 = pyganim.PygAnimation([('Clipart/vopros1/verno1.png', 10)])
verno2 = pyganim.PygAnimation([('Clipart/vopros1/verno2.png', 10)])
#Неверные ответы, вопрос 1,2
neverno11 = pyganim.PygAnimation([('Clipart/vopros1/neverno11.png', 10)])
neverno12 = pyganim.PygAnimation([('Clipart/vopros1/neverno12.png', 10)])
neverno21 = pyganim.PygAnimation([('Clipart/vopros1/neverno21.png', 10)])
netotveta2 = pyganim.PygAnimation([('Clipart/vopros1/netotveta2.png', 10)])

#Обучение
odin = pygame.image.load("Clipart/obuchenie/odin.png")
dva = pygame.image.load("Clipart/obuchenie/dva.png")
tri = pygame.image.load("Clipart/obuchenie/tri.png")
chetire = pygame.image.load("Clipart/obuchenie/chetire.png")
pyat = pygame.image.load("Clipart/obuchenie/pyat.png")
shest = pygame.image.load("Clipart/obuchenie/shest.png")
sem = pygame.image.load("Clipart/obuchenie/sem.png")
odin1 = pygame.image.load("Clipart/obuchenie/odin1.png")
dva1 = pygame.image.load("Clipart/obuchenie/dva1.png")
tri1 = pygame.image.load("Clipart/obuchenie/tri1.png")
chetire1 = pygame.image.load("Clipart/obuchenie/chetire1.png")
pyat1 = pygame.image.load("Clipart/obuchenie/pyat1.png")
shest1 = pygame.image.load("Clipart/obuchenie/shest1.png")
sem1 = pygame.image.load("Clipart/obuchenie/sem1.png")
menuob = pygame.image.load("Clipart/obuchenie/menu.png")
menuob1 = pygame.image.load("Clipart/obuchenie/menu1.png")
oneob = pygame.image.load("Clipart/obuchenie/one.png")
oneob1 = pyganim.PygAnimation([('Clipart/obuchenie/one.png', 10)])
twoob = pyganim.PygAnimation([('Clipart/obuchenie/two.png', 10)])
threeob = pyganim.PygAnimation([('Clipart/obuchenie/three.png', 10)])
fourob = pyganim.PygAnimation([('Clipart/obuchenie/four.png', 10)])
fiveob = pyganim.PygAnimation([('Clipart/obuchenie/five.png', 10)])
sixob = pyganim.PygAnimation([('Clipart/obuchenie/six.png', 10)])
sevenob = pyganim.PygAnimation([('Clipart/obuchenie/seven.png', 10)])
#Экран 3
fonv3 = pygame.image.load("Clipart/vopros3/fon.png")
dalee3 = pygame.image.load("Clipart/vopros3/dalee.png")
dalee31 = pygame.image.load("Clipart/vopros3/dalee1.png")
otvetv31 = pygame.image.load("Clipart/vopros3/otvet1.png")
otvetv32 = pygame.image.load("Clipart/vopros3/otvet2.png")
otvetv33 = pygame.image.load("Clipart/vopros3/otvet3.png")
otvetv311 = pygame.image.load("Clipart/vopros3/otvet11.png")
otvetv321 = pygame.image.load("Clipart/vopros3/otvet21.png")
otvetv331 = pygame.image.load("Clipart/vopros3/otvet31.png")

nevernov31 = pyganim.PygAnimation([('Clipart/vopros3/neverno1.png', 10)])
vernov32 = pyganim.PygAnimation([('Clipart/vopros3/verno2.png', 10)])
nevernov33 = pyganim.PygAnimation([('Clipart/vopros3/neverno3.png', 10)])
stayherov3 = pyganim.PygAnimation([('Clipart/vopros3/hero.png', 10)])
stayherov3dalee = pyganim.PygAnimation([('Clipart/vopros3/hero.png', 10)])

                          
odeyalo = pyganim.PygAnimation([('Clipart/vopros3/odeyalo.png', 10)])  
stayherov31 = pyganim.PygAnimation([('Clipart/vopros3/hero1.png', 10)])                               
#Экран 4
fonv4 = pygame.image.load("Clipart/vopros4/fon.png")
dalee4 = pygame.image.load("Clipart/vopros4/dalee.png")
dalee41 = pygame.image.load("Clipart/vopros4/dalee1.png")
otvetv41 = pygame.image.load("Clipart/vopros4/otvet1.png")
otvetv42 = pygame.image.load("Clipart/vopros4/otvet2.png")
otvetv43 = pygame.image.load("Clipart/vopros4/otvet3.png")
otvetv411 = pygame.image.load("Clipart/vopros4/otvet11.png")
otvetv421 = pygame.image.load("Clipart/vopros4/otvet21.png")
otvetv431 = pygame.image.load("Clipart/vopros4/otvet31.png")

nevernov41 = pyganim.PygAnimation([('Clipart/vopros4/neverno1.png', 10)])
nevernov42 = pyganim.PygAnimation([('Clipart/vopros4/neverno2.png', 10)])
nevernov43 = pyganim.PygAnimation([('Clipart/vopros4/verno.png', 10)])
stayherov4 = pyganim.PygAnimation([('Clipart/vopros4/hero.png', 10)])
stayherov41 = pyganim.PygAnimation([('Clipart/vopros4/hero1.png', 10)])


#Анимация экран 3
gorelkav3 = pyganim.PygAnimation([('Clipart/vopros3/gorelka.png', 3900),
                                  ('Clipart/vopros3/gorelka1.png', 1000000)])
ogonanim1 = pyganim.PygAnimation([('Clipart/vopros3/ogonanim1.png', 100),
                                  ('Clipart/vopros3/ogonanim2.png', 100),
                                  ('Clipart/vopros3/ogonanim3.png', 100),
                                  ('Clipart/vopros3/ogonanim4.png', 100),
                                  ('Clipart/vopros3/ogonanim5.png', 100),
                                  ('Clipart/vopros3/ogonanim6.png', 100)])
trezhinaanim = pyganim.PygAnimation([('Clipart/vopros3/trezhinaanim1.png', 300),
                                     ('Clipart/vopros3/trezhinaanim2.png', 300),
                                     ('Clipart/vopros3/trezhinaanim3.png', 300),
                                     ('Clipart/vopros3/trezhinaanim4.png', 300),
                                     ('Clipart/vopros3/trezhinaanim5.png', 300),
                                     ('Clipart/vopros3/trezhinaanim6.png', 300),
                                     ('Clipart/vopros3/trezhinaanim7.png', 300),
                                     ('Clipart/vopros3/trezhinaanim8.png', 300),
                                     ('Clipart/vopros3/trezhinaanim9.png', 150),
                                     ('Clipart/vopros3/trezhinaanim10.png', 150),
                                     ('Clipart/vopros3/trezhinaanim11.png', 150),
                                     ('Clipart/vopros3/trezhinaanim12.png', 150),
                                     ('Clipart/vopros3/trezhinaanim13.png', 150),
                                     ('Clipart/vopros3/trezhinaanim14.png', 150),
                                     ('Clipart/vopros3/trezhinaanim15.png', 150),
                                     ('Clipart/vopros3/trezhinaanim16.png', 150),
                                     ('Clipart/vopros3/trezhinaanim17.png', 150),
                                     ('Clipart/vopros3/trezhinaanim18.png', 150),
                                     ('Clipart/vopros3/trezhinaanim19.png', 100000)])
razliv = pyganim.PygAnimation([('Clipart/vopros3/leda9.png', 3900),
                               ('Clipart/vopros3/razliv.png', 10000000)])

led = pyganim.PygAnimation([('Clipart/vopros3/led.png', 10)])
led2 = pyganim.PygAnimation([('Clipart/vopros3/led.png', 10)])
leda = pyganim.PygAnimation([('Clipart/vopros3/leda1.png', 1000),
                             ('Clipart/vopros3/leda2.png', 1000),
                             ('Clipart/vopros3/leda3.png', 1000),
                             ('Clipart/vopros3/leda4.png', 1000),
                             ('Clipart/vopros3/leda5.png', 1000),
                             ('Clipart/vopros3/leda6.png', 1000),
                             ('Clipart/vopros3/leda7.png', 1000),
                             ('Clipart/vopros3/leda8.png', 1000),
                             ('Clipart/vopros3/leda9.png', 100000)])  

vodaanim88 = pyganim.PygAnimation([('Clipart/vopros3/vodaanim9.png', 100),
                                 ('Clipart/vopros3/vodaanim10.png', 100),
                                 ('Clipart/vopros3/vodaanim11.png', 100),
                                 ('Clipart/vopros3/vodaanim12.png', 100)])
odeyalo = pyganim.PygAnimation([('Clipart/vopros3/odeyalo.png', 10)])  
odeyaloanim = pyganim.PygAnimation([('Clipart/vopros3/odeyalo1.png', 1000),
                                    ('Clipart/vopros3/odeyalo2.png', 500),
                                    ('Clipart/vopros3/odeyalo3.png', 500),
                                    ('Clipart/vopros3/odeyalo4.png', 500),
                                    ('Clipart/vopros3/odeyalo5.png', 500),
                                    ('Clipart/vopros3/odeyalo6.png', 500),
                                    ('Clipart/vopros3/odeyalo7.png', 400),
                                    ('Clipart/vopros3/odeyalo8.png', 300),
                                    ('Clipart/vopros3/odeyalo9.png', 200),
                                    ('Clipart/vopros3/odeyalo10.png', 10000)])

#Анимация 4 экран
izkri = pyganim.PygAnimation([('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),
                              ('Clipart/vopros4/one3.png', 100),
                              ('Clipart/vopros4/one.png', 100),
                              ('Clipart/vopros4/one2.png', 100),         
                              ('Clipart/vopros4/leda9.png', 1000000000)])

vzriv = pyganim.PygAnimation([('Clipart/vopros4/leda9.png', 2000),
                             ('Clipart/vopros4/vzriv1.png', 50),
                             ('Clipart/vopros4/vzriv2.png', 50),
                             ('Clipart/vopros4/vzriv3.png', 50),
                             ('Clipart/vopros4/vzriv4.png', 50),
                             ('Clipart/vopros4/vzriv5.png', 50),
                             ('Clipart/vopros4/vzriv6.png', 50),
                             ('Clipart/vopros4/vzriv7.png', 50),
                             ('Clipart/vopros4/vzriv8.png', 50),
                             ('Clipart/vopros4/vzriv9.png', 50),
                             ('Clipart/vopros4/vzriv10.png', 50),
                             ('Clipart/vopros4/vzriv11.png', 50),
                             ('Clipart/vopros4/vzriv12.png', 50),
                             ('Clipart/vopros4/vzriv13.png', 50),
                             ('Clipart/vopros4/vzriv14.png', 50),
                             ('Clipart/vopros4/vzriv15.png', 50),
                             ('Clipart/vopros4/vzriv16.png', 50),
                             ('Clipart/vopros4/vzriv17.png', 50),
                             ('Clipart/vopros4/vzriv18.png', 50),
                             ('Clipart/vopros4/vzriv19.png', 50),
                             ('Clipart/vopros4/vzriv20.png', 50),
                             ('Clipart/vopros4/vzriv21.png', 50),
                             ('Clipart/vopros4/vzriv22.png', 50),
                             ('Clipart/vopros4/vzriv23.png', 50),
                             ('Clipart/vopros4/vzriv24.png', 50),
                             ('Clipart/vopros4/vzriv25.png', 50),
                             ('Clipart/vopros4/vzriv26.png', 50),
                             ('Clipart/vopros4/vzriv27.png', 50),
                             ('Clipart/vopros4/vzriv28.png', 50),
                             ('Clipart/vopros4/vzriv29.png', 50),
                             ('Clipart/vopros4/vzriv30.png', 50),
                             ('Clipart/vopros4/vzriv31.png', 50),
                             ('Clipart/vopros4/vzriv32.png', 50),
                             ('Clipart/vopros4/vzriv33.png', 50),
                             ('Clipart/vopros4/vzriv34.png', 50),
                             ('Clipart/vopros4/vzriv35.png', 50),
                             ('Clipart/vopros4/vzriv36.png', 50),
                             ('Clipart/vopros4/vzriv37.png', 50),
                             ('Clipart/vopros4/vzriv38.png', 50),
                             ('Clipart/vopros4/vzriv39.png', 50),
                             ('Clipart/vopros4/vzriv40.png', 50),
                             ('Clipart/vopros4/vzriv41.png', 50),
                             ('Clipart/vopros4/vzriv42.png', 50),
                             ('Clipart/vopros4/vzriv43.png', 50),
                             ('Clipart/vopros4/vzriv44.png', 50),
                             ('Clipart/vopros4/vzriv45.png', 50),
                             ('Clipart/vopros4/vzriv46.png', 50),
                             ('Clipart/vopros4/vzriv47.png', 50),
                             ('Clipart/vopros4/vzriv48.png', 100),
                             ('Clipart/vopros4/leda9.png', 100000)])


probil = pyganim.PygAnimation([('Clipart/vopros4/probil1.png', 100),
                              ('Clipart/vopros4/probil2.png', 100),
                              ('Clipart/vopros4/probil3.png', 100),
                              ('Clipart/vopros4/probil4.png', 100),
                              ('Clipart/vopros4/probil5.png', 100),
                              ('Clipart/vopros4/probil6.png', 100),
                              ('Clipart/vopros4/probil7.png', 100),
                              ('Clipart/vopros4/probil8.png', 100),
                              ('Clipart/vopros4/probil9.png', 100),
                              ('Clipart/vopros4/probil10.png', 100),
                              ('Clipart/vopros4/probil11.png', 100),
                              ('Clipart/vopros4/probil12.png', 100),
                              ('Clipart/vopros4/probil13.png', 100),
                              ('Clipart/vopros4/probil14.png', 100),
                              ('Clipart/vopros4/probil15.png', 100),
                              ('Clipart/vopros4/probil16.png', 100),
                              ('Clipart/vopros4/probil17.png', 100),
                              ('Clipart/vopros4/probil18.png', 100),
                              ('Clipart/vopros4/probil19.png', 100),
                              ('Clipart/vopros4/probil20.png', 100),
                              ('Clipart/vopros4/probil21.png', 100),
                              ('Clipart/vopros4/probil22.png', 100),
                              ('Clipart/vopros4/probil23.png', 100),
                              ('Clipart/vopros4/probil24.png', 100),                  
                              ('Clipart/vopros4/probil25.png', 100000000)])
 
neft = pyganim.PygAnimation([('Clipart/vopros4/leda9.png', 2500),
                             ('Clipart/vopros4/neft.png', 1000000)])

hodit = pyganim.PygAnimation([('Clipart/vopros4/hodit2.png', 100),
                              ('Clipart/vopros4/hodit3.png', 100),
                              ('Clipart/vopros4/hodit4.png', 100),
                              ('Clipart/vopros4/hodit5.png', 100),
                              ('Clipart/vopros4/hodit6.png', 100),
                              ('Clipart/vopros4/hodit7.png', 100),
                              ('Clipart/vopros4/hodit8.png', 100),
                              ('Clipart/vopros4/hodit9.png', 100)])


strelka1 = pyganim.PygAnimation([('Clipart/vopros4/ctrelka11.png', 50),
                                 ('Clipart/vopros4/ctrelka12.png', 50),
                                 ('Clipart/vopros4/ctrelka13.png', 50),
                                 ('Clipart/vopros4/ctrelka14.png', 50),
                                 ('Clipart/vopros4/ctrelka15.png', 150),
                                 ('Clipart/vopros4/ctrelka16.png', 150),
                                 ('Clipart/vopros4/ctrelka17.png', 150)])

strelka2 = pyganim.PygAnimation([('Clipart/vopros4/ctrelka21.png', 50),
                                 ('Clipart/vopros4/ctrelka22.png', 50),
                                 ('Clipart/vopros4/ctrelka23.png', 50),
                                 ('Clipart/vopros4/ctrelka24.png', 50),
                                 ('Clipart/vopros4/ctrelka25.png', 50),
                                 ('Clipart/vopros4/ctrelka26.png', 100),
                                 ('Clipart/vopros4/ctrelka27.png', 100),
                                 ('Clipart/vopros4/ctrelka28.png', 100),
                                 ('Clipart/vopros4/ctrelka29.png', 100)])

svarlav4 = pyganim.PygAnimation([('Clipart/vopros4/svarka.png', 3300),
                                 ('Clipart/vopros4/leda9.png', 1000000000)])

lezhitv4 = pyganim.PygAnimation([('Clipart/vopros4/leda9.png', 3300),
                                 ('Clipart/vopros4/lezhit.png', 1000000000)])
#Анимация вопрос 1
molni = pyganim.PygAnimation([('Clipart/vopros1/leda9.png', 600),
                              ('Clipart/vopros1/molni1.png', 100),
                              ('Clipart/vopros1/molni2.png', 100),
                              ('Clipart/vopros1/molni3.png', 100),
                              ('Clipart/vopros1/molni4.png', 100),
                              ('Clipart/vopros1/leda9.png', 100000000)])

molni2 = pyganim.PygAnimation([('Clipart/vopros1/leda9.png', 600),
                              ('Clipart/vopros1/molni1.png', 100),
                              ('Clipart/vopros1/molni2.png', 100),
                              ('Clipart/vopros1/molni3.png', 100),
                              ('Clipart/vopros1/molni4.png', 100),
                              ('Clipart/vopros1/leda9.png', 100000000)])

#Не пройден
fonneproy = pygame.image.load("Clipart/end/neproyden/fon.png") 
menuneproyden = pygame.image.load("Clipart/end/neproyden/menu.png")
menuneproyden1 = pygame.image.load("Clipart/end/neproyden/menu1.png")
vihodneproyden = pygame.image.load("Clipart/end/neproyden/vihod.png")
vihodneproyden1 = pygame.image.load("Clipart/end/neproyden/vihod1.png")
zanovoneproyden = pygame.image.load("Clipart/end/neproyden/zanovo.png")
zanovoneproyden1 = pygame.image.load("Clipart/end/neproyden/zanovo1.png")


enum = 2
def print_text (x=30, y=940, font_color = (0, 0, 0), font_type = 'font/f.ttf', font_size = 30):
    global enum
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render("Осталось попыток: "+str(enum), True, font_color)
    screen.blit(text, (x, y))
    if enum == -1:
        endneproyden()

        
rezu = 0   
def rez (x=570, y=480, font_color = (0, 0, 0), font_type = 'font/ins.ttf', font_size = 25):
    global rezu
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(""+str(rezu)+"%", True, font_color)
    screen.blit(text, (x, y))

    
#Кнопки, расположение
def button(x,y,w,h, b1, b2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.blit(b2,(x,y))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "play":
                game()
            elif action == "quit":
                pygame.quit()
            elif action == "vix":
                menu()
            elif action == "menu":
                menu1()
            elif action == "game1":
                game1()
            elif action == "game3":
                game3()
            elif action == "game4":
                game4()                
            elif action == "end":
                end()   
            elif action == "dalee":
                pass 
            elif action == "obuchenie":
                obuchenie() 

        screen.blit(b1,(x,y))

COLOR_INACTIVE = pygame.Color(0, 0, 0)
COLOR_ACTIVE = pygame.Color(0, 0, 0)

FONT = pygame.font.Font('font/f.ttf', 30)

class InputBox: #ввод текста

    def __init__(self, x, y, w, h, text=''): #Функция инициализации текста
        self.rect = pygame.Rect(x, y, w, h) #Создание прямоугольника
        self.color = COLOR_INACTIVE #Задание цвета
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color) #Создание поверхности текста, второе это сглаживание
        self.active = False

    def handle_event(self, event): #Обработка событий
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # Если пользователь нажал на треугольник инпут бокс
            if self.rect.collidepoint(event.pos):
                # включает активную переменную актив нового прямоугольика
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 12:
                        self.text += event.unicode
                 # Повторно изображает текст
                self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen): # Показать текст
        screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+3))

class Box: #Название класса

    def __init__(self, x, y, w, h, b, b1): #Функция инициализации текста
        self.image1 = b
        self.image2 = b1
        self.rect = pygame.Rect(x, y, w, h) #Создание прямоугольника
        self.bitmap = self.image1 
        self.active = False
        self.x = x
        self.y = y
    
    def handle_event(self, event): #Обработка событий
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если пользователь нажал прямоугольник
            if self.rect.collidepoint(event.pos):
                # включает активную переменную актив нового прямоугольика
                self.active = not self.active
            else:
                self.active = False
            # инзменяет изображение
            self.bitmap = self.image2 if self.active else self.image1

    def draw(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))# Показать прямоугольник        

def menu1():
    clock = pygame.time.Clock()
    done = False
    tex1 = InputBox(351, 462, 315, 45)
    tex2 = InputBox(352, 539, 315, 45)
    tex = [tex1, tex2]
    
    input_box12 = Box(342, 462, 315, 45, vvod1, vvod2)
    input_box22 = Box(342, 539, 315, 45, vvod1, vvod2)
    input_boxes2 = [input_box12, input_box22]
    while not done:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes2:
                box.handle_event(event)                
            for boxt in tex:
                boxt.handle_event(event)  
        for box in input_boxes2:
            box.draw(screen)                
        for boxt in tex:
            boxt.draw(screen)
                  
        window.blit(screen, (0, 0)) #Координаты скрина
        screen.fill((50, 50, 50))
        screen.blit(bb, (0, 0))
        button(446.6,611,106,41,vhod1,vhod2, "vix")
        pygame.display.update()
        clock.tick(15)

def menu():
    done = True 
    rect0 = pygame.Rect(342,393,315,45)
    rect = pygame.Rect(342,586,315,45)
    pygame.mixer.music.load("sounds/silence.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    global enum
    global rezu
    while done:
        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):  #Вариант 4
                    sys.exit()     
                if rect0.collidepoint(event.pos):  #Вариант 4
                    enum = 2
                    rezu = 0
                     
        screen.fill((50, 50, 50))
        screen.blit(fonmenu, (0, 0)) #Координаты скрина #Второе значение y
        button(342,393,315,45,button2,button1, "play")
        button(342,489,315,45,quit2,quit1, "obuchenie") 
        button(342,586,315,45,vihod2,vihod1, "dalee")
        window.blit(screen, (0, 0))
        pygame.display.flip()
 
def obuchenie():
    rect = pygame.Rect(680,930,43,43)
    rect2 = pygame.Rect(723,930,43,43)
    rect3 = pygame.Rect(766,930,43,43)
    rect4 = pygame.Rect(808,930,43,43)
    rect5 = pygame.Rect(851,930,43,43)
    rect6 = pygame.Rect(894,930,43,43)
    rect7 = pygame.Rect(937,930,43,43)
    done = True
    while done:
        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    oneob1.play(), twoob.stop(), threeob.stop(), fourob.stop(), fiveob.stop(), sixob.stop(), sevenob.stop()   
                if rect2.collidepoint(event.pos):
                    oneob1.stop(), twoob.play(), threeob.stop(), fourob.stop(), fiveob.stop(), sixob.stop(), sevenob.stop() 
                if rect3.collidepoint(event.pos):
                    oneob1.stop(), twoob.stop(), threeob.play(), fourob.stop(), fiveob.stop(), sixob.stop(), sevenob.stop() 
                if rect4.collidepoint(event.pos):
                    oneob1.stop(), twoob.stop(), threeob.stop(), fourob.play(), fiveob.stop(), sixob.stop(), sevenob.stop() 
                if rect5.collidepoint(event.pos):
                    oneob1.stop(), twoob.stop(), threeob.stop(), fourob.stop(), fiveob.play(), sixob.stop(), sevenob.stop() 
                if rect6.collidepoint(event.pos):
                    oneob1.stop(), twoob.stop(), threeob.stop(), fourob.stop(), fiveob.stop(), sixob.play(), sevenob.stop() 
                if rect7.collidepoint(event.pos):
                    oneob1.stop(), twoob.stop(), threeob.stop(), fourob.stop(), fiveob.stop(), sixob.stop(), sevenob.play()                    
            
        screen.fill((50, 50, 50))
        screen.blit(oneob, (0, 0))
        oneob1.blit(screen, (0, 0))
        twoob.blit(screen, (0, 0))
        threeob.blit(screen, (0, 0))
        fourob.blit(screen, (0, 0))
        fiveob.blit(screen, (0, 0))
        sixob.blit(screen, (0, 0))
        sevenob.blit(screen, (0, 0))
        button(367,925,266,54,menuob1,menuob, "vix")
        button(680,930,43,43, odin, odin1, "dalee")
        button(723,930,43,43, dva, dva1, "dalee")
        button(766,930,43,43, tri, tri1, "dalee")
        button(808,930,43,43,chetire,chetire1, "dalee")
        button(851,930,43,43,pyat,pyat1, "dalee")
        button(894,930,43,43,shest,shest1, "dalee")
        button(937,930,43,43,sem,sem1, "dalee")
        window.blit(screen, (0, 0))
        pygame.display.flip()
    
def game():           
    done = True 
    w1 = 608
    w2 = 666
    move = False
    rect = pygame.Rect(670, 154, 266, 54)

    move2 = False
    rect2 = pygame.Rect(670, 218, 266, 54)

    move3 = False
    rect3 = pygame.Rect(670, 282, 266, 54)
    
    rect4 = pygame.Rect(670, 346, 266, 54)
    
    pygame.mixer.music.load("sounds/bird.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    
    shagi = pygame.mixer.Sound('sounds/shagi.ogg')
    
    global enum
    global rezu
    while done:
        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):  #Вариант 4
                    move = True
                    boltAnim.play()
                    boltAnim2.stop()
                    boltAnim3.stop()
                    neverno11.play()
                    verno1.stop()
                    neverno12.stop()
                    stayherov1dalee.stop()
                    stayhero.loop = False
                    enum -= 1
                    shagi.play(0, 2000)
                if rect2.collidepoint(event.pos):    #Вариант 8
                    move2 = True
                    boltAnim.play()
                    boltAnim1.stop()
                    boltAnim3.stop()
                    verno1.play()
                    neverno12.stop()
                    neverno11.stop()
                    stayherov1dalee.stop()
                    stayhero.loop = False
                    shagi.play(0, 2000)
                    rezu += 25
                    if rezu == 50:
                        rezu = 25
                    
                if rect3.collidepoint(event.pos):   #Вариант 12
                    move3 = True
                    boltAnim.play()  
                    boltAnim1.stop()
                    boltAnim2.stop() 
                    neverno12.play()
                    verno1.stop()
                    neverno11.stop()
                    stayherov1dalee.stop()
                    shagi.play(0, 1000)
                    stayhero.loop = False
                    enum -= 1
                    stayherov1dalee.stop()
                if rect4.collidepoint(event.pos):   #Далее
                    boltAnim.stop()
                    boltAnim1.stop()  
                    boltAnim2.stop()
                    boltAnim3.stop() 
                    verno1.stop()
                    neverno11.stop()
                    neverno12.stop()
                    stayherov1dalee.play()
                    w1 = 650
                    game1()
                    shagi.stop()

             # Вариант 4                   
        if move:
            w1 -= 2            
        if move and w1 == 470:
            boltAnim.stop()
            move = False
            boltAnim1.play()
            w1 = 650
           
            # Вариант 8   
        if move2:
            w1 -= 2
        if move2 and w1 == 490:
            boltAnim.stop()
            move2 = False
            boltAnim2.play()
            w1 = 650
          
          #Вариант 12   
        if move3:
            w1 -= 2       
        if move3 and w1 == 570:
            boltAnim.stop()
            move3 = False
            boltAnim3.play()
            w1 = 650   
        
        if enum == -1: #Возвращение после провала
            boltAnim.stop()
            boltAnim1.stop()  
            boltAnim2.stop()
            boltAnim3.stop() 
            verno1.stop()
            neverno11.stop()
            neverno12.stop()
            stayherov1dalee.play()
            w1 = 608
            shagi.stop()   

        stayhero.play()
        screen.fill((50, 50, 50)) #Заливка нашего экрана
        screen.blit(test1, (0, 0))
        #Анимация
        boltAnim.blit(screen, (w1, w2)) #Ходьба влево
        boltAnim1.blit(screen, (470, 580)) #Испугался ответ 1
        boltAnim2.blit(screen, (490, 666)) #Большой палец ответ 2
        boltAnim3.blit(screen, (570, 666)) #Стоит последний вариант ответ 3
        stayhero.blit(screen, (650, 666)) #Начальное положение
        stayherov1dalee.blit(screen, (650, 666))
        #Кнопки ответов
        button(670,154,266,54,otvet11,otvet1, "dalee")
        button(670,218,266,54,otvet21,otvet2, "dalee")
        button(670,282,266,54,otvet31,otvet3, "dalee")
        #Верно неверно
        verno1.blit(screen, (670, 218))
        neverno11.blit(screen, (670, 154))
        neverno12.blit(screen, (670, 282))
        #Остальные кнопки
        button(935,928,28,49,rigth1,rigth2, "dalee")
        button(670,346,266,54,dalee1,dalee, "dalee")
        print_text()
        window.blit(screen, (0, 0)) #Координаты скрина
        pygame.display.flip() #Показ окна
        
def game1():  
    done = True 
    w1 = 608
    w2 = 666
    e1 = 608
    e2= 666
    move = False
    rect = pygame.Rect(670, 154, 266, 54)
    move2 = False
    rect2 = pygame.Rect(670, 218, 266, 54)
    move3 = False
    rect3 = pygame.Rect(670, 282, 266, 54)
    rect4 = pygame.Rect(670, 346, 266, 54)
    
    rect5 = pygame.Rect(881,928,28,49)
    rect6 = pygame.Rect(935,928,28,49)
    pygame.mixer.music.load("sounds/groza.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    shagi = pygame.mixer.Sound('sounds/shagi.ogg')
    molnis = pygame.mixer.Sound('sounds/moln.ogg')
    global enum
    global rezu
    while done:
        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):  #Вариант 4
                    move = True
                    boltAnim.play()
                    boltAnim1.stop()
                    neverno21.stop() #Ответы
                    netotveta2.stop() 
                    neverno11.play()
                    molni.play()
                    molni2.stop()
                    hoditv1.stop()
                    stayhero2.loop = False
                    stayherov1dalee.stop()
                    enum -= 1
                    shagi.play(0, 1200)
                    molnis.play(0, 0, 4000)
                    
                if rect2.collidepoint(event.pos):    #Вариант 8
                    move2 = True
                    boltAnim.play()
                    boltAnim1.stop()
                    neverno11.stop() #Ответы
                    netotveta2.stop()
                    neverno21.play()
                    molni.stop()
                    molni2.play()
                    hoditv1.stop()
                    stayhero2.loop = False
                    stayherov1dalee.stop()
                    enum -= 1
                    shagi.play(0, 1500)
                    molnis.play(0, 0, 4000)
                if rect3.collidepoint(event.pos):   #Нет ответов
                    move3 = True
                    hoditv1.play()  
                    boltAnim1.stop()
                    neverno21.stop() #Ответы
                    neverno11.stop()
                    netotveta2.play()
                    molni.stop()
                    molni2.stop()
                    stayhero2.loop = False
                    stayherov1dalee.stop()
                    shagi.play(0, 4000)
                    rezu += 25
                    if rezu >= 51:
                        rezu = 50
                    
                if rect4.collidepoint(event.pos):   #Далее
                    molni.stop()
                    molni2.stop()
                    boltAnim.stop()
                    boltAnim1.stop()
                    hoditv1.stop()
                    neverno21.stop() #Ответы
                    neverno11.stop() #Ответы
                    netotveta2.stop() #Ответы
                    stayherov1dalee.play()
                    w1 = 650
                    e1 = 650
                    shagi.stop()
                    molnis.stop()
                    game3()
                if rect5.collidepoint(event.pos): 
                    molni.stop()
                    molni2.stop()
                    boltAnim.stop()
                    boltAnim1.stop()
                    hoditv1.stop()
                    neverno21.stop() #Ответы
                    neverno11.stop() #Ответы
                    netotveta2.stop() #Ответы
                    stayherov1dalee.play()
                    w1 = 650
                    e1 = 650
                    shagi.stop()
                    molnis.stop()
                    game()
                if rect6.collidepoint(event.pos): 
                    molni.stop()
                    molni2.stop()
                    boltAnim.stop()
                    boltAnim1.stop()
                    hoditv1.stop()
                    neverno21.stop() #Ответы
                    neverno11.stop() #Ответы
                    netotveta2.stop() #Ответы
                    stayherov1dalee.play()
                    w1 = 650
                    e1 = 650
                    shagi.stop()
                    molnis.stop()
                    game3()
      
             # Вариант 4                   
        if move:
            w1 -= 2            
        if move and w1 == 570:
            boltAnim.stop()
            move = False
            boltAnim1.play()
            w1 = 650
           
            # Вариант 8   
        if move2:
            w1 -= 2 
        if move2 and w1 == 570:
            boltAnim.stop()
            move2 = False
            boltAnim1.play()
            w1 = 650
          
        #     #Вариант 12   
        if move3:
            e1 += 2        
        if move3 and w1 >= 1000:
            hoditv1.stop()
            move3 = False
            e1 = 650   
            
            
        if enum == -1: #Возвращение после провала
            molni.stop()
            molni2.stop()
            boltAnim.stop()
            boltAnim1.stop()
            hoditv1.stop()
            neverno21.stop() #Ответы
            neverno11.stop() #Ответы
            netotveta2.stop() #Ответы
            stayherov1dalee.play()
            w1 = 608
            e1 = 608
            shagi.stop()
            molnis.stop()
            
            
            
        stayhero2.play()                   
        screen.fill((0, 0, 0)) #Заливка нашего экрана
        #Отображение переменных
        screen.blit(test2, (0, 0))
        #Анимация
        boltAnim.blit(screen, (w1, w2)) #Ходьба вправо ответ 1
        boltAnim1.blit(screen, (550, 580)) #Ходьба вправо ответ 1
        stayhero2.blit(screen, (650, 666)) #Начальное положение
        molni.blit(screen, (-63, 0)) #Ответ 1 молния
        molni2.blit(screen, (-63, 0)) #Ответ 2 молния
        hoditv1.blit(screen, (e1, e2)) #Ходьба влево ответ 3
        stayherov1dalee.blit(screen, (650, 666)) #Если далее
        #Кнопки ответов
        button(670,154,266,54,otvet11,otvet1, "dalee")
        button(670,218,266,54,otvet21,otvet2, "dalee")
        button(670,282,266,54,netotveta,netotveta1, "dalee")
        #Верно неверно
        netotveta2.blit(screen, (670, 282))
        neverno11.blit(screen, (670, 154))
        neverno21.blit(screen, (670, 218))
        #Остальные кнопки
        button(881,928,28,49,left1,left2, "dalee")
        button(935,928,28,49,rigth1,rigth2, "dalee")
        button(670,346,266,54,dalee,dalee1, "dalee")
        print_text()
        window.blit(screen, (0, 0)) #Координаты скрина
        pygame.display.flip() #Показ окна
        
def game3():
    done = True 
    rect = pygame.Rect(682,137,266,54)
    rect2 = pygame.Rect(682,201,266,54)
    rect3 = pygame.Rect(682,265,265,54)
    rect4 = pygame.Rect(682,330,266,54)
    rect5 = pygame.Rect(881,928,28,49)
    rect6 = pygame.Rect(935,928,28,49)
    pygame.mixer.music.load("sounds/veter.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    vodas = pygame.mixer.Sound('sounds/voda.ogg')
    gorelkas = pygame.mixer.Sound('sounds/gorelka.ogg')
    global enum
    global rezu
    while done:

        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):  #Открытый огонь
                    stayherov3dalee.stop()
                    gorelkav3.play()
                    stayherov3.loop = False
                    nevernov31.play()
                    vernov32.stop()
                    nevernov33.stop()
                    odeyalo.stop()
                    stayherov31.stop()
                    ogonanim1.play()
                    trezhinaanim.play()
                    razliv.play()
                    leda.stop()
                    vodaanim88.stop()
                    odeyaloanim.stop()
                    gorelkas.play(0, 4000)
                    enum -= 1
                    led2.play()
                    vodas.stop()
                if rect2.collidepoint(event.pos):    #Горячая вода
                    stayherov3dalee.stop()
                    gorelkav3.stop()
                    stayherov3.loop = False
                    nevernov31.stop()
                    vernov32.play()
                    nevernov33.stop()
                    odeyalo.stop()
                    stayherov31.stop()
                    leda.play()
                    vodaanim88.play()
                    ogonanim1.stop()
                    trezhinaanim.stop()
                    razliv.stop()
                    odeyaloanim.stop()
                    vodas.play(6)
                    rezu += 25
                    gorelkas.stop()
                    
                    led.loop = False
                    led2.stop()
                if rect3.collidepoint(event.pos):   #Одеяло
                    stayherov3dalee.stop()
                    gorelkav3.stop()
                    stayherov3.loop = False
                    nevernov31.stop()
                    vernov32.stop()
                    nevernov33.play()
                    odeyalo.play()
                    stayherov31.play()
                    odeyaloanim.play()
                    ogonanim1.stop()
                    trezhinaanim.stop()
                    razliv.stop()
                    leda.stop()
                    vodaanim88.stop()
                    enum -= 1
                    led2.stop()
                    gorelkas.stop()
                    vodas.stop()
                if rect4.collidepoint(event.pos):   #Далее
                    gorelkav3.stop()
                    stayherov3dalee.play() #Стоит если далее
                    nevernov31.stop() #Ответ
                    vernov32.stop() #Ответ
                    nevernov33.stop() #Ответ
                    odeyalo.stop()
                    stayherov31.stop()
                    ogonanim1.stop()
                    trezhinaanim.stop()
                    razliv.stop()
                    led2.play()  #Возвращает лед
                    leda.stop()
                    vodaanim88.stop()
                    odeyaloanim.stop()
                    gorelkas.stop()
                    vodas.stop()
                    game4()            
                if rect5.collidepoint(event.pos): 
                    gorelkav3.stop()
                    stayherov3dalee.play() #Стоит если далее
                    nevernov31.stop() #Ответ
                    vernov32.stop() #Ответ
                    nevernov33.stop() #Ответ
                    odeyalo.stop()
                    stayherov31.stop()
                    ogonanim1.stop()
                    trezhinaanim.stop()
                    razliv.stop()
                    led2.play()  #Возвращает лед
                    leda.stop()
                    vodaanim88.stop()
                    odeyaloanim.stop()
                    gorelkas.stop()
                    vodas.stop()
                    game1()
                if rect6.collidepoint(event.pos): 
                    gorelkav3.stop()
                    stayherov3dalee.play() #Стоит если далее
                    nevernov31.stop() #Ответ
                    vernov32.stop() #Ответ
                    nevernov33.stop() #Ответ
                    odeyalo.stop()
                    stayherov31.stop()
                    ogonanim1.stop()
                    trezhinaanim.stop()
                    razliv.stop()
                    led2.play()  #Возвращает лед
                    leda.stop()
                    vodaanim88.stop()
                    odeyaloanim.stop()
                    gorelkas.stop()
                    vodas.stop()
                    game4()
                    
        if enum == -1: #Возвращение после провала
            gorelkav3.stop()
            stayherov3dalee.play() #Стоит если далее
            nevernov31.stop() #Ответ
            vernov32.stop() #Ответ
            nevernov33.stop() #Ответ
            odeyalo.stop()
            stayherov31.stop()
            ogonanim1.stop()
            trezhinaanim.stop()
            razliv.stop()
            led2.play()  #Возвращает лед
            leda.stop()
            vodaanim88.stop()
            odeyaloanim.stop()   
            gorelkas.stop()
            vodas.stop()
            
        led.play()
        stayherov3.play()
        screen.fill((50, 50, 50)) #Заливка нашего экрана
        screen.blit(fonv3, (0, 0))

        #Анимация
        led.blit(screen, (38, 465)) #Лед на трубе
        led2.blit(screen, (38, 465)) #Лед на трубе
        leda.blit(screen, (38, 465)) #Лед тает
        gorelkav3.blit(screen, (360, 351)) #Герой с горелкой, потом пугается
        stayherov3.blit(screen, (482, 352)) #Начальное положение героя
        stayherov3dalee.blit(screen, (482, 352)) #После нажатия далее
        odeyalo.blit(screen, (33, 499)) #Одеяло без льда
        stayherov31.blit(screen, (482, 352)) #Снова начальное положение для одеяла
        ogonanim1.blit(screen, (310, 575)) #Анимация огня
        trezhinaanim.blit(screen, (219, 476)) #Появление трещины
        vodaanim88.blit(screen, (124, 281)) #Льется вода
        odeyaloanim.blit(screen, (33, 499)) #Замерзание одеяла
        razliv.blit(screen, (197, 207)) #Вытекает нефть после пробития
        
        #Кнопки ответов
        button(682,137,266,54,otvetv311,otvetv31, "dalee")
        button(682,201,266,54,otvetv321,otvetv32, "dalee")
        button(682,265,265,54,otvetv331,otvetv33, "dalee")
        #Верно неверно
        vernov32.blit(screen, (682, 201))
        nevernov31.blit(screen, (682, 137))
        nevernov33.blit(screen, (682, 265))
        #Остальные кнопки
        button(881,928,28,49,left1,left2, "dalee")
        button(935,928,28,49,rigth1,rigth2, "dalee")
        button(682,330,266,54,dalee31,dalee3, "dalee")
        print_text()
        window.blit(screen, (0, 0)) #Координаты скрина
        pygame.display.flip() #Показ окна

def game4():
    done = True 
    rect = pygame.Rect(682,137,266,54)
    rect2 = pygame.Rect(682,201,266,54)
    rect3 = pygame.Rect(682,265,265,54)
    rect4 = pygame.Rect(682,330,266,54)
    rect5 = pygame.Rect(881,928,28,49)
    w1 = 411
    w2 = 323
    move = False
    pygame.mixer.music.load("sounds/nps.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    molotok = pygame.mixer.Sound('sounds/molotok.ogg')
    svarkas = pygame.mixer.Sound('sounds/svarka.ogg')
    vzrivs = pygame.mixer.Sound('sounds/vzriv.ogg')
    shagiv4 = pygame.mixer.Sound('sounds/shagiv4.ogg')
    global enum
    global rezu
    while done:
        for event in pygame.event.get(): #Получение всех событий
            if event.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):  #Огневые работы
                    w1 = 411
                    svarlav4.play()
                    stayherov4.loop = False
                    nevernov41.play()
                    nevernov42.stop()
                    nevernov43.stop()
                    stayherov41.stop()
                    izkri.play()
                    vzriv.play()
                    probil.stop()
                    neft.stop()
                    lezhitv4.play()
                    hodit.stop()
                    svarkas.play(0, 2000, 1200)
                    vzrivs.play(0, 0, 1200)
                    molotok.stop()
                    shagiv4.stop()
                    enum -= 1
                if rect2.collidepoint(event.pos):    #Ремонт
                    w1 = 411
                    svarlav4.stop()
                    stayherov4.loop = False
                    nevernov41.stop()
                    nevernov42.play()
                    nevernov43.stop()
                    stayherov41.stop()
                    probil.play()
                    neft.play()
                    izkri.stop()
                    vzriv.stop()
                    lezhitv4.stop()
                    hodit.stop()
                    enum -= 1
                    molotok.play(0, 2500)
                    svarkas.stop()
                    vzrivs.stop()
                    shagiv4.stop()
                if rect3.collidepoint(event.pos):   #Неверные
                    svarlav4.stop()
                    stayherov4.loop = False
                    nevernov41.stop()
                    nevernov42.stop()
                    nevernov43.play()
                    probil.stop()
                    neft.stop()
                    izkri.stop()
                    vzriv.stop()
                    hodit.play()
                    lezhitv4.stop()
                    stayherov41.stop()
                    shagiv4.play(0, 3000)
                    rezu += 25
                    molotok.stop()
                    svarkas.stop()
                    vzrivs.stop()
                    move = True
                if rect4.collidepoint(event.pos):   #Завершить
                    w1 = 411
                    svarlav4.stop()
                    nevernov41.stop()
                    nevernov42.stop()
                    nevernov43.stop()
                    stayherov41.play()
                    probil.stop()
                    neft.stop()
                    izkri.stop()
                    vzriv.stop()
                    lezhitv4.stop()
                    hodit.stop()
                    if rezu >= 100:
                        rezu = 100
                    molotok.stop()
                    svarkas.stop()
                    vzrivs.stop()
                    shagiv4.stop()
                    end()

                if rect5.collidepoint(event.pos):   #Завершить
                    w1 = 411
                    svarlav4.stop()
                    nevernov41.stop()
                    nevernov42.stop()
                    nevernov43.stop()
                    stayherov41.play()
                    probil.stop()
                    neft.stop()
                    izkri.stop()
                    vzriv.stop()
                    lezhitv4.stop()
                    hodit.stop()
                    molotok.stop()
                    svarkas.stop()
                    vzrivs.stop()
                    shagiv4.stop()
                    game3()
        
        if enum == -1: #Возвращение после провала
            w1 = 411
            svarlav4.stop()
            nevernov41.stop()
            nevernov42.stop()
            nevernov43.stop()
            stayherov41.play()
            probil.stop()
            neft.stop()
            izkri.stop()
            vzriv.stop()
            lezhitv4.stop()
            hodit.stop()     
            molotok.stop()
            svarkas.stop()
            vzrivs.stop()
            shagiv4.stop()
            
        if move:
            w1 += 5    
        strelka1.play()
        strelka2.play()
        stayherov4.play()
        screen.fill((50, 50, 50)) #Заливка нашего экрана
        screen.blit(fonv4, (0, 0))
        #Анимация
        svarlav4.blit(screen, (381, 502)) #Начальное положение сварки
        stayherov4.blit(screen, (508, 329)) #Начальное положение героя
        stayherov41.blit(screen, (508, 329)) #При кнопке завершить тест
        izkri.blit(screen, (344, 691)) #Искры при сварке
        vzriv.blit(screen, (-94, 292)) #Взрыв после сварки
        probil.blit(screen, (344, 431)) #Бьет ключем
        neft.blit(screen, (256, 389)) #Появление нефти после ремонта
        button(682,330,266,54,dalee41,dalee4, "dalee")
        hodit.blit(screen, (w1, w2)) #Уходит за экран
        strelka1.blit(screen, (556, 43)) #Cтрелка правая
        strelka2.blit(screen, (405, 60)) #Cтрелка левая
        lezhitv4.blit(screen, (512, 764)) #Лежит без сознания
        #Кнопки ответов
        button(682,137,266,54,otvetv411,otvetv41, "dalee")
        button(682,201,266,54,otvetv421,otvetv42, "dalee")
        button(682,265,265,54,otvetv431,otvetv43, "dalee")
        #Верно неверно
        nevernov41.blit(screen, (682, 137))
        nevernov42.blit(screen, (682, 201))
        nevernov43.blit(screen, (682, 265))
        #Остальные кнопки
        button(881,928,28,49,left1,left2, "dalee")
        print_text()
        window.blit(screen, (0, 0)) #Координаты скрина
        pygame.display.flip() #Показ окна
        
def end():  
    end = True 
    pygame.mixer.music.load("sounds/silence.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    while end:
        for e in pygame.event.get(): #Получение всех событий
            if e.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается
                

        screen.fill((50, 50, 50))
        screen.blit(bb2, (0, 0)) #Координаты скрина
        button(342,551,315,45,menuend1,menuend2, "vix")
        button(342,618,315,45,vih1,vih2, "quit") #Второе значение y
        rez()
        window.blit(screen, (0, 0))
        pygame.display.update()
        clock.tick(15)

def endneproyden():  
    end = True 
    global enum
    global rezu
    rect = pygame.Rect(342,487,315,45)
    pygame.mixer.music.load("sounds/silence.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    while end:
        for e in pygame.event.get(): #Получение всех событий
            if e.type == pygame.QUIT: #Если событие выход
                sys.exit() #Цикл завершается и программа закрывается
            if e.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(e.pos):
                    enum = 2
                    rezu = 0
                    

        screen.fill((50, 50, 50))
        screen.blit(fonneproy, (188, 294)) #Координаты скрина
        button(342,551,315,45,menuneproyden1,menuneproyden, "vix")
        button(342,617,315,45,vihodneproyden1,vihodneproyden, "quit")
        button(342,487,315,45,zanovoneproyden1,zanovoneproyden, "play") #Второе значение y
        window.blit(screen, (0, 0))
        pygame.display.update()
        clock.tick(15)



menu1()
pygame.quit()