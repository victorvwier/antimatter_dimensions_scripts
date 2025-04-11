from dataclasses import dataclass
from enum import Enum
from typing import TextIO

@dataclass
class Challenge:
    ec: int
    it: int
    path: str
    ip_auto: int | None = None



@dataclass
class Farm:
    ep_target: int
    ip_auto: int
    path: str
    ep_auto: int

@dataclass
class EternityFarm:
    eternity_target: str

@dataclass
class Inline:
    command: str

@dataclass
class FinalCommand:
    pass

Instruction = Challenge | Farm | EternityFarm | Inline | FinalCommand


def write_instructions(f: TextIO, instructions: list[Instruction]):
    def s(s):
        f.write(f"{s}\n")
    for inst in instructions:
        if isinstance(inst, Challenge):
            s(f"if ec{inst.ec} completions < {inst.it} {{")
            if inst.ip_auto is not None:
                s(f"  auto infinity 1e+{inst.ip_auto} x highest")
            if inst.ec == 4 or inst.ec == 10:
                s(f"  auto infinity 5.1s")
            elif "181" in str(inst.path):
                s(f"  auto infinity off")
            s(f"  studies purchase {inst.path}")
            s(f"  start ec {inst.ec}")
            s(f"  wait pending ip >= 1e+{get_ip_goal(inst.ec, inst.it)}")
            s(f"  infinity")
            s("}")
        elif isinstance(inst, Farm):
            s(f"if ep < 1e+{inst.ep_target} {{")
            
            if "181" in str(inst.path):
                s(f"  auto infinity off")
            else:
                s(f"  auto infinity 1e+{inst.ip_auto} x highest")
            s(f"  auto eternity 1e+{inst.ep_auto} x highest")
            s(f"  studies purchase {inst.path}")
            s(f"  wait ep >=1e+{inst.ep_target}")
            s("}")
        elif isinstance(inst, EternityFarm):
            s(f"if eternities < 1e+{inst.eternity_target} {{")
            s(f"  auto infinity 1.8e+308 ip")
            s(f"  auto eternity 1 ep")
            s(f"  wait eternities > 1e+{inst.eternity_target}\n")
            s("}")
        elif isinstance(inst, Inline):
            s(f"{inst.command}")
        elif isinstance(inst, FinalCommand):
            s(f"while ep < 1e+6000 {{")
            s("  studies nowait purchase 11,21,22,31,32,33,41,42,51,61,62,73,83,93,103,111,121,131,141,151,161,162,171,181,191,192,193,201,72,82,92,102,214,228,234,213,226,212,224,232,211,222,71,81,91,101")
            s("  start dilation")
            s("  pause 3s")
            s("  studies respec")
            s("  eternity")
            s("  studies nowait purchase 11,21,22,31,32,33,41,42,51,61,62,73,83,93,103,111,121,131,141,151,161,162,171,181,191,192,193,201,72,82,92,102,214,228,234,213,226,212,224,232,211,222,71,81,91,101")
            s("  pause 10s")
            s("  studies respec")
            s("  eternity")
            s("}")

class Path(Enum):
    TIME = "11-61, 62, time, 111, idle, 151-171"
    ANTIMATTER = "11-61, 62, antimatter, 111, idle, 151-171"
    INFINITY = "11-61, 62, infinity, 111, idle, 151-171"
    ACTIVE = "11-61, 62, time, 111, active, 151-171, 181"
    def __str__(self):
        return str(self.value)

def get_ip_goal(ec, it):
    lut = [
        (1800, 200),
        (975, 175),
        (600, 75),
        (2750, 550),
        (750, 400),
        (850, 250),
        (2000, 530),
        (1300, 900),
        (1750, 250),
        (3000,300),
        (450,200),
        (110000,12000)
    ]
    mult = lut[ec-1]
    return mult[0] + (it-1) * mult[1]
    

