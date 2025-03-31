class ItemBox {
    int numOfBoxes;
    void push() {numOfBoxes++;}
    void pop() {numOfBoxes--;}
}
class Foo {
    ItemBox box;
    Foo(ItemBox argBox) {box = argBox;}
}
class Pos {
    ItemBox box;
    Pos(ItemBox argBox) {box = argBox;}
}
public class Test1 {
    public static void main(String[] args) {
        ItemBox box = new ItemBox();
        Foo foo = new Foo(box);
        Pos pos = new Pos(box);
        foo.box.push();
        foo.box.push();
        pos.box.pop();
        pos.box.pop();
    }
}