import javax.swing.*;

public class swingApp {
    swingApp()
    {
        JFrame F = new JFrame();

        JLabel FirstName = new JLabel("First Name");
        FirstName.setBounds(20, 50, 80, 20);

        JLabel LastName = new JLabel("Last Name");
        LastName.setBounds(20, 80, 80, 20);

        JLabel dob = new JLabel("Date of Birth");
        dob.setBounds(20, 110, 80, 20);

        JTextField FirstNameTF = new JTextField();
        FirstNameTF.setBounds(150, 50, 120, 20);

        JTextField lastNameTF = new JTextField();
        lastNameTF.setBounds(150, 80, 120, 20);

        JTextField dobTF = new JTextField();
        dobTF.setBounds(150, 110, 120, 20);

        JButton sbmt = new JButton("Submit");
        sbmt.setBounds(20,160,100,30);

        JButton reset = new JButton("reset");
        reset.setBounds(140, 160, 100, 30);

        JButton exit = new JButton("Exit");
        exit.setBounds(75, 210, 100, 30);
        exit.addActionListener(e -> System.exit(0));

        F.add(FirstName);
        F.add(LastName);
        F.add(dob);
        F.add(FirstNameTF);
        F.add(lastNameTF);
        F.add(dobTF);
        F.add(sbmt);
        F.add(reset);
        F.add(exit);
        
        F.setSize(300,300);
        F.setLayout(null);
        F.setVisible(true);
    }



    public static void main(String[] args) {
        new swingApp();
    }
}