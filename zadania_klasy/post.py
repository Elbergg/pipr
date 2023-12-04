class Package:
    def __init__(self, sender, recipient, size, weigth):
        self._sender = sender
        self._recipient = recipient
        if min(size) <= 0:
            raise ValueError
        self._size = size
        if weigth <= 0:
            raise ValueError
        self._weigth = weigth
        
    def sender(self):
        return self._sender
       
    def recipient(self):
        return self._recipient
    
    def size(self):
        return self._size
    
    def weigth(self):
        return self._weigth
    
    def smallest_size_parameter(self):
        return min(self._size)
    
    def biggest_size_parameter(self):
        return max(self._size)
    
    def __str__(self) -> str:
        return f'The package was sent by {self._sender} to {self._recipient}. Its size is {self._size[0]} length, {self._size[1]} width, and {self._size[2]} height. It weighs {self._weigth} kg.'