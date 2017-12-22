public class HelloWorld
{

    public static void printOne() {

        CNode previous = aNode;
        CNode current = previous.next;

        while (current.value < costOfItem || previous.value > costOfItem) {
            previous = previous.next;
            current = current.next;
            if (current == aNode) {
                break;
            }
        }
        CNode item = new CNode(costOfItem);
        item->value = costOfItem;
        item->next = current;
        previous->next = item;
        //cout << "item->value" << endl;
        return item;
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}