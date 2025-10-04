from abc import ABC, abstractmethod

#abstract base class
class Shape(ABC):
    @abstractmethod
    def draw(self,*args, **kwargs) -> int:
        """Render the shape and return value"""
        pass

#concrete classes
class Circle(Shape):
    def draw(self,r: int) -> int:
        area=int(22/7*r*r)
        return area

class Square(Shape):
    def draw(self,length : int) -> int:
        area= length*length
        return area

class Triangle(Shape):
    def draw(self,base :int ,height:int) -> int:
        area=int(0.5*base*height)
        return area
    

# factory class
class DrawingProcessorFactory:
    _shapes = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle
    }

    @classmethod
    def register_shape(cls, shape_name: str, shape_cls: Shape) -> None:
        """Register a new shape class with the factory"""
        if not issubclass(shape_cls, Shape):
            raise ValueError(f"Shape class must inherit from Shape")
        cls._shapes[shape_name] = shape_cls
        
    @classmethod
    def create_shape(cls, shape_name: str, *args) -> Shape:
        shape_cls = cls._shapes.get(shape_name)
        if shape_cls is None:
            return ValueError("Shape '{shape_name}' not found")
        shape_instance = shape_cls()
        return shape_instance.draw(*args)
    

if __name__ == "__main__":
    factory = DrawingProcessorFactory

    circle = factory.create_shape("circle", 4)
    print("Circle:", circle)

    square = factory.create_shape("square", 4)
    print("Square:", square)

    triangle = factory.create_shape("triangle", 4, 5)
    print("Triangle:", triangle)
    

