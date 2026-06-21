class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minhand = minutes * 6.0
        hr = hour % 12
        hrhand = (hr * 30.0 ) + (minutes *0.5)
        angle = abs(minhand - hrhand)
        return min(angle,360.0-angle)

