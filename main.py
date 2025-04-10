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

Instruction = Challenge | Farm | EternityFarm


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
        # Challenge(ec=2, it=1, path=Path.TIME),
        # Farm(ep_target=10, path=Path.TIME, ip_auto=100, ep_auto=1),
        # Challenge(ec=2, it=2, path=Path.TIME),
        # Challenge(ec=3, it=1, path=Path.ANTIMATTER),
        # Farm(ep_target=28, path=Path.TIME, ip_auto=100, ep_auto=1),
        # EternityFarm(eternity_target="5"),
        # Challenge(ec=1, it=1, path=Path.ANTIMATTER),
        # Challenge(ec=1, it=2, path=Path.ANTIMATTER),
        # Challenge(ec=2, it=3, path=Path.ANTIMATTER),
        # Challenge(ec=1, it=3, path=Path.INFINITY),
        # Farm(ep_target=33, path=Path.TIME, ip_auto=250, ep_auto=1),
        # Challenge(ec=3, it=2, path=Path.ANTIMATTER),
        # Challenge(ec=1, it=4, path=Path.INFINITY),
        # Challenge(ec=1, it=5, path=Path.INFINITY),
        # Challenge(ec=3, it=3, path=Path.ANTIMATTER),
        
        # Challenge(ec=3, it=5, path=Path.TIME, ip_auto=1),
        # Challenge(ec=2, it=4, path=Path.ANTIMATTER),
        # Challenge(ec=2, it=5, path=Path.TIME),
        # Challenge(ec=3, it=4, path=Path.ANTIMATTER),

        # Challenge(ec=4, it=1, path=Path.TIME),
        # Challenge(ec=4, it=2, path=Path.TIME),
        # Challenge(ec=4, it=3, path=Path.TIME),
        # Farm(ep_target=40,path=Path.TIME,  ip_auto=200, ep_auto=1),
        # Challenge(ec=5, it=1, path=Path.TIME),
        # Challenge(ec=5, it=2, path=Path.TIME),
        # Challenge(ec=5, it=3, path=Path.TIME),
        # Challenge(ec=5, it=4, path=Path.TIME),
        # Challenge(ec=5, it=5, path=Path.TIME),

        # Challenge(ec=4, it=4, path=Path.TIME),
        
        # Challenge(ec=6, it=1, path=Path.ACTIVE),
        # Challenge(ec=6, it=2, path=Path.ACTIVE),
        # Challenge(ec=6, it=3, path=Path.ACTIVE),
        # Challenge(ec=6, it=4, path=Path.ACTIVE),
        # Challenge(ec=6, it=5, path=Path.ACTIVE),

        # Challenge(ec=7, it=1, path=Path.TIME),
        # Challenge(ec=7, it=2, path=Path.TIME),
        # Challenge(ec=7, it=3, path=Path.TIME),
        # Challenge(ec=7, it=4, path=Path.TIME),
        

        # Challenge(ec=8, it=1, path=Path.TIME),
        # Challenge(ec=8, it=2, path=Path.TIME),
        # Challenge(ec=8, it=3, path=Path.TIME),
        
        Challenge(ec=9, it=1, path=Path.ACTIVE),
        Challenge(ec=9, it=2, path=Path.ACTIVE),
        Challenge(ec=9, it=3, path=Path.ACTIVE),
        Challenge(ec=9, it=4, path=Path.ACTIVE),
        Challenge(ec=9, it=5, path=Path.ACTIVE),

        Challenge(ec=10, it=1, path=Path.ACTIVE),
        Farm(ep_target=270, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211", ep_auto=10),
        Challenge(ec=10, it=2, path=str(Path.ANTIMATTER)+" 193 191 212 214 211"),
        Challenge(ec=10, it=3, path=str(Path.ANTIMATTER)+" 193 191 212 214 211"),
        Farm(ep_target=400, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211, 224, 232", ep_auto=10),
        Challenge(ec=10, it=4, path=str(Path.ANTIMATTER)+" 193 191 212 214 211, 224, 232"),

        Farm(ep_target=500, ip_auto=1000, path=str(Path.ACTIVE)+" 193 191 212 214 211 224 232", ep_auto=10),
        Challenge(ec=8, it=4, path=str(Path.ACTIVE) + " 193 191 212 214 211 224 232"),


        Challenge(ec=10, it=5, path=str(Path.ANTIMATTER)+" 193 191 212 214 211 224 232"),

        Challenge(ec=8, it=5, path=Path.ACTIVE),

        Challenge(ec=7, it=5, path=Path.TIME),

        Challenge(ec=11, it=1, path=Path.TIME),
        Challenge(ec=11, it=2, path=Path.TIME),
        Challenge(ec=11, it=3, path=Path.TIME),
        Challenge(ec=11, it=4, path=Path.TIME),
        Challenge(ec=11, it=5, path=Path.TIME),

        Challenge(ec=12, it=1, path=Path.TIME),
        Challenge(ec=12, it=2, path=Path.TIME),
        Challenge(ec=12, it=3, path=Path.TIME),
        Challenge(ec=12, it=4, path=Path.TIME),
        Challenge(ec=12, it=5, path=Path.TIME),

        Challenge(ec=4, it=5, path=Path.TIME),
    ]

    with open("challenges.dsl", 'w') as f:
        write_instructions(f, instructions)

    print("Instructions written to 'challenges.dsl'.")


if __name__ == "__main__":
    main()