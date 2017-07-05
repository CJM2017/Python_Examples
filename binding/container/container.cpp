// Source: https://stackoverflow.com/questions/19198872/how-do-i-return-objects-from-a-c-function-with-ctypes
#include <vector>


class Item{
    public:
        Item(char* name,int id);
        char* getName();
    private:
        char* name;
        int id;
};

class Container {
    public:
        Container();
        Item* getItem(int id);
    private:
        std::vector<Item*> items;
};

Item::Item(char* name,int id) {
    this->name = name;
}

extern "C" {
    Container* Container_init() {return new Container();}
    Item* Container_getItem(Container* container,int id){return container->getItem(id);}
    char* Item_getName(Item* item) { return item->getName(); }
}