#!/usr/local/bin/python3
"""
Console class
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Comand line class
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Exit the comandline
        """

        return True

    def do_quit(self, line):
        """
        Exit the comandline
        """

        return True

    def emptyline(self):
        """
        empty line
        """

        return False

    def do_create(self, line):
        """
        Creates new base model
        """

        if line == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """

        if line == "":
            print("** class name missing **")
        elif line.count("BaseModel") != 1:
            print("** class doesn't exist **")
        elif len(line.split(" ")) == 1:
            print("** instance id missing **")
        elif line.count(" ") == 1:
            key = line.replace(" ", ".")
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance of base id
        """

        if line == "":
            print("** class name missing **")
        elif line.count("BaseModel") != 1:
            print("** class doesn't exist **")
        elif len(line.split(" ")) == 1:
            print("** instance id missing **")
        elif line.count(" ") == 1:
            key = line.replace(" ", ".")
            all_objs = models.storage.all()
            if key in all_objs:
                models.storage._FileStorage__objects.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Returnd all string representation of existing objects
        """

        if line in ("BaseModel", "User") or len(line) == 0:
            all_objs = models.storage.all()
            i = 0
            print("[\"", end="")
            for key in all_objs.keys():
                if key.count(line) == 1 or len(line) == 0:
                    print(all_objs[key], end="")
                    i += 1
                    if i != len(all_objs):
                        print(", ", end="")
            print("\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        updates an instance of base id
        """

        if line == "":
            print("** class name missing **")
        elif line.count("BaseModel") != 1:
            print("** class doesn't exist **")
        elif len(line.split(" ")) == 1:
            print("** instance id missing **")
        elif line.count(" ") >= 3:
            key = line.split(" ")
            objKey = key[0] + "." + key[1]
            all_objs = models.storage.all()
            if objKey in all_objs:
                if key[2] not in ("1d", "created_at", "updated_at"):
                    all_objs[objKey].__dict__[key[2]] = key[3]\
                        .replace("\"", "").replace("\'", "")
                    models.storage.save()
            else:
                print("** no instance found **")
        elif line.count(" ") == 1:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
