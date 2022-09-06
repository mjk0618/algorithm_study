def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mag_dict = {}
    for s in magazine:
        if s not in mag_dict:
            mag_dict.update(s = 1)
        else: mag_dict[s] += 1
    
    for s in ransomNote:
        if s in mag_dict and mag_dict[s] > 0:
            mag_dict[s] -= 1
        else:
            return False
        