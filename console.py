#!/usr/bin/python3
"""Console class"""
import cmd

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
        return cmd.Cmd.emptyline(self)
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()