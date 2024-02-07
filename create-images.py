import asyncio
from playwright.async_api import async_playwright

async def capture_between_elements(page, selector_start, selector_end, output_path):
    print("selector_start", selector_start)
    # Scroll the element into view using page.evaluate()
    await page.evaluate(f'document.getElementById("{selector_start}").scrollIntoView();')
    await asyncio.sleep(2)
            # Get the bounding boxes of the two elements
    element1 = page.locator(f"#{selector_start}")
    element2 = page.locator(f"#{selector_end}")

        # bounding_box() allows you to retrieve information about the position and size of an element on a web page

        # The "x" value represents the horizontal position of the top-left corner of the bounding box relative to the
        # left edge of the viewport or the entire page. For example, if "x" is 100 it means the left edge of the 
        # bounding box is 100 pixels to the right of the left edge of the viewport or page

        # The "y" value represents the vertical position of the top-left corner of the bounding box relative to the 
        # top edge of the viewport or the entire page. For example, if "y" is 200 it means the top edge of the 
        # bounding box is 50 pixels below the top edge of the viewport or page

        # "width" and "height" values represent the width and height of the bounding box in pixels
        # in this case of the div element selected with page.locator()
        
    bounding_box1 = await element1.bounding_box()
    bounding_box2 = await element2.bounding_box()
    print("bounding_box1", bounding_box1)
    print("bounding_box2", bounding_box2)

    clip_x = bounding_box1['x']
    clip_y = bounding_box1['y']
    clip_width = bounding_box1['width']
    clip_height = bounding_box2['y'] - bounding_box1['y']

    if bounding_box1 and bounding_box2:
        # Calculate the coordinates for the clip option
        clip = {
                "x": clip_x,
                "y": clip_y,
                "width": clip_width,
                "height": clip_height
            }

        # Take a screenshot of the area between the two elements
        await page.screenshot(path=output_path, clip=clip, full_page=True)


async def main(url, report_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1280, "height": 850})

        # Navigate to the example page (replace with your URL)
        await page.goto(url)

        # Wait for 15 seconds until the streamlit report loads
        await asyncio.sleep(15)

        # we select all the elements with the class "element-container"
        elements = await page.query_selector_all('section.main .element-container')  

        # Loop through the selected elements and perform actions
        for index, element in enumerate(elements):

            # we don't want to take screenshots of streamlit widgets 
            has_row_widget = await element.query_selector('.row-widget')
            if has_row_widget:
                continue
            
            await element.scroll_into_view_if_needed()
            await asyncio.sleep(2)

            bounding_box = await element.bounding_box()

            # bounding_box() allows you to retrieve information about the position and size of an element on a web page

            # The "x" value represents the horizontal position of the top-left corner of the bounding box relative to the
            # left edge of the viewport or the entire page. For example, if "x" is 100 it means the left edge of the 
            # bounding box is 100 pixels to the right of the left edge of the viewport or page

            # The "y" value represents the vertical position of the top-left corner of the bounding box relative to the 
            # top edge of the viewport or the entire page. For example, if "y" is 200 it means the top edge of the 
            # bounding box is 50 pixels below the top edge of the viewport or page

            # "width" and "height" values represent the width and height of the bounding box in pixels
            # in this case of the div element selected with page.locator()
            
            print("bounding_box", bounding_box)
            # if element "height" is 0, we skip it (it means it is not a visible element)
            if bounding_box['height'] == 0:
                continue
            
            clip_x = 456
            clip_y = bounding_box['y']
            clip_width = 704
            clip_height = bounding_box['height']

            clip = {
                "x": clip_x,
                "y": clip_y,
                "width": clip_width,
                "height": clip_height
            }

            output_path = f"./report_images/{report_name}_{index}.png"

            await page.screenshot(path=output_path, clip=clip, full_page=True)

        # Close the browser and finish the test
        await browser.close()

report_name = "competitors_analysis"
asyncio.run(main(url="http://localhost:8501/", report_name=report_name))





# Define a function to capture the content between two elements
# def capture_between_elements(url, selector1, selector2, output_path):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         # Set the viewport size to simulate a desktop screen
#         page.set_viewport_size({"width": 1280, "height": 1000})
#         page.goto(url)

#         # Get the bounding boxes of the two elements
#         element1 = page.locator(selector1)
#         element2 = page.locator(selector2)

#         # bounding_box() allows you to retrieve information about the position and size of an element on a web page

#         # The "x" value represents the horizontal position of the top-left corner of the bounding box relative to the
#         # left edge of the viewport or the entire page. For example, if "x" is 100 it means the left edge of the 
#         # bounding box is 100 pixels to the right of the left edge of the viewport or page

#         # The "y" value represents the vertical position of the top-left corner of the bounding box relative to the 
#         # top edge of the viewport or the entire page. For example, if "y" is 200 it means the top edge of the 
#         # bounding box is 50 pixels below the top edge of the viewport or page

#         # "width" and "height" values represent the width and height of the bounding box in pixels
#         # in this case of the div element selected with page.locator()
        
#         bounding_box1 = element1.bounding_box()
#         bounding_box2 = element2.bounding_box()
#         print("bounding_box1", bounding_box1)
#         print("bounding_box2", bounding_box2)

#         clip_x = bounding_box1['x']
#         clip_y = bounding_box1['y']
#         clip_width = bounding_box1['width']
#         clip_height = bounding_box2['y'] - bounding_box1['y']

#         print("bounding_box2['y']", bounding_box2['y'])
#         page.evaluate(f"window.scrollTo(0, {bounding_box2['y']})")

#         page.wait_for_timeout(5000)

#         if bounding_box1 and bounding_box2:
#             # Calculate the coordinates for the clip option
#             clip = {
#                 "x": clip_x,
#                 "y": clip_y,
#                 "width": clip_width,
#                 "height": clip_height
#             }

#             # Take a screenshot of the area between the two elements
#             page.screenshot(path=output_path, clip=clip, full_page=True)

#         browser.close()

# # Example usage
# #capture_between_elements("http://localhost:8501/", "#start", "#end", "between_elements_screenshot.png")

# list_sections = [
#                     ["start_total_reviews", "end_total_reviews"],
#                     [ "start_average_rating_reviews", "end_average_rating_reviews"], 
#                     ["start_total_reviews_per_month", "end_total_reviews_per_month"], 
#                     ["start_most_common_words_in_reviews", "end_most_common_words_in_reviews"],
#                     ["start_most_common_words_product_titles", "end_most_common_words_product_titles"], 
#                     ["start_wholesale_product_prices", "end_wholesale_product_prices"],
#                     ["start_minimum_order_amount", "end_minimum_order_amount"],
#                     ["start_fulfillment_speed", "end_fulfillment_speed"]
#                 ]

# for section in list_sections:
#     print("sexction", section)
#     capture_between_elements("http://localhost:8501/", f"#{section[0]}", f"#{section[1]}", f"./report_images/{section[0]}.png")