def main():
    instructions: list[Instruction] = [
        Farm(ep_target=1, path=Path.TIME, ip_auto=10, ep_auto=1),
        Challenge(ec=2, it=1, path=Path.TIME),
        Farm(ep_target=10, path=Path.TIME, ip_auto=100, ep_auto=1),
        Challenge(ec=2, it=2, path=Path.TIME),
        Challenge(ec=3, it=1, path=Path.ANTIMATTER),
        Farm(ep_target=28, path=Path.TIME, ip_auto=100, ep_auto=1),
        EternityFarm(eternity_target="5"),
        Challenge(ec=1, it=1, path=Path.ANTIMATTER),
        Challenge(ec=1, it=2, path=Path.ANTIMATTER),
        Challenge(ec=2, it=3, path=Path.ANTIMATTER),
        Challenge(ec=1, it=3, path=Path.INFINITY),
        Farm(ep_target=33, path=Path.TIME, ip_auto=250, ep_auto=1),
        Challenge(ec=3, it=2, path=Path.ANTIMATTER),
        Challenge(ec=1, it=4, path=Path.INFINITY),
        Challenge(ec=1, it=5, path=Path.INFINITY),
        Challenge(ec=3, it=3, path=Path.ANTIMATTER),
        
        Challenge(ec=3, it=5, path=Path.TIME, ip_auto=1),
        Challenge(ec=2, it=4, path=Path.ANTIMATTER),
        Challenge(ec=2, it=5, path=Path.TIME),
        Challenge(ec=3, it=4, path=Path.ANTIMATTER),

        Challenge(ec=4, it=1, path=Path.TIME),
        Challenge(ec=4, it=2, path=Path.TIME),
        Challenge(ec=4, it=3, path=Path.TIME),
        Farm(ep_target=40,path=Path.TIME,  ip_auto=200, ep_auto=1),
        Challenge(ec=5, it=1, path=Path.TIME),
        Challenge(ec=5, it=2, path=Path.TIME),
        Challenge(ec=5, it=3, path=Path.TIME),
        Challenge(ec=5, it=4, path=Path.TIME),
        Challenge(ec=5, it=5, path=Path.TIME),

        Challenge(ec=4, it=4, path=Path.TIME),
        
        Challenge(ec=6, it=1, path=Path.ACTIVE),
        Challenge(ec=6, it=2, path=Path.ACTIVE),
        Challenge(ec=6, it=3, path=Path.ACTIVE),
        Challenge(ec=6, it=4, path=Path.ACTIVE),
        Challenge(ec=6, it=5, path=Path.ACTIVE),

        Challenge(ec=7, it=1, path=Path.TIME),
        Challenge(ec=7, it=2, path=Path.TIME),
        Challenge(ec=7, it=3, path=Path.TIME),
        Challenge(ec=7, it=4, path=Path.TIME),
        

        Challenge(ec=8, it=1, path=Path.TIME),
        Challenge(ec=8, it=2, path=Path.TIME),
        Challenge(ec=8, it=3, path=Path.TIME),
        
        Challenge(ec=9, it=1, path=Path.ACTIVE),
        Challenge(ec=9, it=2, path=Path.ACTIVE),
        Challenge(ec=9, it=3, path=Path.ACTIVE),
        Challenge(ec=9, it=4, path=Path.ACTIVE),
        Challenge(ec=9, it=5, path=Path.ACTIVE),

        Challenge(ec=10, it=1, path=Path.ACTIVE),
        Farm(ep_target=270, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211", ep_auto=10),
        Challenge(ec=10, it=2, path=str(Path.ANTIMATTER)+" 181 193 191 212 214 211"),
        Challenge(ec=10, it=3, path=str(Path.ANTIMATTER)+" 181 193 191 212 214 211"),
        Farm(ep_target=400, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211, 224, 232", ep_auto=10),
        Challenge(ec=10, it=4, path=str(Path.ANTIMATTER)+" 181 193 191 212 214 211, 224, 232"),

        Farm(ep_target=500, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211 224 232", ep_auto=10),
        Challenge(ec=8, it=4, path=str(Path.TIME) + " 181 193 191 212 214 211 224 232"),


        

        # Challenge(ec=8, it=5, path=str(Path.TIME) + " 181 193 191 212 214 211 224 232"),

        # Challenge(ec=7, it=5, path=Path.TIME),
        # Farm(ep_target=600, ip_auto=1000, path="11,21,22,31,32,33,41,42,51,61,62,73,83,93,103,111,121,131,141,151,161,162,171,181,191,192,193,201,72,82,92,102,214,228,234,213,226,212,224,232,211,222,71,81,91,101", ep_auto=15),
        # Challenge(ec=11, it=1, path="11,21,22,31,32,41,42,51,61,62,71,81,91,101,111,123,133,143,151,161,162,171,181,191,192,193,211,212,213,222,223,225,231,214,233"),
        # Challenge(ec=11, it=2, path="11,21,22,31,32,41,42,51,61,62,71,81,91,101,111,123,133,143,151,161,162,171,181,191,192,193,211,212,213,222,223,225,231,214,233"),
        # Challenge(ec=11, it=3, path="11,21,22,31,32,41,42,51,61,62,71,81,91,101,111,123,133,143,151,161,162,171,181,191,192,193,211,212,213,222,223,225,231,214,233"),
        # Challenge(ec=11, it=4, path="11,21,22,31,32,41,42,51,61,62,71,81,91,101,111,123,133,143,151,161,162,171,181,191,192,193,211,212,213,222,223,225,231,214,233"),
        # Challenge(ec=12, it=1, path="11,22,21,33,31,32,42,41,51,61,62,73,83,93,103,111,122,132,142,151,162,161,171,181,191,193,211,212,213,214,228,234,224,232,222,192"),
        # Challenge(ec=12, it=2, path="11,22,21,33,31,32,42,41,51,61,62,73,83,93,103,111,122,132,142,151,162,161,171,181,191,193,211,212,213,214,228,234,224,232,222,192"),
        # Challenge(ec=12, it=3, path="11,22,21,33,31,32,42,41,51,61,62,73,83,93,103,111,122,132,142,151,162,161,171,181,191,193,211,212,213,214,228,234,224,232,222,192"),
        # Challenge(ec=12, it=4, path="11,22,21,33,31,32,42,41,51,61,62,73,83,93,103,111,122,132,142,151,162,161,171,181,191,193,211,212,213,214,228,234,224,232,222,192"),
        
        # Challenge(ec=10, it=5, path=str(Path.ANTIMATTER)+" 181 193 191 212 214 211 224 232"),
        # Challenge(ec=12, it=5, path="11,22,21,33,31,32,42,41,51,61,62,73,83,93,103,111,122,132,142,151,162,161,171,181,191,193,211,212,213,214,228,234,224,232,222,192"),

        # Farm(ep_target=1000, ip_auto=1000, path="11,21,22,31,32,33,41,42,51,61,62,73,83,93,103,111,121,131,141,151,161,162,171,181,191,192,193,201,72,82,92,102,214,228,234,213,226,212,224,232,211,222,71", ep_auto=20),
        
        # Challenge(ec=11, it=5, path="11,21,22,31,32,41,42,51,61,62,71,81,91,101,111,123,133,143,151,161,162,171,181,191,192,193,211,212,213,222,223,225,231,214,233"),
        # Farm(ep_target=1500, ip_auto=1000, path="11,21,22,31,32,33,41,42,51,61,62,73,83,93,103,111,121,131,141,151,161,162,171,181,191,192,193,201,72,82,92,102,214,228,234,213,226,212,224,232,211,222", ep_auto=100),
        # FinalCommand(),
        
    ]

    with open("challenges.dsl", 'w') as f:
        write_instructions(f, instructions)

    print("Instructions written to 'challenges.dsl'.")


if __name__ == "__main__":
    main()