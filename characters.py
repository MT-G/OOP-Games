import requests
import random
from bs4 import BeautifulSoup

class WonderlandMember:
    """
    Creates a character of Wonderland
    """

    def __init__(self, name: str, species: str, fantastic: bool = False):
        
        self.name = name
        self.species = species
        self.fantastic = fantastic
        
    @classmethod
    def hero(cls) -> "WonderlandMember":
        """Create main character

        Returns:
            class: class object
        """
        return cls("Alice", "human", True)
    
    @property
    def mood(self) -> str:
        if (self.species == "human") and (self.fantastic == True):
            return "angry"
        elif (self.species == "human") and (self.fantastic == False):
            return "whimsical"
        else:
            return "mysterious"

    @property 
    def interpretation(self):
        print("@property class method called")
        return self._interpretation 

    @interpretation.setter
    def interpretation(self,value):
        print("@interpretation.setter class method called")
        self._interpretation = value
    

    @staticmethod
    def get_quotes(url):
        """Get all the quotes of a webpage and return a list

        Args:
            url ([type]): webpage 

        Returns:
            list: list of quotes in the webpage
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        quotes = []
        for row in soup.find_all("div", attrs={"class": "quoteText"}):
            quote = row.text.split("―\n")[0]
            quotes.append(quote)
        return quotes

    @staticmethod
    def print_random_quote(quotes):
        n = random.randrange(len(quotes))
        print(quotes[n])


    def __repr__(self) -> str:
        """Representation function for the intances of the class

        Returns:
            str: class intances
        """
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"species='{self.species}', fanstatic='{self.fantastic}')"
        )

class StrangeAnimal(WonderlandMember):
    """Creates fantastic animals in Wonderland 

    Args:
        WonderlandMember (class): creates generic Wonderland member
    """

    def __init__(
        self,
        name: str,
        species: str,
        artefact: str,
        fantastic: bool = True
    ):
        super().__init__(name, species, fantastic)
        self.artefact = artefact

    @classmethod
    def white_rabbit(cls) -> "StrangeAnimal":
        
        return cls("White Rabbit", "animal", "clock")


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"species='{self.species}', artefact='{self.artefact}'"
        )


if __name__ == "__main__":
    mad_hat = WonderlandMember("Mad Hat", "something")
    alice = WonderlandMember.hero()
    url = "https://www.goodreads.com/work/quotes/2933712-alice-in-wonderland"
    quotes = alice.get_quotes(url)
    alice.print_random_quote(quotes)
    cat = WonderlandMember("Cheshire Cat", "animal")
    queen = WonderlandMember("Queen of Hearth", "human")
    print(f"{alice.name} is {alice.mood}")
    print()
    print(f"{cat.name} is {cat.mood}")
    print()
    print(f"{queen.name} is {queen.mood}")
    caterpillar = WonderlandMember("Caterpillar", "animal", "wise adult")
    print(f'The {caterpillar.name} is an {caterpillar.species} that represents a {caterpillar.interpretation}')
    print("="*70)
    caterpillar.interpretation = 'Hippy hookah smoker'
    print(f"Caterpillar interpretation is: {caterpillar.interpretation}")
    print("="*70)
    WonderlandMember.interpretation = 'teacher'
    print(f"Caterpillar interpretation is: a {WonderlandMember.interpretation}")
    rabbit = StrangeAnimal.white_rabbit()
    print(rabbit)
    print(f"The {rabbit.name}'s is {rabbit.mood}")