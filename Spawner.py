import config
from defs import *
from structures import Structures
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Spawner:
    def __init__(self, bot):
        self.b = bot
        self.spawn = None
        self.builder_called = 0

    def get_count(self, role):
        count = 0
        creeps = [c for c in Object.keys(Game.creeps)]
        for n in creeps:
            creep = Game.creeps[n]
            if creep.memory['role'] == role:
                count += 1
        return count


    def harvesters(self, st):
        m = {"role": 'harvester'}
        name = m['role'] + Game.time
        for spawn in st:
            if spawn.store.getUsedCapacity(RESOURCE_ENERGY) >= 210:
                if not spawn.spawning:
                    if not self.b.is_sleeping:
                        print("SPAWNING:", name)
                        spawn.createCreep([WORK, CARRY, MOVE], m['role'] + Game.time, m)
                        self.b.sleep(1)
    
