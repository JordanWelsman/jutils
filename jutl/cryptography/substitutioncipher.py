# Module imports

# External class visibility
__all__ = ['SubstitutionCipher']


class SubstitutionCipher():
    """
    Class which acts as the
    base Cipher implementation.
    """
    def __init__(self, rotation: int = 0):
        "Initialization method."
        self.rotation = self._check_rotation(rotation)
    
    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.rotation != 0:
            print("s")
    

    def _check_rotation(self, rotation: int) -> int:
        """
        Checks if rotation is valid.
        """
        allowed_range = range(0, 27)

        if rotation in allowed_range:
            return rotation
        else:
            return 0


    def set_rotation(self, rotation: int = 0):
        """
        Sets the rotation
        after initialization.
        """
        self.rotation = self._check_rotation(rotation)

    
    def _encrypt(self, message: str):
        """
        Encrypts the passed message
        using the defined rotation.
        """
        __alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        __alpha_lower = "abcdefghijklmnopqrstuvwxyz"
        encrypted_message: str = ""
        
        for letter in message:
            if letter in __alpha_upper:
                encrypted_message += __alpha_upper[(__alpha_upper.find(letter) + self.rotation) % 26]
            elif letter in __alpha_lower:
                encrypted_message += __alpha_lower[(__alpha_lower.find(letter) + self.rotation) % 26]
            else:
                encrypted_message += letter

        return encrypted_message

