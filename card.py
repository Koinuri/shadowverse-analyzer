from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self):
        self.Name = ""
        self.Cost = 0
        self.Description = ""
        self.Trait = ""
        self.Class = -1
        self.Owner = Player([])

    @abstractmethod
    def ReadBasicInformation(self, file_name):
        pass

    @abstractmethod
    def Destroy(self):
        pass

    @abstractmethod
    def Banish(self):
        pass
        
class Follower(Card):
    def __init__(self):
        super(Follower, self).__init__()
        self.EvoDescription = ""
        self.Attack = 0
        self.Defense = 0
        self.EvoAttack = 0
        self.EvoDefense = 0
        self.Status = -1

    def Destroy(self):
        self.Owner.Shadow += 1
        self.Owner.Board.remove(self)
        self.LastWord()

    def Banish():
        self.Owner.Board.remove(self)

    @abstractmethod
    def Fanfare():
        pass

    @abstractmethod
    def Clash():
        pass

    @abstractmethod
    def AuraCondition():
        pass

    @abstractmethod
    def AuraCondition():
        pass

    @abstractmethod
    def AuraEffect():
        pass

    @abstractmethod
    def LastWord():
        pass

class Spell(Card)
    def __init__(self):
        super(Spell, self).__init__()

    @abstractmethod
    def Fanfare():
        pass

class Amulet(Card):
    def __init__(self):
        self.Countdown = -1

    @abstractmethod
    def Fanfare():
        pass

    @abstractmethod
    def AuraCondition():
        pass

    @abstractmethod
    def AuraEffect():
        pass

    @abstractmethod
    def LastWord():
        pass
