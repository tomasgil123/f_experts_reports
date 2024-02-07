from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.pdfgen import canvas
import os

def add_images_to_pdf(folder_path, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    page_width, page_height = letter
    current_height = page_height - 100

    # Unlike most popular desktop application development libraries, 
    # in ReportLab the origin of the coordinates (that is, the (0, 0) position) is at the bottom left.

    sorted_filename_list = sorted(os.listdir(folder_path), key=lambda x: int(x.split('_')[-1].split('.')[0]))
    print("sorted_filename_list", sorted_filename_list)

    for filename in sorted_filename_list:
        print("filename", filename)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            img_path = os.path.join(folder_path, filename)

            img = utils.ImageReader(img_path)
            # Open the image and get its height
            original_img_width, original_img_height = img.getSize()

            # Calculate the new width and height
            new_img_width = page_width - 150  # 50 on the left and 50 on the right
            aspect_ratio = original_img_width / original_img_height
            new_img_height = new_img_width / aspect_ratio

            # Check if there is enough space on the current page
            # we add 100 because we want to leave some space at the bottom of the page
            space_missing = current_height - new_img_height - 100
            if space_missing < 0:

                ratio_space_missing_img_height = (abs(space_missing) / new_img_height)
                print("ratio_space_missing_img_height", ratio_space_missing_img_height)
                if ratio_space_missing_img_height < 0.3:
                    # we reduce the height and width of the image
                    new_img_height = new_img_height - abs(space_missing) - 10
                    new_img_width = new_img_height * aspect_ratio
                    current_height -= new_img_height  # Update current_height
                    # Set the position and add the image to the PDF with the new dimensions
                    x, y = 75, current_height  # Adjust the x position as needed
                    print("x", x)
                    print("y", y)
                    c.drawImage(img, x, y, width=new_img_width, height=new_img_height)
                    continue

                c.showPage()  # Add a new page if not enough space
                current_height = page_height - 100  # Reset current_height for the new page
                current_height -= new_img_height  # Update current_height
                x, y = 75, current_height  # Adjust the x position as needed
                print("y next page", y)
                c.drawImage(img, x, y, width=new_img_width, height=new_img_height)
                
                print("-------we move to next page-------")
                continue
            
            current_height -= new_img_height  # Update current_height
            # Set the position and add the image to the PDF with the new dimensions
            x, y = 75, current_height  # Adjust the x position as needed
            print("x", x)
            print("y", y)
            c.drawImage(img, x, y, width=new_img_width, height=new_img_height)
            

    c.save()

folder_path = "./report_images"
output_pdf = "./pdf_reports/competitors_analytics_report.pdf"

add_images_to_pdf(folder_path, output_pdf)