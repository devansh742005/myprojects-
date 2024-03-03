import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ImageComparator {

    public static void main(String[] args) {
        // Replace "path/to/images" with the actual path to your image folder
        String folderPath = "path/to/images";
        File folder = new File(folderPath);

        File[] files = folder.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isFile() && file.getName().endsWith(".png")) {
                    compareAndHighlightDifferences("C:\Users\ADMIN\Desktop\Xray", file.getAbsolutePath());
                }
            }
        }
    }

    private static void compareAndHighlightDifferences(String referenceImagePath, String imagePath) {
        try {
            BufferedImage referenceImage = ImageIO.read(new File(referenceImagePath));
            BufferedImage imageToCompare = ImageIO.read(new File(imagePath));

            int width = referenceImage.getWidth();
            int height = referenceImage.getHeight();

            int differences = 0;

            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    int rgbReference = referenceImage.getRGB(x, y);
                    int rgbCompare = imageToCompare.getRGB(x, y);

                    if (rgbReference != rgbCompare) {
                        differences++;
                        // You can highlight differences by modifying pixel values or saving the differences
                        // imageToCompare.setRGB(x, y, Color.RED.getRGB());
                    }
                }
            }

            double totalPixels = width * height;
            double differencePercentage = (differences / totalPixels) * 100;

            System.out.println("Image: " + imagePath);
            System.out.println("Difference Percentage: " + differencePercentage + "%");

            if (differencePercentage < 69) {
                // Save or process the image with highlighted differences
                // ImageIO.write(imageToCompare, "png", new File("path/to/output/differences_" + imagePath));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}