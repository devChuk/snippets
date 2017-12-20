#include <iostream>
using namespace std;

struct CNode {
    int value;
    CNode* next;
};


CNode* what(CNode* aNode, int item) {

    CNode* previous = aNode;
    CNode* current = previous->next;

    while (current->value < item || previous->value > item) {
        previous = previous->next;
        current = current->next;
        if (current == aNode) {
            break;
        }
    }
    CNode* thing = new CNode;
    thing->value = item;
    thing->next = current;
    previous->next = thing;
    //cout << "thing->value" << endl;
    return thing;
}

int main() {
    CNode* a = new CNode;
    CNode* b = new CNode;
    CNode* c = new CNode;
    CNode* d = new CNode;
    CNode* e = new CNode;

    a->value = 0;
    b->value = 1;
    c->value = 2;
    d->value = 3;
    e->value = 7;

    a->next = b;
    b->next = c;
    c->next = d;
    d->next = e;
    e->next = a;

    // CNode* temp = a->next;
    // while (temp != a) {
    //     cout << temp->value << endl;
    //     temp = temp->next;
    // }

    CNode* fun = what(a, 8);
    CNode* run = fun;
    cout << run->value << endl;
    run = run->next;
    while (run != fun) {
        cout << run->value << endl;
        run = run->next;
    }
}
