from abc import ABC, abstractmethod


class ChickyController(ABC):
    """
    Abstract base class representing a controller for the Picky Chicky game.

    Attributes:
        _board: A Picky Chicky instance representing the game to
            send moves to.
    """

    def __init__(self, board):
        """
        Create a new controller for a Picky Chicky.

        Args:
            board: A Picky Chicky instance representing the Picky Chicky
                to send moves to.
        """
        self._board = board

    @property
    def board(self):
        """
        Return the TicTacToeBoard instance this controller interacts with.
        """
        return self._board

    @abstractmethod
    def move(self):
        """
        Make a valid move in the current board.
        """
        pass


class ArrowKeyController(ChickyController):
    """
    Text-based controller for tic-tac-toe that takes user input representing
    board coordinates.
    """

    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
