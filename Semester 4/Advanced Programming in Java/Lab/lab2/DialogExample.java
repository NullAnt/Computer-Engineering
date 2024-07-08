import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class DialogExample {
    private static Dialog d;
    DialogExample() {
        JFrame f= new JFrame("Parent Frame");
        f.add(new Label("Parent of dialog box"));
        f.setSize(300, 300);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        d = new Dialog(f , "Dialog Example", true);
        d.setLayout( new FlowLayout() );

        Button b = new Button ("OK");

        b.addActionListener ( new ActionListener()
        {
            public void actionPerformed( ActionEvent e )
            {
                DialogExample.d.setVisible(false);
            }
        });

        d.add( new Label ("Click button to continue."));
        d.add(b);
        d.setSize(300,300);
        d.setVisible(true);
    }
    public static void main(String args[])
    {
        new DialogExample();
    }
}