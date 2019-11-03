import face_detector, cv2

class TemplateTracking:

    def do_Track_in_Frame(self, template, image):
        res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)
        miv_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return miv_val, max_val, min_loc, max_loc

