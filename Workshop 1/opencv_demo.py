import cv2 as cv2
import numpy as np

# Display base images
haystack_img = cv2.imread("haystack_img.png", cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread("needle_img.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("Screenshot", haystack_img)
cv2.waitKey()
cv2.destroyAllWindows()

# Process base image through template matching
result = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()

# Find the highest scored location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

needle_img_height = needle_img.shape[0]
needle_img_width = needle_img.shape[1]

# Draw rectangle over the highest scored area
cv2.rectangle(haystack_img, max_loc,
              (max_loc[0] + needle_img_width, max_loc[1] + needle_img_height), (255, 0, 255), 3)

cv2.imshow("Screenshot", haystack_img)
cv2.waitKey()
cv2.destroyAllWindows()

# Initialize another object
needle2_img = cv2.imread("needle2_img.png", cv2.IMREAD_UNCHANGED)
needle2_img_height = needle2_img.shape[0]
needle2_img_width = needle2_img.shape[1]

# Use tresholding to locate every location above a certain score
result = cv2.matchTemplate(haystack_img, needle2_img, cv2.TM_CCOEFF_NORMED)
cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()

# Filter out results below the threshold
threshold = 0.4
yloc, xloc = np.where(result >= threshold)

# Generate rectangles to bound detected objects
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x),
                       int(y),
                       int(needle2_img_width),
                       int(needle2_img_height)])
    rectangles.append([int(x),
                       int(y),
                       int(needle2_img_width),
                       int(needle2_img_height)])

# Group rectangles that are too close to each other
rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

# Draw rectangles on haystack image
for (x, y, w, h) in rectangles:
    cv2.rectangle(haystack_img, (x, y), (x+w, y+h), (255, 255, 0), 3
                  )

cv2.imshow("Screenshot", haystack_img)
cv2.waitKey()
cv2.destroyAllWindows()
