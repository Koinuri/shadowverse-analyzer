#include<string>

using std::string;

class Card {
    public:
        string Name;
        int Cost;
        string Text;
        bool Earthrite;
        string Trait;
        int Class_Type;

        void ReadBasicInformation(string txt) {}
        void Destroy() {}
        void Banish() {}
        void HandAuraCondition() {}
        void HandAuraEffect() {}
};

class Follower: Card {
    public:
        string EvoText;
        int Attack;
        int Defense;
        int EvoAttack;
        int EvoDefense;
        int Status;
        
        void Fanfare() {}
        void Clash() {}
        bool AuraCondition() { return false; }
        void AuraEffect() {}
        void LastWord() {}
};

class Spell: Card {
    public:
        void Fanfare() {}
};

class Amulet: Card {
    public:
        int Countdown;

        void Fanfare() {}
        bool AuraCondition() {}
        void AuraEffect() {}
        void LastWord() {}
};

class Effect: Card {
    public:
        bool AuraCondition() {}
        void AuraEffect() {}
};


