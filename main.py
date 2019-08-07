# -------------------------------------------------- #
#    GUI Car picture crawler and detector program    #
#    by. 294                                         #
# -------------------------------------------------- #

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
import multiprocessing as mul
import sys
import time
import os
import cv2
from res import design
from res.cafe import mssd as m

# TEST MODE TRIGGER [ 0 : NONE, 1 : ACTIVE, 2 : WEB CAM MODE ]
# LOAD IMAGES DIRECTLY IN DEBUG FOLDER
test_mode = 0


# -------------------------------------------- #
#             DOWNLOAD IMAGE(FUNC)             #
# -------------------------------------------- #
def download_image(var, path):
    a = var.split("/")
    filename = a[-1]
    download_path = path + filename
    urllib.request.urlretrieve(var, download_path)


def download_image2(request_url_addr):
    html_page = urllib.request.urlopen(request_url_addr)
    soup = BeautifulSoup(html_page, 'html.parser')
    download_url = list(soup.findAll("a", {'class': 'preview'}))
    for value in download_url:
        url = value["href"]
        a = url.split('/')
        print("작업중...." + url)
        mypath = 'test'
        download_path = os.path.join(mypath, a[-1])
        urllib.request.urlretrieve(url, download_path)


# -------------------------------------------- #
#                 MAIN THREAD                  #
# -------------------------------------------- #
class Main(QThread):
    def __init__(self, path, brand, model, grade,
                 terminal, list_form, all_c, cur_c, count):
        super(self.__class__, self).__init__()
        QThread.__init__(self)
        self.path = path
        self.terminal = terminal
        self.brand = brand
        self.model = model
        self.grade = grade
        self.list_form = list_form
        self.all_c = all_c
        self.cur_c = cur_c
        self.set_count = count
        self.cpu_count = mul.cpu_count()

        if mul.cpu_count() - 4 <= 0:
            self.pool_count = 2
            self.download_p = Pool(self.pool_count)
        else:
            self.pool_count = mul.cpu_count() - 4
            self.download_p = Pool(self.pool_count)

    def __del__(self):
        self.wait()

    def run(self):
        def get_address():
            out = []
            self.terminal.append("Enter SK-Encar Website...")
            target_url = 'http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.' + self.brand + '._.(C.ModelGroup.' + self.model + '._.Model.' + self.grade + '.))))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A50%7D'
            driver.get(target_url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            find = soup.find('tbody', {'id': 'sr_normal'})
            find2 = list(find.findAll('tr'))
            self.terminal.append("Found " + str(len(find2)) + " lists.")

            for val in find2:
                links = val.find("a")
                _url = links["href"]
                driver.get('http://www.encar.com' + _url)
                founded_html = driver.page_source
                find3 = BeautifulSoup(founded_html, 'html.parser')
                find_span = list(find3.findAll('li', {'class': 'frame'}))

                if self.set_count != "COUNT":
                    for val2 in find_span:
                        onf = val2.find("a")
                        if onf:
                            swa_pic = onf["onfocus"]
                            swa_pic = swa_pic.split("'")
                            out.append(swa_pic[1])
                            self.all_c.setText("TOTAL : " + str(len(out)))
                            if int(len(out)) >= int(self.set_count):
                                return out
                else:
                    for val2 in find_span:
                        onf = val2.find("a")
                        if onf:
                            swa_pic = onf["onfocus"]
                            swa_pic = swa_pic.split("'")
                            out.append(swa_pic[1])
                            self.all_c.setText("TOTAL : " + str(len(out)))

            return out

        # Main thread core
        start_time = time.time()
        path = self.path
        self.terminal.append("[ Program launched. Your Computer thread count : {0} ]".format(self.cpu_count))
        opt = Options()
        opt.add_argument('headless')
        opt.add_argument('window-size=1920x1080')
        opt.add_argument('disable-gpu')
        driver = webdriver.Chrome(options=opt)
        data = get_address()
        count = int(len(data))
        self.list_form.clear()
        if count == 0:
            self.terminal.append("Nothing to download")
        else:
            self.terminal.append("Found " + str(count) + " pictures")

        if self.set_count != "COUNT":
            final_cnt = int(self.set_count)
            count = final_cnt
            self.terminal.append("Download count has enabled")
            self.terminal.append("Program will download " + str(count) + " picture(s)")

        # download images pool
        for r in data:
            a = r.split("/")
            filename = a[-1]
            download_path = path + filename
            self.download_p.starmap(download_image, zip([r], [path]))
            self.cur_c.setText("LEFT : " + str(count))
            self.list_form.addItem(download_path)
            count = count - 1
            if count == 0:
                break

        self.download_p.close()
        self.download_p.join()
        end_time = round(time.time() - start_time, 1)
        self.terminal.append("JOB DONE! [ TIME: {0}SEC, THREAD USED : {1} ]".format(str(end_time), self.pool_count))

        driver.quit()


# -------------------------------------------- #
#                  GUI THREAD                  #
# -------------------------------------------- #
class Gui(QMainWindow, design.Ui_MainWindow, QThread):
    def __init__(self):
        QThread.__init__(self)
        super(self.__class__, self).__init__()
        self.popup = QMessageBox()
        self.setupUi(self)
        self.btn_download.setEnabled(False)
        self.btn_view_func_1.setEnabled(False)
        self.btn_view_func_2.setEnabled(False)
        self.btn_view_func_3.setEnabled(False)
        self.btn_dir.clicked.connect(self.seldir)
        self.btn_download.clicked.connect(self.start_main)
        self.btn_view_func_1.clicked.connect(self.view_gray)
        self.btn_view_func_2.clicked.connect(self.view_invert)
        self.btn_view_func_3.clicked.connect(self.detection)
        self.listWidget.clicked.connect(self.show_listitem)
        if test_mode == 1:
            self.win_log.append("[ TEST MODE ACTIVATED. LOAD SAMPLE IMAGES IN ./test ]")
            self.load_folder(path="")

    def start_main(self):
        self.win_log.clear()
        set_path = self.set_path
        brand = self.com_brand.currentText()
        model = self.com_model.currentText()
        grade = self.com_grade.currentText()
        count = self.com_count.currentText()
        terminal = self.win_log
        list_form = self.listWidget
        all_c = self.lab_info2
        cur_c = self.lab_info3
        self.core = Main(set_path, brand, model, grade, terminal, list_form, all_c, cur_c, count)
        self.btn_dir.setEnabled(False)
        self.btn_download.setEnabled(False)
        self.com_brand.setEnabled(False)
        self.com_model.setEnabled(False)
        self.com_grade.setEnabled(False)
        self.com_count.setEnabled(False)
        self.btn_view_func_1.setEnabled(False)
        self.btn_view_func_2.setEnabled(False)
        self.btn_view_func_3.setEnabled(False)
        try:
            self.core.start()
        except Exception as e:
            print(e)

        self.core.finished.connect(self.done)

    def show_listitem(self):
        self.btn_view_func_1.setEnabled(True)
        self.btn_view_func_2.setEnabled(True)
        self.btn_view_func_3.setEnabled(True)
        selected = self.listWidget.currentItem().text()
        print(selected)
        ori_img = cv2.imread(selected)
        ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
        show_image = QImage(ori_img.data, ori_img.shape[1], ori_img.shape[0], QImage.Format_RGB888)
        self.win_pic.setPixmap(QPixmap.fromImage(show_image))

    def view_gray(self):
        img = self.listWidget.currentItem().text()
        ori_img = cv2.imread(img)
        ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
        show_image = QImage(ori_img.data, ori_img.shape[1], ori_img.shape[0], QImage.Format_Grayscale8)
        self.win_pic.setPixmap(QPixmap.fromImage(show_image))

    def view_invert(self):
        img = self.listWidget.currentItem().text()
        ori_img = cv2.imread(img)
        b, g, r = cv2.split(ori_img)
        invert_img = cv2.merge((255-b, 255-g, 255-r))
        show_image = QImage(invert_img.data, invert_img.shape[1], invert_img.shape[0], QImage.Format_RGB888)
        self.win_pic.setPixmap(QPixmap.fromImage(show_image))

    def seldir(self):
        self.set_path = QtWidgets.QFileDialog.getExistingDirectory(None, "SELECT PATH") + "/"
        self.lab_paths.setText(self.set_path)
        self.load_folder(self.set_path)
        self.btn_download.setEnabled(True)

    def detection(self):
        try:
            image = self.listWidget.currentItem().text()
            ori_img = m.showpic(image)
            b, g, r = cv2.split(ori_img)
            invert_img = cv2.merge((r, g, b))
            show_image = QImage(invert_img.data, invert_img.shape[1], invert_img.shape[0], QImage.Format_RGB888)
            self.win_pic.setPixmap(QPixmap.fromImage(show_image))
        except Exception as e:
            print(e)
            self.win_log.append("ERROR: Nothing detected or image is too big")

    # IF DEBUG MODE ACTIVATED
    def load_folder(self, path):
        self.listWidget.clear()

        if test_mode == 1:
            path = "./test"

        if path == '':
            return
        cnt = self.listWidget.count()
        du_cnt = 0
        add_list = []
        cur_files = []
        sel_files = []
        for i in os.listdir(path):
            sel_files.append(path + "/" + i)

        if not cnt == 0:
            for i in range(cnt):
                cur_files.append(self.listWidget.item(i).text())

        for file in sel_files:
            if not cnt == 0:
                for r in cur_files:
                    if file == r:
                        du_cnt += 1
            else:
                if file.endswith(".jpg") or file.endswith(".png"):
                    add_list.append(file)

        for f in add_list:
            self.listWidget.addItem(f)
            self.done()

    # JOB DONE!
    def done(self):
        if test_mode == 1:
            self.btn_dir.setEnabled(False)
            self.btn_download.setEnabled(False)
            self.com_brand.setEnabled(False)
            self.com_model.setEnabled(False)
            self.com_grade.setEnabled(False)
            self.com_count.setEnabled(False)
        else:
            self.btn_dir.setEnabled(True)
            self.btn_download.setEnabled(True)
            self.com_brand.setEnabled(True)
            self.com_model.setEnabled(True)
            self.com_grade.setEnabled(True)
            self.com_count.setEnabled(True)
            self.lab_info2.setText("TOTAL : ")
            self.lab_info3.setText("LEFT : ")

# 이전 작품 크롤러
class WallPaper:
    def get_html_addr(self, keyword):
        html_page = urllib.request.urlopen("https://kr.freeimages.com/search/" + str(keyword))
        soup = BeautifulSoup(html_page, 'html.parser')
        lists = list(soup.findAll("li", {'class': 'item'}))
        output = []
        for value in lists:
            into_soup = value.find("a")
            _url = into_soup["href"]
            output.append('https://kr.freeimages.com' + _url)
        return output

    def main(self):
        cpus = mul.cpu_count()
        directory = 'test'
        key = 'fox'
        poolcount = 4
        print("총 {0} 개의 프로세스가 감지되었습니다.".format(cpus))
        print("키워드는 {0}, 사용할 프로세서 수는 {1} 입니다. {2} 폴더에 저장됩니다".format(key, poolcount, directory))

        html_p = Pool(poolcount)

        data = html_p.map(self.get_html_addr, [i for i in [key]])

        for r in data:
            print(r)

        html_p.close()
        html_p.join()

        download_p = Pool(poolcount)
        for r in data:
            download_p.map(download_image2, r)

        # for urls in data:
        #     download_url = download_p.map(download_image, urls)
        download_p.close()
        download_p.join()


def main():
    if test_mode == 2:
        m.playvid()
    else:
        try:
            app = QApplication(sys.argv)
            form = Gui()
            form.show()
            exit(app.exec_())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
