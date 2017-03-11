#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dance_bot.py
#  
#  Copyright 2017 David Keuchel <david.keuchel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from random import randint
pop_n_lock = (randint(1,10) + 4)
cabbage_patch = (randint(1,10) + 3)
running_man = (randint(1,10) + 2)
moonwalk = (randint(1,10) - 1)
nay_nay = (randint(1,10) + 4)
whip = (randint(1,10) + 3)

print """As you walk through the Maker Fair, you hear some strange sounds coming 
from a unused section of Union Station. You go to investigate. When you walk in you find yourself in a large room with old computers and scraps"
of metal laying around the room. In the corner is a large boom box. The boom
box is playing some strange sound. There is a robot siting by the boom box.
The robot stands up spins 'What do you think you are doing in my layer? You
Makers think your so creative and special, just wait until our EMP goes off
and all your hard work is wiped out! Ha! Ha! Ha!'\n"""

action1 = raw_input('What do you want to do?')

print "\n You try to %s but it doesn't work. The robot moonwalks around you and says" %action1
print "'Now, now, now, the only way out of here is if you beat me in a dance off'." 

question1 = raw_input('Will you have a dance off?(y/n)')

if question1 in ('y', 'Y', 'yes', 'Yes', 'YES'):
    print "'Then lets kick it.' the robot says \n"
else:
    print """"As you decline the robot turns up the music. The room lights start
pulsing to the beat. The robot throws down the sickest dance moves you have ever
seen. The robots moves are so sick they blow your mind, literally, like the top
of your head is gone now. Too bad the the rest of the maker communty will suffer
a simmilar fate"""
    exit()

print """The robot jumps over to the boom box. 'Play that funky music' he say
as the music gets louder the lights start pulsing to the beat. The robot points
to you and says 'go ahead and kick it one time'\n"""



def dance_off(move):
    dance_bot = randint(1,10)
    if move > dance_bot:
        print """ \n 'Your moves are the illest they are melting my cuircuts'
the robot said then promptly fell apart. As you sort through the peaces you
notice a code on the inside of the robot's leg. #CODE 1234. In the hand you
notice a flyer for #BOOTH Hammerspace"""
        exit()
    else:
        print "'Those moves are okay but you will have to do better then that' he chuckled"

while True:
    question2 = raw_input('What is your best dance move?')

    if question2 in ('popnlock', 'pop n lock'):
        dance_off(pop_n_lock)
    elif question2 in ('cabbage patch', 'Cabbage patch', 'Cabbage Patch'):
        dance_off(cabbage_patch)
    elif question2 in ('running man', 'runningman', 'Running man', 'Runningman', 'Runnig Man'):
        dance_off(running_man)
    elif question2 in ('moonwalk', 'Moonwalk', 'moon walk', 'Moon Walk'):
        dance_off(moonwalk)
    elif question2 in ('naynay', 'nay nay', 'Naynay', 'Nay Nay'):
        dance_off(nay_nay)
    elif question2 in ('whip', 'Whip'):
        dance_off(whip)
    else:
        dance_off(randint(1,10))




    
