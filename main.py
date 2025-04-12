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

class Class:
    studies: str | None = None
    auto_ip: str | None = None
    def _s(self, s, f):
        if "studies purchase" in s:
            newstudies = s.split("purchase ")[1]
            if self.studies == newstudies:
                self.studies = newstudies
                return 
            self.studies = newstudies
        elif "studies respec" in s or "start ec" in s:
            self.studies = None
        elif "auto infinity" in s:
            newauto_ip = s.split("infinity ")[1]
            if self.auto_ip == newauto_ip:
                self.auto_ip = newauto_ip
                return
            self.auto_ip = newauto_ip
        f.write(f"{s}\n")
    
    def write_instructions(self, f: TextIO, instructions: list[Instruction]):
        def s(s):
            self._s(s, f)
        for inst in instructions:
            if isinstance(inst, Challenge):
                if inst.ip_auto is not None:
                    s(f"auto infinity 1e+{inst.ip_auto} x highest")
                if inst.ec == 4 or inst.ec == 10:
                    s(f"auto infinity 5.1s")
                elif "181" in str(inst.path) or "151-214" in str(inst.path):
                    s(f"auto infinity off")
                s(f"studies purchase {inst.path}")
                s(f"start ec {inst.ec}")
                s(f"wait ec{inst.ec} completions >= {inst.it}")
                if inst.ec == 4 or inst.ec == 10 or "181" in str(inst.path) or "151-214" in str(inst.path):
                    s(f"auto infinity 1e+100 x highest")
            elif isinstance(inst, Farm):                
                if "181" in str(inst.path):
                    s(f"auto infinity off")
                else:
                    s(f"auto infinity 1e+{inst.ip_auto} x highest")
                s(f"auto eternity 1e+{inst.ep_auto} x highest")
                s(f"studies purchase {inst.path}")
                s(f"wait ep >=1e+{inst.ep_target}")
                s(f"studies respec")
                s(f"eternity")
            elif isinstance(inst, EternityFarm):
                s(f"auto infinity 1.8e+308 ip")
                s(f"auto eternity 1 ep")
                s(f"wait eternities > 1e+{inst.eternity_target}")
                s(f"auto infinity 1e+100 x highest")
                s(f"auto eternity 1e+10 x highest")
                s(f"studies respec")
                s(f"eternity")
                
            elif isinstance(inst, Inline):
                s(f"{inst.command}")
            elif isinstance(inst, FinalCommand):
                s(f"studies nowait purchase 11-111 time 111 active 151-214 dark")
                s(f"unlock dilation")
                s(f"while ep < 1e+10000 {{")
                s(f"auto infinity off")
                s(f"auto eternity off")
                s(f"studies nowait purchase 11-111 time 111 active 151-214 dark")
                s(f"start dilation")
                s(f"pause 3s")
                s(f"studies respec")
                s(f"eternity")
                s(f"studies nowait purchase 11-111 time 111 active 151-214 dark")
                s(f"pause 10s")
                s(f"studies respec")
                s(f"eternity")
                s(f"}}")

