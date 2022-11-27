#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
"""Console class"""

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    """Comand line processor"""
    
    def do_EOF(self, line):
        """Exit the comandline"""
        
        return True
    
    def do_quit(self, line):
        """Exit the comandline"""
        
        return True
    
    def emptyline(self):
        return False
    
    def do_create(self, line):
        """Creates new base model"""
        if line == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if line == "":
            print("** class name missing **")
        elif line.count("BaseModel") != 1:
            print("** class doesn't exist **")
        elif len(line.split(" ")) == 1:
            print("** instance id missing **")
        elif line.count(" ") == 1:
            key = line.replace(" ", "." )
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Prints the string representation of an instance"""
        if line == "":
            print("** class name missing **")
        elif line.count("BaseModel") != 1:
            print("** class doesn't exist **")
        elif len(line.split(" ")) == 1:
            print("** instance id missing **")
        elif line.count(" ") == 1:
            key = line.replace(" ", "." )
            all_objs = storage.all()
            if key in all_objs:
                all_objs[key].delete()
            else:
                print("** no instance found **")
        else:
                print("** no instance found **")
    
    def do_all(self, line):
        """Prints the string representation of an instance"""
        if line in ("BaseModel") or len(line) == 0:
            all_objs = storage.all()
            lista = []
            for key in all_objs:
                lista.append(all_objs[key].to_dict())
            print(lista)
        else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()