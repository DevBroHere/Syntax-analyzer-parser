#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By: Cezary Bujak
# Created Date: 19-06-2022
# Python version ='3.9'
# ---------------------------------------------------------------------------
"""Syntactic analyzer LL(1) implementing a generative dissection algorithm descending one symbol
advance by one symbol to the following grammar
S ∷= W ; S
W ∷= PW’
W’ ∷= OW | ε
P ∷= R | (W)
R ∷= LR’
R' ∷= .L | ε
L ∷= CL’
L' ∷= L | ε
C ∷= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
O ∷= * |∶ | + | - | ˆ
"""


class Parser:
    """
        The class used to construct the LL(1) syntactic analyzer
        which uses generational dissection descending one symbol in advance.

        ...

        Attributes
        ----------
        user_input : str
            Arithmetic expression entered by the user.
        stack : list
            list of symbols of the arithmetic expression entered by the user
        Next : str
            variable storing the current character waiting to be loaded
        index : int
            variable storing the current index of the symbol to be loaded
        output : int
            variable storing the result of the syntax analyzer operation

        Methods
        -------
        read_symbol(self)
            Method is responsible for reading the symbol
        raise_error(self)
            Method is responsible for pointing out the error in the string and informing you of the error
        start(self)
            The method starts the syntax analyzer and is responsible for informing the
            successful or erroneous completion
        state_L(self)
            Implementation of the syntax diagram of the production of L
        state_W(self)
            Implementation of the syntax diagram of production W
        state_S(self)
            Implementation of the syntax diagram of production S
        """

    def __init__(self, user_input):
        """
        Parameters
        ----------
        user_input : str
            Arithmetic expression entered by the user.
        """

        self.user_input = user_input
        self.stack = [i for i in user_input]
        if self.stack:
            self.Next = self.stack.pop(0)
        else:
            self.Next = None
        self.index = 0
        self.output = 0

    def read_symbol(self):
        """ Loads a symbol. If the stack is not empty then another symbol is taken from it with simultaneous
        removal. Otherwise, None is set as the actual symbol.
        """
        if self.stack:
            self.Next = self.stack.pop(0)
            self.index += 1
        else:
            self.Next = None

    def raise_error(self):
        """ Displays the loaded string along with an indication of which symbol caused the error. Then, depending on
        the value of the self.output variable, it displays the corresponding error message.
        """

        print("-------------------------------")
        print(self.user_input)
        print("".join([" " for _ in range(0, self.index)]) + "^")
        print("State", self.output)
        if self.output == -1:
            print("Syntax error: Symbol", self.Next, "is not a digit from 0 to 9")
        elif self.output == -2:
            print("Syntax error: Symbol", self.Next, "is not a symbol ')'")
        elif self.output == -3:
            print("Syntax error: Symbol", self.Next, "is not a symbol '('")
        elif self.output == -4:
            print("Syntax error: Symbol", self.Next, "is not a symbol ';'")
        elif self.output == -5:
            print("Syntax error: Symbol", self.Next, "is not a digit from 0 to 9 or the symbol '('")

    def start(self):
        """ Starts the syntax analyzer by running the output S.
        The value of the self.output variable indicates that the program completed the operation successfully,
        otherwise the the program reports a failure and runs the self.raise_error() method.
        """

        self.state_S()
        if self.output == 0:
            print("State", self.output)
            print("The program completed successfully")
        else:
            print("Syntax error: program with failure terminated")
            self.raise_error()

    def state_L(self):
        """ Implementation of the syntax diagram of L production.
        """

        # If the current symbol is in the set of digits 0-9 then read the symbol.
        # This is an abbreviated implementation of the alternative in the syntax diagram.
        # Otherwise, assign error code -1 to the variable self.output.
        if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.read_symbol()
            # If the current symbol is in the set of first production symbols L
            # (these are digits in the range 0-9) then read the symbol.
            # Otherwise, continue the program operation
            if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.state_L()
            else:
                pass
        else:
            # If the error code has not yet been assigned then assign the error code to the self.output variable.
            # Otherwise, continue the program.
            if self.output == 0:
                self.output = -1
            else:
                pass

    def state_W(self):
        """ Implementation of the syntax diagram of W production.
        """

        # If the current symbol is in the set of digits 0-9 then read the symbol.
        # This is an abbreviated implementation of the alternative in the syntax diagram.
        if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.read_symbol()
            # If the current symbol is in the set of first production symbols L
            # (these are digits in the range 0-9) then read the symbol.
            # Otherwise, continue the program operation
            if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.state_L()
            else:
                pass
            # If the current symbol is "." then read the symbol.
            # Otherwise, continue the program operation.
            if self.Next == ".":
                self.read_symbol()
                self.state_L()
            else:
                pass
            # If the current symbol is in the set of operators then read the symbol.
            # Otherwise, continue the program.
            if self.Next in ["*", ":", "+", "-", "^"]:
                self.read_symbol()
                self.state_W()
            else:
                pass
        # If the current symbol is "(" then read the symbol.
        elif self.Next == "(":
            self.read_symbol()
            self.state_W()
            # If the current symbol is ")" then read the symbol.
            # Otherwise, assign error code -2 to the variable self.output.
            if self.Next == ")":
                self.read_symbol()
                # If the current symbol is in the set of operators then read the symbol.
                # Otherwise, continue the program.
                if self.Next in ["*", ":", "+", "-", "^"]:
                    self.read_symbol()
                    self.state_W()
                else:
                    pass
            else:
                # If the error code has not yet been assigned then assign the error code to the self.output variable.
                # Otherwise, continue the program.
                if self.output == 0:
                    self.output = -2
                else:
                    pass
        else:
            # If the error code has not yet been assigned then assign the error code to the self.output variable.
            # Otherwise, continue the program.
            if self.output == 0:
                self.output = -3
            else:
                pass

    def state_S(self):
        """ An implementation of the syntax diagram of S production.
        """

        # If the current symbol is in the set of digits 0-9 then read the symbol.
        # This is an abbreviated implementation of the alternative in the syntax diagram.
        if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.read_symbol()
            # If the current symbol is in the set of first production symbols L
            # (these are digits in the range 0-9) then read the symbol.
            # Otherwise, continue the program operation
            if self.Next in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.state_L()
            else:
                pass
            # If the current symbol is "." then read the symbol.
            # Otherwise, continue the program operation.
            if self.Next == ".":
                self.read_symbol()
                self.state_L()
            else:
                pass
            # If the current symbol is in the set of operators then read the symbol.
            # Otherwise, continue the program.
            if self.Next in ["*", ":", "+", "-", "^"]:
                self.read_symbol()
                self.state_W()
            else:
                pass
            # If the current symbol is "." then read the symbol.
            # Otherwise, continue the program operation.
            if self.Next == ";":
                self.read_symbol()
                if self.Next:
                    self.state_S()
                else:
                    return
            else:
                # If the error code has not been assigned yet then assign the error code to the self.output variable.
                # Otherwise, assign error code -4 to variable self.output.
                if self.output == 0:
                    self.output = -4
                else:
                    pass
        # If the current symbol is "(" then read the symbol.
        elif self.Next == "(":
            self.read_symbol()
            self.state_W()
            # If the current symbol is ")" then read the symbol.
            # Otherwise, assign error code -2 to the variable self.output.
            if self.Next == ")":
                self.read_symbol()
                # If the current symbol is in the set of operators then read the symbol.
                # Otherwise, continue the program.
                if self.Next in ["*", ":", "+", "-", "^"]:
                    self.read_symbol()
                    self.state_W()
                else:
                    pass
                # If the current symbol is "." then read the symbol.
                # Otherwise, continue the program operation.
                if self.Next == ";":
                    self.read_symbol()
                    if self.Next:
                        self.state_S()
                    else:
                        return
                else:
                    # If the error code has not yet been assigned then assign the error code to the
                    # self.output variable. Otherwise, continue the program.
                    if self.output == 0:
                        self.output = -4
                    else:
                        pass
            else:
                # If the error code has not yet been assigned then assign the error code to the self.output variable.
                # Otherwise, continue the program.
                if self.output == 0:
                    self.output = -2
                else:
                    pass
        # If the current symbol has not been matched with any of the production terminal symbols then
        # Assign error code -2 to the variable self.output.
        else:
            # If the error code has not yet been assigned then assign the error code to the self.output variable.
            # Otherwise, continue the program.
            if self.output == 0:
                self.output = -5
            else:
                pass


def main():
    # Main program - IMPORTANT: The string must end with a semicolon character.
    while True:
        user_input = input("Enter an arithmetic expression: ")
        parser = Parser(user_input)
        parser.start()


# Python program to use
# main for function call.
if __name__ == "__main__":
    main()
