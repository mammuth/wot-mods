from math import floor

import BigWorld
from Avatar import PlayerAvatar
from gui.battle_control.controllers.battle_field_ctrl import BattleFieldCtrl

from xfw.events import registerEvent
from xvm_main.python.logger import *


# todo what is deterministic=False?
@xvm.export('vehicleDistance', deterministic=False)
def vehicleDistance(name):
    # todo doesn't get updated ever :(
    # name is a player name like "JeffForPresident"

    print('vehicleDistance called')
    print('name: ' + name)
    
    player = BigWorld.player()
    for vehicle in player.arena.vehicles.itervalues():
        print('vehicle: ' + str(vehicle))
        entity = BigWorld.entity(int(vehicle['avatarSessionID']))
        # todo filter allies
        # todo only return if entity name == name
        if entity is not None and entity.publicInfo.name == name:
            print('entity: ' + str(entity.__dict__))
            print('name: ' + str(entity.publicInfo.name))
            print('player position: ' + str(player.position))
            print('opponent position: ' + str(entity.position))
            print('diff:')
            diff = int(floor(player.position.distTo(entity.position)))
            print(diff)
            return diff

    print('oh nein')
    return 'oh nein'
