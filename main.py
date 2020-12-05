import cv2


def rgb2hex(rgb_arr):
    return '#%02x%02x%02x' % tuple(rgb_arr)
    

def pic2html(input_image, output_html):
    img = cv2.imread(input_image)
    w, h, _ = img.shape
    cvt_img = map(lambda arr: map(rgb2hex, arr), img)
    content = ''
    for i, row in enumerate(cvt_img):
        if i >= 100:
            continue
        content += '<tr>'
        for j, elem in enumerate(row):
            if j >= 100:
                continue
            content += '<td bgcolor=' + elem + '>&nbsp;</td>'
        content += '</tr>'
    html_begin = '<html><head><style type=\"text/css\">table{table-layout:fixed;empty-cells:hide;height:100px;width:100px;border-top:0px;margin:0px;padding:0px;font-size:0px}</style></head><body><table cellspacing=0 cellpadding=0 border=0>'
    html_end = '</table></body></html>'
    with open(output_html, 'w') as f_out:
        f_out.write(html_begin)
        f_out.write(content)
        f_out.write(html_end)
        


pic2html('cat.jpg', 'out.html')
