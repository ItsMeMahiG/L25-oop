class vehicle :
    def __init__(self, ms, ml):
        self.ms=ms
        self.ml=ml
modelX= vehicle(240, 18)

print("model max speed : ",modelX.ms)
print("model mileage : ",modelX.ml)


modely= vehicle(300, 25)

print("model max speed : ",modely.ms)
print("model mileage : ",modely.ml)