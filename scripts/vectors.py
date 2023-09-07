import math

class Vector2D(object):
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    @property
    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def scalar_product(self, scalar = 1):
        return (self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return ("({}, {})".format(self.x, self.y))
        
    @classmethod
    def sum(cls, v1, v2):
        return cls(v1.x + v2.x , v1.y + v2.y)
    
    @classmethod
    def subtract(cls, v1, v2):
        return cls(v1.x - v2.x , v1.y - v2.y)
        
    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y
    
    @classmethod
    def distance(cls, v1, v2):
        return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)
    
    def extend_to_3D(self, z = 0):
        return Vector3D(self.x, self.y, z)
        
        
        
class Vector3D(Vector2D):
    
    def __init__(self, x = 1, y = 1, z = 1):
        super().__init__(x, y)
        self.z = z
    
    def __str__(self):
        return super().__str__()[:-1] + ", {})".format(self.z)
        
    @property
    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        
    def scalar_product(self, scalar = 1):
        return super().scalar_product(scalar) + (self.z * scalar, )
    
    @classmethod
    def sum(cls, v1, v2):
        return cls(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    
    @classmethod
    def subtract(cls, v1, v2):
        return cls(v1.x - v2.x , v1.y - v2.y, v1.z - v2.z)
    
    @staticmethod
    def dot_product(v1, v2):
        return super().dot_product(v1, v2) + (v1.z * v2.z) 
    
    @classmethod
    def distance(cls, v1, v2):
        return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2)
    
    @classmethod
    def zero(cls):
        return cls(0,0,0)
    
    @classmethod
    def horizontal(cls):
        return cls(1,0,0)
        
    @classmethod
    def vertical(cls):
        return cls(0,1,0)
    
    @classmethod
    def forward(cls):
        return cls(0,0,1)
    