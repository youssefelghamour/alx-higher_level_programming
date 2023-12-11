#!/usr/bin/python3
""" Module for Base class """
import json
import os
import csv


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        lst = []
        if list_objs is not None:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)  # Rectangle(1,1)
        elif cls.__name__ == "Square":
            new = cls(1)  # Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a json file """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        lst = []
        with open(filename, 'r', encoding="utf-8") as f:
            json_string = f.read()

        lst = cls.from_json_string(json_string)
        lst = [cls.create(**lst[i]) for i in range(len(lst))]
        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves a list of object to a CSV file """
        filename = "{}.csv".format(cls.__name__)

        lst = []
        if list_objs is not None:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    lst.append([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:  # cls.__name__ == "Square"
                    lst.append([obj.id, obj.size, obj.x, obj.y])

        with open(filename, 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(lst)

    @classmethod
    def load_from_file_csv(cls):
        """ loads and deserializes a CSV string from a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        list_objs = []
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)

            attr = []
            for row in reader:
                row = [int(r) for r in row]
                if cls.__name__ == "Rectangle":
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:  # cls.__name__ == "Square"
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                list_objs.append(cls.create(**d))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares """
        import turtle
        from random import randrange

        for obj in list_rectangles + list_squares:
            drawer = turtle.Turtle()
            drawer.color((randrange(255), randrange(255), randrange(255)))
            drawer.pensize(1)
            drawer.penup()
            drawer.goto(obj.x, obj.y)
            drawer.pendown()
            drawer.begin_fill()
            drawer.pensize(10)

            for i in range(2):
                drawer.forward(obj.width)
                drawer.left(90)
                drawer.forward(obj.height)
                drawer.left(90)

            drawer.hideturtle()
            drawer.end_fill()

        turtle.Screen().exitonclick()
