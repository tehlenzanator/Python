from defs import *
import structures
import config

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

class Harvester:
    def __init__(self, creep: Creep):
        self.creep = creep
        self.structure = structures.Structures(None, creep)
    
    def run(self):
        creep = self.creep
        if creep.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
            if config.creep_say: creep.say("Harvest..")
            source = self.creep.pos.findClosestByPath(FIND_SOURCES)
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)
        else:
            for target in self.structure.targets_need_filling():
                if config.creep_say: creep.say(f"filling {target.name}...")
                if creep.transfer(target, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                    creep.moveTo(target)
