import face_detector, cv2

class TemplateTracking:


    # template -- template for tracking; position -- template position on image; image - cur image
    def do_Track_in_Frame(self, template, position, image):
        (x, y, w, h) = self.area_To_Track(position, (len(image[0]), len(image)))
        res = cv2.matchTemplate(image[y:y+h, x:x+w], template, cv2.TM_SQDIFF_NORMED)
        miv_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        min_loc = (min_loc[0] + x, min_loc[1] + y)
        max_loc = (max_loc[0] + x, max_loc[1] + y)
        return miv_val, max_val, min_loc, max_loc

    def area_To_Track(self, position, max_size, coef = 2):
        x1 = position[0] - position[2]//2
        y1 = position[1] - position[3]//2
        x2 = position[0] + position[2]*3//2
        y2 = position[1] + position[3]*3//2

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > max_size[0]:
            x2 = max_size[0]
        if y2 > max_size[1]:
            y2 = max_size[1]

        return (x1, y1, x2 - x1, y2 - y1)



