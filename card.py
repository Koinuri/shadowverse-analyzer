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
        
    @abstractmethod
    def HandAuraCondition(self):
        pass

    @abstractmethod
    def HandAuraEffect(self):
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
        for i in range(0, len(self.Owner.Hand)):
            if self.Owner.Hand[i] == self:
                self.Owner.Hand.pop(i)
        self.LastWord()

    def Banish():
        for i in range(0, len(self.Owner.Hand)):
            if self.Owner.Hand[i] == self:
                self.Owner.Hand.pop(i)

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
