class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0

    def next(self):
        new_fib = Fib()
        if self.value == 0:
            new_fib.value = 1
            new_fib.previous = 0
            return new_fib
        elif self.value == 1 and self.previous < 1:
            self.value = 1
            self.previous = 1
        else:
            t = self.value
            self.value = self.value + self.previous
            self.previous = t
        return self

    def __repr__(self):
        return str(self.value)

class VendingMachine():
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, cost):
        self.product = product
        self.cost = cost
        self.num_in_stock = 0
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        #enough_in_stock = self.balance / self.num_in_stock
        if self.num_in_stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(self.balance)
        return 'Current balance: ${0}'.format(self.balance)

    def vend(self):
        if self.num_in_stock == 0:
            return 'Machine is out of stock.'
        if self.balance == 0:
            return 'You must deposit $10 more.' 
        elif self.balance < self.cost:
            return 'You must deposit ${0} more.'.format(10 - self.balance)
        else:
            self.num_in_stock -= 1
            self.balance -= self.cost
            if self.balance == 0:
                return 'Here is your {0}.'.format(self.product)
            else:
                temp_balance = self.balance
                self.balance = 0
                return 'Here is your {0} and ${1} change.'.format(self.product, temp_balance)

    def restock(self,quantity):
        self.num_in_stock = quantity
        return 'Current {0} stock: {1}'.format(self.product, self.num_in_stock)

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        lst = message.split()
        if hasattr(self.obj, lst[1]):
            return getattr(self.obj, lst[1])(*args)  
        else:
            return 'Thanks for asking, but I know not how to {0}.'.format(" ".join(lst[1:]))









