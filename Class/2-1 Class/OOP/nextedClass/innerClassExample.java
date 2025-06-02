package nextedClass;

import javax.swing.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

class NonInnerClassExample extends JFrame {

    private String originalTitle = "Original Title";

    public NonInnerClassExample() {
        setTitle(originalTitle);
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 외부 클래스 객체를 명시적으로 전달
        addMouseListener(new ExternalMouseEventHandler(this));

        setVisible(true);
    }

    // getter, setter 필요
    public void updateTitle(String title) { setTitle(title); }
    public String getOriginalTitle() { return originalTitle; }
}

class ExternalMouseEventHandler implements MouseListener {
    private NonInnerClassExample frame;

    public ExternalMouseEventHandler(NonInnerClassExample frame) { this.frame = frame;}

    public void mouseEntered(MouseEvent e) { frame.updateTitle("Mouse on"); }
    public void mouseExited(MouseEvent e) { frame.updateTitle(frame.getOriginalTitle()); }

    public void mouseClicked(MouseEvent e) { frame.updateTitle("Mouse clicked"); }
    public void mousePressed(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
}



public class innerClassExample {
    public static void main(String[] args) {
        new NonInnerClassExample();
    }
}
