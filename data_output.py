# -*- coding: UTF-8 -*-
import codecs


class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_out = codecs.open('baike.html', 'w', encoding='utf-8')
        file_out.write("<!DOCTYPE html>")
        file_out.write('<html lang="en">')
        file_out.write('<head><meta charset="UTF-8"><title>Title</title></head>')
        file_out.write("<body>")
        file_out.write("<table>")
        for data in self.datas:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['url'])
            file_out.write("<td>%s</td>" % data['title'])
            file_out.write("<td>%s</td>" % data['summary'])
            file_out.write("</tr>")
            self.datas.remove(data)
        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()
