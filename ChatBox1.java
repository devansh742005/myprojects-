import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import javax.swing.*;
import java.util.Random;

public class ChatBox1 extends JFrame implements ActionListener {

    private String[] urls = {
            "https://www.youtube.com/",
            "https://open.spotify.com/",
            "https://web.whatsapp.com/",
            "https://www.instagram.com/",
            "https://samvidha.iare.ac.in/index"
    };

    private String[] jokes = {
            "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else.",
            "Parallel lines have so much in common... It's a shame they'll never meet.",
            // ... (other jokes)
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
    };

    private Random random = new Random();
    private int jokeIndex = random.nextInt(jokes.length);

    private JLabel welcomeLabel;
    private JButton submitButton;
    private JComboBox<String> options;
    private String[] users = {"Devansh", "rex", "yash", "sujay", "IARE"};

    public ChatBox1() {
        setTitle("Chat Box");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        welcomeLabel = new JLabel("Hello! Who is using me?");
        add(welcomeLabel);

        submitButton = new JButton("Submit");
        submitButton.addActionListener(this);
        add(submitButton);

        JComboBox<String> options = new JComboBox<>(new String[]{"D2", "D9", "D4", "G6", "<>"});
        add(options);
options = new JComboBox<>(new String[]{"D2", "D9", "D4", "G6", "<>"});

        JComboBox<String> choices = new JComboBox<>(new String[]{"youtube", "spotify", "whatsapp", "iG", "IARE", "jokes"});
        add(choices);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            int choice = options.getSelectedIndex();
            String selectedUser = users[choice];

            String selectedOption = (String) options.getSelectedItem();

            if (selectedUser != null) {
                if (choice != 5) {
                    if (choice >= 0 && choice < urls.length && urls[choice] != null) {
                        openURL(urls[choice]);
                        JOptionPane.showMessageDialog(this, "Hello " + selectedUser + "! Redirecting to " + selectedOption);
                    } else {
                        JOptionPane.showMessageDialog(this, "URL not found for " + selectedOption);
                    }
                } else {
                    int jokeNumber = jokeIndex;
                    JOptionPane.showMessageDialog(this, jokes[jokeNumber]);
                }
            } else {
                JOptionPane.showMessageDialog(this, "Please enter a name!");
            }
        }
    }

    private void openURL(String url) {
        try {
            Desktop.getDesktop().browse(new URI(url));
        } catch (URISyntaxException | IOException ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ChatBox1());
    }
}
