def display_hangman_Easy(tries):
    stages = [  """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / 
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |   
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    | 
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O
         |     
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    O
         |     
         |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    
         | 
         |   
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    
         |    
         | 
         |   
         |
        _|_
       |   |________
       |            |
       |____________|
        """
    ]
    return stages[tries]

def display_hangman_Normal(tries):
    stages = [  """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / 
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /| 
         |    |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    | 
         |    |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |    
         |    
         |
         |
        _|_
       |   |________
       |            |
       |____________|
         """
    ]
    return stages[tries]

def display_hangman_Hard(tries):
    stages = [  """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |   / \\
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |   /|\\
         |    |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |   [O]
         |    |
         |    |
         |
        _|_
       |   |________
       |            |
       |____________|
        """,
        """
         _____
         |    |
         |
         |    
         |    
         |
        _|_
       |   |________
       |            |
       |____________|
         """
    ]
    return stages[tries]