import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginForm extends JFrame {
    private JLabel titleLabel, usernameLabel, passwordLabel;
    private JTextField usernameField;

    private JPasswordField passwordField;
    private JButton loginButton;

    public LoginForm() {
        setTitle("Login Form");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 2, 5, 5));

        titleLabel = new JLabel("Login Form");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 18));
        add(titleLabel);

        usernameLabel = new JLabel("Username:");
        add(usernameLabel);

        usernameField = new JTextField();
        add(usernameField);

        passwordLabel = new JLabel("Password:");
        add(passwordLabel);

        passwordField = new JPasswordField();
        add(passwordField);

        loginButton = new JButton("Login");

        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = usernameField.getText();
                String password = new String(passwordField.getPassword());

                if (username.equals("admin") && password.equals("admin123")) {

                    JOptionPane.showMessageDialog(LoginForm.this,"Login Successful!");
                } else {
                JOptionPane.showMessageDialog(LoginForm.this,"Invalid Username or Password", "Error", JOptionPane.ERROR_MESSAGE);

                }
            }
        });

        add(loginButton);
        setVisible(true);
    }

    public static void main(String[] args) {
        new LoginForm();
    }
}