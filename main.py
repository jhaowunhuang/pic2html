import cv2


def rgb2hex(rgb_arr):
    return '#%02x%02x%02x' % tuple(rgb_arr[::-1])
    

def pic2html(input_image, output_html):
    img = cv2.imread(input_image)
    h, w, _ = img.shape
    h //= 10
    w //= 10
    img = cv2.resize(img, (h, w), interpolation = cv2.INTER_AREA) 
    cvt_img = map(lambda arr: map(rgb2hex, arr), img)
    content = '<html><head></head><body>'
    content += '<table style=\"font-size:0px; height: ' + str(h) + 'px; width: ' + str(w) + 'px\" cellspacing=0 cellpadding=0 border=0>'
    for i, row in enumerate(cvt_img):
        content += '<tr>'
        for j, elem in enumerate(row):
            content += '<td bgcolor=' + elem + '>&nbsp;</td>'
        content += '</tr>'
    content += '</table></body></html>'
    with open(output_html, 'w') as f_out:
        f_out.write(content)


pic2html('cat.jpg', 'out.html')
