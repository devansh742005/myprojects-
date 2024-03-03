import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.io.IOException;

public class XRayHealthAnalysis extends JFrame {
    private JLabel statusLabel;

    public XRayHealthAnalysis() {
        setTitle("Papyrus");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 750); // Increased height for accommodating the logo
        setLocationRelativeTo(null);

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());

        JButton selectImageButton = new JButton("Select X-ray Image");
        selectImageButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                int returnValue = fileChooser.showOpenDialog(null);
                if (returnValue == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    try {
                        BufferedImage xrayImage = ImageIO.read(selectedFile);
                        if (xrayImage != null) {
                            boolean isHealthy = analyzeXRayImage(xrayImage);
                            if (isHealthy) {
                                statusLabel.setText("The X-ray appears to be healthy.");
                            } else {
                                statusLabel.setText("The X-ray shows abnormalities.");
                            }
                        } else {
                            statusLabel.setText("Error: Unable to read the image.");
                        }
                    } catch (IOException ex) {
                        ex.printStackTrace();
                        statusLabel.setText("Error: Failed to open the image.");
                    }
                }
            }
        });

        statusLabel = new JLabel("Select an X-ray image to analyze its health.");
        statusLabel.setHorizontalAlignment(JLabel.CENTER);

        mainPanel.add(selectImageButton, BorderLayout.NORTH);
        mainPanel.add(statusLabel, BorderLayout.CENTER);

        // Adding logo panel at the bottom
        LogoPanel logoPanel = new LogoPanel();
        mainPanel.add(logoPanel, BorderLayout.SOUTH);

        add(mainPanel);

        setVisible(true);
    }

    private boolean analyzeXRayImage(BufferedImage xrayImage) {
        if (xrayImage == null) {
            return false; // Return false if the image is null
        }

        int width = xrayImage.getWidth();
        int height = xrayImage.getHeight();
        long totalPixelIntensity = 0;

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int pixel = xrayImage.getRGB(x, y);
                int red = (pixel >> 16) & 0xFF;
                int green = (pixel >> 8) & 0xFF;
                int blue = pixel & 0xFF;

                int pixelIntensity = (red + green + blue) / 3;
                totalPixelIntensity += pixelIntensity;
            }
        }

        long averagePixelIntensity = totalPixelIntensity / (width * height);
        int threshold = 100;
        return averagePixelIntensity > threshold;
    }

    static class LogoPanel extends JPanel {
        private BufferedImage logo;

        LogoPanel() {
            try {
                logo = ImageIO.read(new File("C:\\Users\\ADMIN\\Desktop\\STAN\\Designer.png"));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            if (logo != null) {
                int panelWidth = getWidth();
                int panelHeight = getHeight();
                
                int imgWidth = logo.getWidth();
                int imgHeight = logo.getHeight();

                double scaleFactor = Math.min(1.0 * panelWidth / imgWidth, 1.0 * panelHeight / imgHeight);

                int drawWidth = (int) (scaleFactor * imgWidth);
                int drawHeight = (int) (scaleFactor * imgHeight);

                int x = (panelWidth - drawWidth) / 2;
                int y = (panelHeight - drawHeight) / 2;
            

                g.drawImage(logo, x, y, drawWidth, drawHeight, this);
            }
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(200, 100);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new XRayHealthAnalysis());
    }
}
