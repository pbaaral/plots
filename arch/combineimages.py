from reportlab.pdfgen import canvas
from PIL import Image

def rotate_image(image_path, degrees):
    # Open the image and rotate it
    img = Image.open(image_path)
    rotated_img = img.rotate(degrees, expand=True)
    return rotated_img

def create_pdf(file_list, output_pdf):
    c = canvas.Canvas(output_pdf)

    # Define the number of images per page
    images_per_page = 2
    image_width = c._pagesize[0] / 2  # Assuming A4 size, divide by 2 for two columns

    # Loop through the list of files
    for i, filename in enumerate(file_list):
        if i % images_per_page == 0 and i != 0:
            c.showPage()  # Start a new page after every set of images

        # Calculate the position of the image on the page
        x = (i % 2) * image_width
        y = (i % images_per_page // 2) * (c._pagesize[1] / 2)

        # Rotate the image by 90 degrees
        rotated_image = rotate_image(filename, -90)

        # Draw the rotated image on the canvas
        c.drawInlineImage(rotated_image, x, y, width=image_width, height=c._pagesize[1] / 2)

    c.save()

if __name__ == "__main__":
    # List of your EPS file names
    eps_files = ["alpha_adna.eps", "alpha_zdna_zii.eps", "beta_zdna_zi.eps", "epsilon_bdna_bii.eps",
                 "gamma_bdna_bi.eps", "zeta_adna.eps", "zeta_zdna_zii.eps", "alpha_bdna_bi.eps",
                 "beta_adna.eps", "beta_zdna_zii.eps", "epsilon_zdna_zi.eps", "gamma_bdna_bii.eps",
                 "zeta_bdna_bi.eps", "alpha_bdna_bii.eps", "beta_bdna_bi.eps", "epsilon_adna.eps",
                 "epsilon_zdna_zii.eps", "gamma_zdna_zi.eps", "zeta_bdna_bii.eps", "alpha_zdna_zi.eps",
                 "beta_bdna_bii.eps", "epsilon_bdna_bi.eps", "gamma_adna.eps", "gamma_zdna_zii.eps",
                 "zeta_zdna_zi.eps"]

    # Output PDF file name
    output_pdf_name = "output_rotated.pdf"

    # Create the PDF with rotated images
    create_pdf(eps_files, output_pdf_name)


