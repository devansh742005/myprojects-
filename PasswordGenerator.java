import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class PasswordGenerator implements ActionListener {

    JFrame frame;
    JTextField textfield;
    JButton[] characterButtons;
    JButton[] lengthButtons;
    JTextField lengthField;
    JPanel panel;
    Font myFont = new Font("Papyrus", Font.BOLD, 30);
    Random random = new Random();
    String D = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$";
    String E = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String V = "abcdefghijklmnopqrstuvwxyz";
    String A = "0123456789@$";
    String selectedCharacterSet = "";

    PasswordGenerator() {
        frame = new JFrame("Password Generator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setLayout(null);

        textfield = new JTextField();
        textfield.setBounds(50, 25, 400, 50);
        textfield.setFont(myFont);
        textfield.setEditable(false);



        lengthField = new JTextField();
        lengthField.setBounds(50, 80, 100, 50);
        lengthField.setFont(myFont);
        lengthField.setHorizontalAlignment(JTextField.CENTER);

        panel = new JPanel();
        panel.setBounds(50, 150, 450, 150);
        panel.setLayout(new GridLayout(2, 2, 2, 2)); 

        String[] buttonTexts = {"@", "&", "!", "*"};
        characterButtons = new JButton[4];
        for (int i = 0; i < 4; i++) {
            characterButtons[i] = new JButton(buttonTexts[i]);
            characterButtons[i].addActionListener(this);
            characterButtons[i].setFont(myFont);
            characterButtons[i].setFocusable(false);
            panel.add(characterButtons[i]);
        }

        lengthButtons = new JButton[10]; // Create buttons for numbers 0-9
        for (int i = 0; i < 10; i++) {
            lengthButtons[i] = new JButton(String.valueOf(i));
            lengthButtons[i].addActionListener(this);
            lengthButtons[i].setFont(myFont);
            lengthButtons[i].setFocusable(false);
            panel.add(lengthButtons[i]);
        }

        frame.add(panel);
        frame.add(textfield);
        frame.add(lengthField);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 4; i++) {
            if (e.getSource() == characterButtons[i]) {
                selectCharacterSet(i + 1);
                break;
            } else {
                for (int j = 0; j < 10; j++) {
                    if (e.getSource() == lengthButtons[j]) {
                        lengthField.setText(lengthButtons[j].getText());
                        generatePassword();
                        break;
                    }
                }
            }
        }
    }

    void selectCharacterSet(int choice) {
        switch (choice) {
            case 1:
                selectedCharacterSet = D;
                break;
            case 2:
                selectedCharacterSet = E;
                break;
            case 3:
                selectedCharacterSet = V;
                break;
            case 4:
                selectedCharacterSet = A;
                break;
            default:
                selectedCharacterSet = D;
                break;
        }
        generatePassword();
    }

    void generatePassword() {
        int length = Integer.parseInt(lengthField.getText());
        StringBuilder generatedPassword = new StringBuilder();
        if (!selectedCharacterSet.isEmpty()) {
            for (int i = 0; i < length; i++) {
                int randomIndex = random.nextInt(selectedCharacterSet.length());
                generatedPassword.append(selectedCharacterSet.charAt(randomIndex));
            }
        }
        textfield.setText(generatedPassword.toString());
    }

    public static void main(String[] args) {
        PasswordGenerator passwordGenerator = new PasswordGenerator();
    }
}