class Path(Enum):
    TIME = "11-61 62 time 111 idle 151-171"
    ANTIMATTER = "11-61 62 antimatter 111 idle 151-171"
    INFINITY = "11-61 62 infinity 111 idle 151-171"
    ACTIVE = "11-61 62 time 111 active 151-171"
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
        # Early game farming and challenges to build up resources
        Farm(ep_target=1, path="11-61", ip_auto=10, ep_auto=1),  # Early game farm
        Farm(ep_target=14, path=Path.ACTIVE, ip_auto=10, ep_auto=1), # Farm for time dimensions
        Challenge(ec=2, it=1, path=Path.ACTIVE), # Time challenge 2, iteration 1
        Challenge(ec=2, it=2, path=Path.ACTIVE, ip_auto=25), # Time challenge 2, iteration 2
        Challenge(ec=3, it=1, path=Path.ANTIMATTER), # Antimatter challenge 3, iteration 1
        EternityFarm(eternity_target="5"), # Eternity farm to get eternity points
        Challenge(ec=1, it=1, path=Path.ANTIMATTER), # Antimatter challenge 1, iteration 1
        Challenge(ec=1, it=2, path=Path.ANTIMATTER, ip_auto=10), # Antimatter challenge 1, iteration 2
        Farm(ep_target=28, path=Path.ACTIVE, ip_auto=25, ep_auto=1), # Farm for time dimensions again
        Challenge(ec=1, it=3, path=Path.INFINITY, ip_auto=10), # Infinity challenge 1, iteration 3
        Challenge(ec=2, it=3, path=Path.ANTIMATTER), # Antimatter challenge 2, iteration 3
        Farm(ep_target=33, path=Path.ACTIVE, ip_auto=100, ep_auto=1), # Farm for time dimensions
        Challenge(ec=3, it=2, path=Path.ANTIMATTER, ip_auto=25), # Antimatter challenge 3, iteration 2
        Challenge(ec=1, it=4, path=Path.INFINITY), # Infinity challenge 1, iteration 4
        Challenge(ec=3, it=3, path=Path.ANTIMATTER), # Antimatter challenge 3, iteration 3
        Challenge(ec=2, it=4, path=Path.ANTIMATTER), # Antimatter challenge 2, iteration 4
        Challenge(ec=2, it=5, path=Path.ACTIVE), # Time challenge 2, iteration 5
        Challenge(ec=4, it=1, path=Path.TIME), # Time challenge 4, iteration 1
        Challenge(ec=5, it=1, path=Path.TIME), # Time challenge 5, iteration 1
        Challenge(ec=6, it=1, path=str(Path.ACTIVE)), # Active challenge 6, iteration 1
        Challenge(ec=3, it=4, path=Path.ACTIVE), # Antimatter challenge 3, iteration 4
        Challenge(ec=3, it=5, path=Path.ACTIVE, ip_auto=1), # Time challenge 3, iteration 5
        # Time dimension challenges
        
        Challenge(ec=4, it=2, path=Path.TIME), # Time challenge 4, iteration 2
        Challenge(ec=4, it=3, path=Path.TIME), # Time challenge 4, iteration 3
        Farm(ep_target=40, path=Path.ACTIVE,  ip_auto=100, ep_auto=1), # Farm for time dimensions
        
        Challenge(ec=5, it=2, path=Path.TIME, ip_auto=100), # Time challenge 5, iteration 2
        Challenge(ec=5, it=3, path=Path.TIME), # Time challenge 5, iteration 3
        Challenge(ec=5, it=4, path=Path.TIME), # Time challenge 5, iteration 4
        Challenge(ec=5, it=5, path=Path.TIME), # Time challenge 5, iteration 5
        Challenge(ec=4, it=4, path=Path.TIME), # Time challenge 4, iteration 4
        Challenge(ec=1, it=5, path=Path.INFINITY), # Infinity challenge 1, iteration 5
        Farm(ep_target=70, ip_auto=100, path=Path.TIME, ep_auto=1), # Farm for time dimensions

        # Active dimension challenges
        Challenge(ec=6, it=2, path=str(Path.ACTIVE) + " 181"), # Active challenge 6, iteration 2
        Challenge(ec=6, it=3, path=str(Path.ACTIVE) + " 181"), # Active challenge 6, iteration 3
        Challenge(ec=6, it=4, path=str(Path.ACTIVE) + " 181"), # Active challenge 6, iteration 4
        Challenge(ec=6, it=5, path=str(Path.ACTIVE) + " 181"), # Active challenge 6, iteration 5

        # More Time dimension challenges
        Challenge(ec=7, it=1, path=Path.TIME), # Time challenge 7, iteration 1
        Challenge(ec=7, it=2, path=Path.TIME), # Time challenge 7, iteration 2
        Challenge(ec=7, it=3, path=Path.TIME), # Time challenge 7, iteration 3
        Challenge(ec=7, it=4, path=Path.TIME, ip_auto=10), # Time challenge 7, iteration 4
        Challenge(ec=8, it=1, path=Path.TIME), # Time challenge 8, iteration 1
        Challenge(ec=8, it=2, path=Path.TIME), # Time challenge 8, iteration 2
        Challenge(ec=8, it=3, path=Path.TIME), # Time challenge 8, iteration 3
        
        # More Active dimension challenges
        Challenge(ec=9, it=1, path=str(Path.ACTIVE) + " 181"), # Active challenge 9, iteration 1
        Challenge(ec=9, it=2, path=str(Path.ACTIVE) + " 181"), # Active challenge 9, iteration 2
        Challenge(ec=9, it=3, path=str(Path.ACTIVE) + " 181"), # Active challenge 9, iteration 3
        Challenge(ec=9, it=4, path=str(Path.ACTIVE) + " 181"), # Active challenge 9, iteration 4
        Challenge(ec=9, it=5, path=str(Path.ACTIVE) + " 181"), # Active challenge 9, iteration 5

        # Challenge 10 and farming with specific pathing
        Challenge(ec=10, it=1, path=str(Path.ACTIVE)+ " 181"), # Active challenge 10, iteration 1
        Farm(ep_target=270, ip_auto=1000, path=str(Path.ACTIVE) + " 181 193 191 212 214 211", ep_auto=10), # Farm with specific active path
        Challenge(ec=10, it=2, path=str(Path.ANTIMATTER) + " 181 193 191 212 214 211"), # Antimatter challenge 10, iteration 2, specific path
        Challenge(ec=10, it=3, path=str(Path.ANTIMATTER) + " 181 193 191 212 214 211"), # Antimatter challenge 10, iteration 3, specific path
        Farm(ep_target=400, ip_auto=1000, path=str(Path.ACTIVE) + " 181 193 191 212 214 211, 224, 232", ep_auto=10), # Farm with expanded active path
        Challenge(ec=10, it=4, path=str(Path.ANTIMATTER) + " 181 193 191 212 214 211, 224, 232"), # Antimatter challenge 10, iteration 4, expanded path
        Farm(ep_target=500, ip_auto=1000, path=str(Path.ACTIVE) + " 181 193 191 212 214 211 224 232", ep_auto=10),# Farm with full active path
        Challenge(ec=8, it=4, path=str(Path.TIME) + " 181 193 191 212 214 211 224 232"), # Time challenge 8, iteration 4, full path
        Challenge(ec=4, it=4, path=str(Path.TIME) + " 181"), # Time challenge 4, iteration 4, specific path
        Challenge(ec=8, it=5, path=str(Path.TIME) + " 181 193 191 212 214 211 224 232"), # Time challenge 8, iteration 5, full path
        Challenge(ec=7, it=5, path=str(Path.TIME) + " 181 193 191 212 214 211 224 232"), # Time challenge 7, iteration 5, full path
        Farm(ep_target=600, ip_auto=1000, path="11-61 62 time 111 active 151-214 72 82 92 102 224 232 222", ep_auto=15), # Farm with long path
        Farm(ep_target=900, ip_auto=1000, path="11-61 62 time 111 active 151-214 72 82 92 102 224 232 222", ep_auto=15), # Farm with long path
        
        # Challenge 11
        Challenge(ec=11, it=1, path="11-61 62 antimatter 111 idle 151-214 222 223 225 231 233"), # Challenge 11, iteration 1, long path
        Challenge(ec=11, it=2, path="11-61 62 antimatter 111 idle 151-214 222 223 225 231 233"), # Challenge 11, iteration 2, long path
        Challenge(ec=11, it=3, path="11-61 62 antimatter 111 idle 151-214 222 223 225 231 233"), # Challenge 11, iteration 3, long path
        Challenge(ec=11, it=4, path="11-61 62 antimatter 111 idle 151-214 222 223 225 231 233"), # Challenge 11, iteration 4, long path
        
        # Challenge 12
        Challenge(ec=12, it=1, path="11-61 62 time 111 idle 151-214 228 234 224 232 222 192"), # Challenge 12, iteration 1, long path
        Challenge(ec=12, it=2, path="11-61 62 time 111 idle 151-214 228 234 224 232 222 192"), # Challenge 12, iteration 2, long path
        Challenge(ec=12, it=3, path="11-61 62 time 111 idle 151-214 228 234 224 232 222 192"), # Challenge 12, iteration 3, long path
        Challenge(ec=12, it=4, path="11-61 62 time 111 idle 151-214 228 234 224 232 222 192"), # Challenge 12, iteration 4, long path
        
        # Final challenges and farming
        Challenge(ec=10, it=5, path=str(Path.ANTIMATTER)+" 181 193 191 212 214 211 224 232"), # Antimatter challenge 10, iteration 5, full path
        Challenge(ec=12, it=5, path="11-61 62 time 111 idle 151-214 228 234 224 232 222 192"), # Challenge 12, iteration 5, long path
        Inline(command="wait ec12 completions >= 5"),
        Farm(ep_target=1200, ip_auto=1000, path="11-61 62 time 111 active 151-214 72 82 92 102 dark", ep_auto=20), # Farm with very long path
        Challenge(ec=11, it=5, path="11-61 62 antimatter 111 idle 151-214 222 223 225 231 233"), # Challenge 11, iteration 5, long path
        Inline(command="wait ec11 completions >= 5"),
        Farm(ep_target=1500, ip_auto=1000, path="11-61 62 time 111 active 151-214 72 82 92 102 dark", ep_auto=100), # Farm with very long path
        FinalCommand(), # Final command to finish the run
    ]

    with open("challenges.dsl", 'w') as f:
        c = Class()
        c.write_instructions(f, instructions)
    with open("challenges.dsl", "r") as f:
        cont = str("".join(f.read()))
        print(len(cont))
    print("Instructions written to 'challenges.dsl'.")


if __name__ == "__main__":
    main()